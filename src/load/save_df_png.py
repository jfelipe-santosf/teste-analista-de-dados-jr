import matplotlib.pyplot as plt

class SaveDFPNG:
    def save_df_png( df, name_png):
        path_png = f'output/{name_png}.png'

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