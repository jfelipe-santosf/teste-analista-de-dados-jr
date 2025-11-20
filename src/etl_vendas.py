import pandas as pd
from extract import ExtractVendas
from transform import DataCleaner, FeatureEngineer
from load import SaveDFPNG

class ETLVendas:
    def __init__(self):
        print("Iniciando processo ETL de Vendas...")

        self.df = pd.DataFrame()
        self._run()

    def _run(self):
        self._Extract()
        self._Transform()
        self._Load(self.df)
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
        print("Limpeza concluída.")

        fe = FeatureEngineer()
        self.df = fe.apply_transforms(self.df)
    
    def _Load(self, df: pd.DataFrame):
        df.sort_values('id_cliente', inplace=True)
        sv_png = SaveDFPNG()
        sv_png.save_df_png(df[:9], 'vendas')
        print("Carregamento concluído. DataFrame salvo como PNG.")


if __name__ == "__main__":
    etl = ETLVendas()