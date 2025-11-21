import pandas as pd
from extract import ExtractVendas
from transform import DataCleaner, FeatureEngineer, DataAggregator
from load import SaveDFPNG

class ETLVendas:
    def __init__(self):
        print("Iniciando processo ETL de Vendas...")

        self.df = pd.DataFrame()
        self._run()

    def _run(self):
        self._Extract()
        self._Transform()
        self._Load(self.df[:9])
        self._Load(self.df_agg, name="etl_vendas_aggregated")
        print("Processo ETL concluído.")

    def _Extract(self):
        '''Extrai os dados de vendas utilizando a classe ExtractVendas.'''
        ev = ExtractVendas()
        df_vendas = ev.extract_data()
        print("Extração concluída.")
        self.df = df_vendas
    
    def _Transform(self):
        dc = DataCleaner()
        self.df = dc.clear_data(self.df)
        print("Limpeza concluída."
              +"\n=========================")

        fe = FeatureEngineer()
        self.df = fe.apply_transforms(self.df)
        print("Transformações concluídas."
              +"\n=========================")
        
        da = DataAggregator()
        self.df_agg = da.aggregate_data(self.df) # Cria um novo DataFrame para os dados agregados
        print("Novo DataFrame agregado criado."
              +"\n=========================")
    
    def _Load(self, df: pd.DataFrame, name: str = "etl_vendas"):
        if 'id_cliente' in df.columns:
            df = df.sort_values('id_cliente', ascending=True).reset_index(drop=True)
        sv_png = SaveDFPNG()
        sv_png.save_df_png(df, name)
        print("Carregamento concluído. DataFrame salvo como PNG.")


if __name__ == "__main__":
    etl = ETLVendas()