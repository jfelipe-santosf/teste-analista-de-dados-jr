import pandas as pd
from extract.e_vendas import EVendas
from load import SaveDFPNG

class ETLVendas:
    def __init__(self):
        evendas = EVendas()
        self.extractor = evendas.extract_data()

        SaveDFPNG.save_df_png(self.extractor, 'vendas_etl_output', start=50, end=78)

if __name__ == "__main__":
    etl = ETLVendas()