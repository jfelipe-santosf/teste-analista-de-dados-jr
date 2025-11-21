# `E`xtração dos dados
Etapa de extração de dados.
1. Extrai de um banco de dados local [[mais]](/data/README.md).
2. Retorna um DataFrame com o resultado.

Por se tratar de algo simples como um db local procurei usar `métodos simples` para extrair os dados porém `redudantes`.

## Consulta SQL com JOIN

A consulta SQL utilizada nesta etapa realiza um `JOIN` entre as tabelas `clientes` e `vendas` para combinar os dados relacionados. O objetivo é obter informações completas sobre as vendas, incluindo os detalhes dos clientes associados. Abaixo está a consulta utilizada:

```sql
SELECT
    c.id_cliente,
    v.id_venda,
    c.nome,
    c.email,
    c.estado,
    c.segmento,
    v.data_venda,
    v.quantidade,
    v.preco_unitario,
    v.desconto_percentual
FROM clientes c
JOIN vendas v
    ON c.id_cliente = v.id_cliente;
```

### Explicação da Consulta

1. **Tabelas Envolvidas**:
   - `clientes`: Contém informações sobre os clientes, como nome, email, estado e segmento.
   - `vendas`: Contém informações sobre as vendas, como data, quantidade, preço unitário e desconto.

2. **Cláusula JOIN**:
   - A cláusula `JOIN` combina as tabelas `clientes` e `vendas` com base na chave estrangeira `id_cliente`.
   - Isso garante que cada venda esteja associada ao cliente correspondente.

3. **Colunas Selecionadas**:
   - Inclui colunas de ambas as tabelas para fornecer uma visão completa das vendas e dos clientes.

4. **Alias**:
   - O alias `AS nome_cliente` é usado para renomear a coluna `nome` da tabela `clientes`, tornando o resultado mais descritivo.

Esta consulta é essencial para a etapa de extração, pois fornece os dados necessários para as próximas etapas do processo ETL.

[Arquivo](/data/select.sql)

Um simples join para crusar id_cliente entre as duas tabelas.

## Documentação Adicional

- [Documentação do Banco de Dados](/data/README.md): Informações sobre o banco de dados `vendas.db`.