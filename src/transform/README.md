## Seção de `T`ransformação de dados

### Data cleaner
Aqui é feita a limpeza de dados em etapas:

1. **_repl_nan_segmento**: substitui valores nulos (none/NaN) na coluna segmento por *Não listado*

2. **_rm_dup_id_venda**: Remove id_vendas duplicados, mantendo o de maior valor.
> sort_values para organizar na ordem de quantidade, drop_duplicates e keep='first' para excluir duplicados e manter o primeiro.

Podendo se obter o dataframe limpo com o @property `cleaned_data` que retorna um dataframe.