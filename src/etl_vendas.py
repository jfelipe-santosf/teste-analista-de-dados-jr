import pandas as pd
from extract import EVendas
from transform import DataCleaner
from load import SaveDFPNG

class ETLVendas:
    def __init__(self):
        print("Iniciando processo ETL de Vendas...")

        self.df = pd.DataFrame()
        self.run()

    def run(self):
        self.Extract()
        self.Transform()
        self.Load(self.df)
        print("Processo ETL concluído.")

    def Extract(self):
        '''Extrai os dados de vendas utilizando a classe EVendas.'''
        evendas = EVendas()
        df_vendas = evendas.extract_data()
        print("Extração concluída.")
        self.df = df_vendas
    
    def Transform(self):
        data_cleaner = DataCleaner(self.df)
        self.df = data_cleaner.cleaned_data
        print("Limpeza concluída.")
    
    def Load(self, df: pd.DataFrame):
        sv_png = SaveDFPNG()
        sv_png.save_df_png(df, 'vendas_cleaned')
        print("Carregamento concluído. DataFrame salvo como PNG.")


if __name__ == "__main__":
    etl = ETLVendas()