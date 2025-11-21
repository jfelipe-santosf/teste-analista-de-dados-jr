# Código do Processo ETL

Este diretório contém todo o código necessário para executar o processo ETL (Extração, Transformação e Carga) de dados de vendas. O objetivo é demonstrar a manipulação de dados desde a extração de um banco SQLite até a transformação e carregamento em diferentes formatos.

## Arquivo Principal

- [**etl_vendas.py**](/src/etl_vendas.py): Arquivo principal que orquestra todas as etapas do processo ETL.

## Estrutura do Processo ETL

1. **[`E`xtract - Extração](/src/extract/README.md)**: Responsável por extrair os dados do banco SQLite e retorná-los como um DataFrame.
2. **[`T`ransform - Transformação](/src/transform/README.md)**: Aplica limpeza, engenharia de features e agregações nos dados extraídos.
3. **[`L`oad - Carga](/src/load/README.md)**: Carrega os dados transformados para diferentes destinos, como MongoDB ou arquivos PNG.

## Como Executar

1. Certifique-se de que todas as dependências estão instaladas (consulte o [README principal](/README.md)).
2. Execute o arquivo principal:

```bash
python src/etl_vendas.py
```

## Documentação Adicional

- [Documentação do Banco de Dados](/data/README.md): Informações sobre o banco de dados `vendas.db`.
- [Documentação de Extração](/src/extract/README.md): Detalhes sobre a etapa de extração.
- [Documentação de Transformação](/src/transform/README.md): Informações sobre as transformações aplicadas.
- [Documentação de Carga](/src/load/README.md): Detalhes sobre o processo de carga.

