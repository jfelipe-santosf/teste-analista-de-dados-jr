import matplotlib.pyplot as plt

class SaveDFPNG:
    def save_df_png( df, name_png, start=None, end=None, max_rows=None):
        path_png = f'output/{name_png}.png'

        # Definir fatia do DF
        if start is not None or end is not None:
            df_plot = df[start:end]
        elif max_rows is not None:
            df_plot = df.head(max_rows)
        else:
            df_plot = df

        # Criar figura proporcional à quantidade de linhas
        fig, ax = plt.subplots(figsize=(12, 0.4 * len(df_plot) + 1))
        ax.axis('off')

        # Criar tabela
        tabela = ax.table(
            cellText=df_plot.values,
            colLabels=df_plot.columns,
            loc='center'
        )

        # Ajustar aparência
        tabela.auto_set_font_size(True)
        tabela.set_fontsize(8)
        tabela.scale(1, 1.5)  # aumentar altura das linhas

        plt.savefig(path_png, dpi=300, bbox_inches='tight')
        plt.close()

        print(f"Imagem salva em: {path_png}")