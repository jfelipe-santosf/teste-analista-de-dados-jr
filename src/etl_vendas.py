import pandas as pd
from extract import ExtractVendas
from transform import DataCleaner, FeatureEngineer, DataAggregator
from load import SaveDFPNG, LoadToMongo

class ETLVendas:
    def __init__(self):
        print("Iniciando processo ETL de Vendas...")

        self.df = pd.DataFrame()
        self._run()

    def _run(self):
        self._Extract()
        self._Transform()
        self._Load()
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
    
    def _Load(self):
        sv_png = SaveDFPNG()
        sv_png.save_df_png(self.df[:7], 'etl_vendas')
        sv_png.save_df_png(self.df_agg, 'etl_vendas_aggregated')

        lt_mongo = LoadToMongo()
        lt_mongo.load_data(self.df, collection_name="vendas_clientes", embedded_cols={
            "venda_info": ["id_venda", "data_venda", "trimestre", "quantidade", "preco_unitario", "desconto_percentual", "valor_liquido"],
        })
        lt_mongo.load_data(self.df_agg, collection_name="analise_vendas")

        print("Carregamento concluído. DataFrame salvo como PNG.")


if __name__ == "__main__":
    etl = ETLVendas()