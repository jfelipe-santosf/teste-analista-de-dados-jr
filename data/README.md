# Banco de Dados: vendas.db

Este banco de dados foi gerado aleatoriamente por uma inteligência artificial para fins de teste e análise. Ele contém duas tabelas principais:

## Estrutura do Banco de Dados

### Tabela: clientes
- **id_cliente**: Identificador único do cliente (chave primária).
- **nome**: Nome do cliente.
- **email**: Endereço de email único.
- **estado**: Estado (UF) do cliente, limitado aos 9 principais estados do Brasil.
- **segmento**: Segmento de mercado do cliente (alguns valores podem ser nulos).

### Tabela: vendas
- **id_venda**: Identificador da venda (alguns valores podem ser duplicados).
- **id_cliente**: Identificador do cliente associado à venda (chave estrangeira para `clientes.id_cliente`).
- **data_venda**: Data da venda (últimos 12 meses). 
- **quantidade**: Quantidade de itens vendidos (1 a 5).
- **preco_unitario**: Preço unitário do item (R$20,00 a R$3.000,00).
- **desconto_percentual**: Percentual de desconto aplicado (0% a 20%).

## Observações
- Os dados foram gerados aleatoriamente utilizando a biblioteca Faker e outras técnicas de simulação.
- O banco de dados foi criado para simular um cenário realista, incluindo:
  - Emails únicos para cada cliente.
  - Referência consistente entre vendas e clientes.
  - Distribuição aleatória de estados e segmentos.
  - Introdução de duplicatas controladas no campo `id_venda` (~5-10%).
- Seguimentos incluem:
  - **varejo**
  - **e-comerce**
  - **atacado**
  - **corporativo**
  - **franquia**
  - **distribuidor**

## Localização do Arquivo
O arquivo do banco de dados está localizado em:
```
data/vendas.db
```

## Uso
Este banco de dados pode ser utilizado para testes de ETL, análises de dados e outras finalidades educacionais ou de desenvolvimento.