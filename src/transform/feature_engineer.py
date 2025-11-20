import pandas as pd

class FeatureEngineer:
    def _add_quarter(self):
        '''Adiciona uma coluna `trimestre` baseada na coluna `data_venda`.'''

        self.df['trimestre'] = pd.to_datetime(self.df['data_venda']).dt.quarter
        #soma total de cada semestre
        amount = [self.df['trimestre'].value_counts().get(i, 0) for i in range(1,5)]

        print("Coluna 'trimestre' adicionada ao DataFrame.")
        print(f"Registros por trimestre: \n1º: {amount[0]}, \n2º: {amount[1]}, \n3º: {amount[2]}, \n4º: {amount[3]}.")

    def _add_net_value(self):
        '''Adiciona uma coluna `valor_liquido` calculada como `preco_unitario` * `quantidade` * (1 - `desconto_percentual`/100).'''

        self.df['valor_liquido'] = (
            self.df['preco_unitario'] * self.df['quantidade']
            * (1 - self.df['desconto_percentual'] / 100)
        ).round(2) #calcula o valor líquido com duas casas decimais
        # soma total de linhas não nulas na coluna valor_liquido
        amount = self.df['valor_liquido'].notna().sum()

        print(f"{amount} valores na coluna 'valor_liquido' foram calculados e adicionados ao DataFrame.")

    def apply_transforms(self, df: pd.DataFrame) -> pd.DataFrame:
        '''Aplica transformações de engenharia de features no DataFrame.'''
        self.df = df.copy()

        self._add_quarter()
        self._add_net_value()

        return self.df