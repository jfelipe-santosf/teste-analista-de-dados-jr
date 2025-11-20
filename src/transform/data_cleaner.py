import pandas as pd

class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def _repl_nan_segmento(self):
        '''Substitui valores NaN na coluna 'segmento' por 'Não classificado'.'''

        self.df['segmento'] = self.df['segmento'].fillna('Não classificado')

        print("Valores NaN na coluna 'segmento' foram substituídos por 'Não classificado'.")

    def _rm_dup_id_venda(self):
        '''Remove linhas duplicadas com base na coluna 'id_venda', mantendo a ocorrência de maior valor em 'quantidade'.'''

        self.df = self.df.sort_values('quantidade', ascending=False).drop_duplicates(subset=['id_venda'], keep='first')

        print("Linhas duplicadas com base em 'id_venda' foram removidas, mantendo a ocorrência de maior valor em 'quantidade'.")

    @property
    def cleaned_data(self) -> pd.DataFrame:
        '''Retorna o DataFrame limpo após aplicar as transformações.'''

        self._repl_nan_segmento()
        self._rm_dup_id_venda()
        return self.df