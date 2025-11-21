# Seção de `T`ransformação de dados
Etapa de transformação foi dividida em três partes: `limpeza dos dados`, `engenharia de features` e `agregação`.
## [Data cleaner](/src/transform/data_cleaner.py)
Aqui é feita a limpeza de dados em etapas:

1. **_repl_nan_segmento**: Substitui valores nulos (none/NaN) na coluna `segmento` por *'Não listado'*

2. **_rm_dup_id_venda**: Remove id_vendas duplicados, mantendo o de maior `quantidade`.
> sort_values para organizar na ordem de quantidade, drop_duplicates e keep='first' para excluir duplicados e manter o primeiro.

### Executar
Basta chamar pelo método `clear_data`, passando o DataFrame, então ele retorna o DF limpo.

## [Feature engineer](/src/transform/feature_engineer.py)
Aqui são adiconadas as colunas `trimestre` e `valor_liquido` ao DF principal.

- **_add_quarter**: Adiciona uma coluna `trimestre` baseada na coluna `data_venda`.
- **_add_net_value**: Adiciona uma coluna `valor_liquido` calculada como:
    - preço_und × qtd × (1 - desconto ÷ 100).

### Executar
Basta chamar o método `apply_transforms`, passando o DataFrame, então ele retorna o DF com as novas colunas.

## [Data aggregator](/src/transform/data_aggregator.py)
A partir do DF princiapl calcula o Valor Médio de Vendas (AOV) por `estado` e `segmento` e calcular Total de Vendas por `estado` e `segmento`, inserindo em um novo DF.

- **_calculate_aov**: Calcula AOV.
- **_calculate_total_sales**: Adiciona duas colunas:
    - `total_vendas_count`: Quantidade de vendas por `seguimento` e `estado`.
    - `total_vendas_value`: Valor total (soma) de vendas por `seguimento` e `estado`.

### Executar
Basta chamar o método `aggregate_data`, passando o DataFrame, então ele retorna um DF com a seguinte estrutura:

```csv
estado | segmento | AOV | total_vendas_count | total_vendas_count
 str       str     float        int                 float
```