# Etapa de carregamento (`L`oad) de dados
Aqui o DF é tratado e carregado para uma instância do mongo.

## [Load to MongoDB](/src/load/load_to_mongo.py)
- **_prepare_collection**: Recebe DataFrame e converte em um documento pronto para ser inserido no MonogoDB.
- **_insert_documents**: Insere os dados no MongoDB utilizando *insert_many* para inserir um documento inteiro (vários documentos em uma coleção).

### Executar
Para carregar basta chamar o método `load_data`e passar os parámentros:
1. **df**: Dataframe a ser carregado.
2. **collection_name**: Nome da coleção onde os documentos serão inseridos.
3. **db_name**: Nome do banco de dados na instância. `Padrão: "vendas_db"`.
4. **mongo_uri**: Link de conexão ao MongoDB. `Padrão: conexão local`.
5. **embedded_docs**: Colunas a serem desnormalizadas. `Padrão: none`.
    - Exemplo:
    ```py
    {"chave": ["valor1", "valor2", "valorN"],
    "chave": ["valorN"]}
    ```
    - chave = nome do novo campo embedded
    - valor = lista de colunas que irão dentro desse campo

## [Save PNG](/src/load/save_df_png.py)
Salva imagem de resultados de um DF.
- **save_df_png**: Recebe um DF e o nome do arquivo. Exemplo:
    ```py
    SaveDFPNG.save_png(df[:10], "vendas") #salva um png das 10 primeiras linhas de um df e salva como vendas.png
    ```
- **save_graph**: Recebe alguns parâmetros:
    1. **df**: DataFrame contendo os dados.
    2. **x_col**: Nome da coluna para o eixo X.
    3. **y_col**: nome da coluna para o eixo Y.
    4. **graph_name**: Nome do arquivo PNG.

### Saída
A saída é padrão em [output](/output/)

## Justificativa para o Modelo Embedded no MongoDB

O modelo de dados embedded foi escolhido para o MongoDB devido às seguintes razões:

1. **Desempenho em Consultas**:
   - Dados relacionados, como informações de clientes e vendas, são armazenados juntos, reduzindo a necessidade de operações de `JOIN`.
   - Consultas que acessam dados relacionados podem ser realizadas de forma mais eficiente, pois todos os dados necessários estão em um único documento.

2. **Simplicidade de Modelagem**:
   - O modelo embedded reflete a estrutura hierárquica dos dados, tornando o esquema mais intuitivo e fácil de entender.
   - Ideal para cenários onde os dados relacionados têm uma relação "um para muitos" e o volume de subdocumentos é limitado.

3. **Redução de Latência**:
   - Como os dados estão armazenados juntos, há menos chamadas ao banco de dados, reduzindo a latência em operações de leitura.

4. **Cenário de Uso**:
   - No contexto deste projeto, as vendas estão diretamente associadas a clientes, e é improvável que os subdocumentos (vendas) cresçam de forma ilimitada. Isso torna o modelo embedded uma escolha prática e eficiente.

> Embora o modelo embedded seja adequado para este projeto, é importante avaliar cuidadosamente o volume de dados e os padrões de acesso em cenários reais para garantir que o desempenho e a escalabilidade não sejam comprometidos.