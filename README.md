# Teste Técnico Analista de Dados Júnior
Teste Técnico Analista de Dados Júnior para a empresa GFT Promotora. Consistindo basicamente em um Projeto Prático ETL.

Este projeto consiste em um processo ETL (Extração, Transformação e Carga) desenvolvido para simular o fluxo de dados de vendas. Ele utiliza um banco de dados SQLite gerado aleatoriamente, aplica transformações nos dados e os carrega em diferentes formatos, como MongoDB e arquivos PNG.

O objetivo é demonstrar habilidades em manipulação de dados, integração com bancos de dados e geração de relatórios visuais.
## Rquisitos
1. Instalar blibiotecas do [requirements](/requirements.txt).
    - recomendo usar [ambiente de desenvolvimento virtual](#1-criar-o-ambiente-virtual).
2. Possuir uma instância ativa do MongoDB.
    - ⚠️ Caso a instância não seja local, atualize a [string de conexão](src/load/load_to_mongo.py#L114) com as credenciais e o endereço do servidor MongoDB.

## Execuntado o projeto

### 1. Criar o ambiente virtual:

```bash
python3 -m venv venv
```

### 2. Ativar o ambiente virtual:

Linux / macOS
```bash
source venv/bin/activate
```

Windows (PowerShell)
```powershell
venv\Scripts\Activate.ps1
```

### 3. Instalar dependências do requirements.txt

```bash
pip install -r requirements.txt
```

### 4. Executar o ETL

```bash
python src/etl_vendas.py
```
## Análise final
- [Documentação de saída](/output/README.md): Detalhes sobre a saída e uma breve análise delas.
## Documentação Adicional

- [Documentação do Banco de Dados](data/README.md): Detalhes sobre o banco de dados `vendas.db`.
- [Documentação do ETL](src/README.md): Informações sobre o processo ETL e suas etapas.
- [Documentação de Extração](src/extract/README.md): Detalhes sobre a extração de dados.
- [Documentação de Transformação](src/transform/README.md): Informações sobre as transformações aplicadas.
- [Documentação de Carga](src/load/README.md): Detalhes sobre o processo de carga.