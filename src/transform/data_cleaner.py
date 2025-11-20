import pandas as pd

class DataCleaner:
    def _repl_nan_segmento(self):
        '''Substitui valores NaN na coluna 'segmento' por 'Não classificado'.'''

        amount = self.df['segmento'].isna().sum()
        self.df['segmento'] = self.df['segmento'].fillna('Não classificado')

        print(f"{amount} valores NaN na coluna 'segmento' foram substituídos por 'Não classificado'.")

    def _rm_dup_id_venda(self):
        '''Remove linhas duplicadas com base na coluna 'id_venda', mantendo a ocorrência de maior valor em 'quantidade'.'''

        amount = self.df.duplicated(subset=['id_venda']).sum()
        self.df = self.df.sort_values('quantidade', ascending=False).drop_duplicates(subset=['id_venda'], keep='first')

        print(f"{amount} linhas duplicadas com base em 'id_venda' foram removidas, mantendo a ocorrência de maior valor em 'quantidade'.")

    def clear_data(self, df: pd.DataFrame) -> pd.DataFrame:
        '''Realiza a limpeza dos dados no DataFrame fornecido.'''

        self.df = df.copy()

        self._repl_nan_segmento()
        self._rm_dup_id_venda()

        return self.df