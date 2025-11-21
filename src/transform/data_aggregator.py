import pandas as pd

class DataAggregator:
    def _calculate_aov(self):
        '''Calcula o Valor Médio de Vendas (AOV) por `estado` e `segmento`.'''

        self.df = (
            self.df_src.groupby(['estado', 'segmento']) # Agrupa por estado e segmento
            ['valor_liquido'].mean() # Calcula a média do valor líquido
            .reset_index() # Reseta o índice após o agrupamento para transformar em DataFrame
            .rename(columns={'valor_liquido': 'AOV'})
        ).round(2)

        print("Cálculo do AOV por estado e segmento concluído.")

    def _calculate_total_sales(self):
        '''Calcula o Total de Vendas por `estado` e `segmento`.'''

        total_sales = (
            self.df_src.groupby(['estado', 'segmento']) # Agrupa por estado e segmento
            ['valor_liquido'].count() # Soma a quantidade de vendas
            .reset_index()
            .rename(columns={'valor_liquido': 'total_vendas_count'})
        )
        value_total_sales = (
            self.df_src.groupby(['estado', 'segmento'])
            ['valor_liquido'].sum() # Calcula a soma do valor líquido
            .reset_index()
            .rename(columns={'valor_liquido': 'total_vendas_value'})
        ).round(2)

        # pd.merge Mescla os DataFrames com base em estado e segmento
        self.df = pd.merge(self.df, total_sales, on=['estado', 'segmento'])
        self.df = pd.merge(self.df, value_total_sales, on=['estado', 'segmento'])

        print("Cálculo do Total de Vendas por estado e segmento concluído.")

    def aggregate_data(self, df: pd.DataFrame) -> pd.DataFrame:
        '''Calcular Valor Médio de Vendas (AOV) por `estado` e `segmento` e calcular Total de Vendas por `estado` e `segmento`'''

        self.df_src = df.copy()
        self.df = pd.DataFrame()

        self._calculate_aov()
        self._calculate_total_sales()

        return self.df