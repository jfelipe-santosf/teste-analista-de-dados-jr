import matplotlib.pyplot as plt

class SaveDFPNG:
    def save_df_png(self, df, name_png):
        path_png = f'output/{name_png}.png'

        df = df.sort_values(by=df.columns[0]) # Ordenar pela primeira coluna

        # Criar figura proporcional à quantidade de linhas
        fig, ax = plt.subplots(figsize=(12, 0.4 * len(df) + 1))
        ax.axis('off')

        # Criar tabela
        tabela = ax.table(
            cellText=df.values,
            colLabels=df.columns,
            loc='center'
        )

        # Ajustar aparência
        tabela.auto_set_font_size(True)
        tabela.set_fontsize(8)
        tabela.scale(1, 1.5)  # aumentar altura das linhas

        plt.savefig(path_png, dpi=300, bbox_inches='tight')
        plt.close()

        print(f"Imagem salva em: {path_png}")

    def save_graph(self, df, x_col, y_col, graph_name):
        """
        Salva um gráfico PNG com base em um DataFrame.

        :param df: DataFrame contendo os dados.
        :param x_col: Nome da coluna para o eixo X.
        :param y_col: Nome da coluna para o eixo Y.
        :param graph_name: Nome do arquivo PNG a ser salvo.
        """

        df = (
            df.groupby(x_col)[y_col].max().reset_index()
        )

        path_png = f'output/{graph_name}.png'

        # Criar o gráfico
        plt.figure(figsize=(10, 6))
        plt.plot(df[x_col], df[y_col], marker='o')
        plt.title(f'Gráfico de {y_col} por {x_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.grid(True)

        # Salvar o gráfico como PNG
        plt.savefig(path_png, dpi=300, bbox_inches='tight')
        plt.close()

        print(f"Gráfico salvo em: {path_png}")