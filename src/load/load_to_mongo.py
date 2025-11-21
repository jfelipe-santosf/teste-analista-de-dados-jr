from pymongo import MongoClient
import pandas as pd

class LoadToMongo:    
    def _connect_to_mongo(self, mongo_uri: str):
        """
        Conecta ao MongoDB usando o URI fornecido.

        Params:
            mongo_uri (str): URI de conexão com o MongoDB

        Return:
            MongoClient: cliente conectado ao MongoDB
        """

        try:
            client = MongoClient(mongo_uri)
            return client
        except Exception as e:
            print(f"Erro ao conectar ao MongoDB: {e}")
            return None
    
    def _disconnect_from_mongo(self, client):
        """
        Desconecta do MongoDB.

        Params:
            client (MongoClient): cliente conectado ao MongoDB
        """

        if client:
            client.close()

    def _connect_to_db(self, client, db_name: str):
        """
        Conecta a um banco de dados específico no MongoDB.

        Params:
            client (MongoClient): cliente conectado ao MongoDB
            db_name (str): nome do banco de dados
            clean_if_exists (bool): se True, limpa o banco se ele já existir

        Return:
            Database: banco de dados conectado
        """

        try:
            db = client[db_name]
            return db
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados '{db_name}': {e}")
            return None

    def _prepare_collection(self, df: pd.DataFrame, embedded_cols: dict = None):
        """
        Converte um DataFrame para documentos prontos para o MongoDB,
        permitindo criar campos embedded.

        Params:
            df (pd.DataFrame): DataFrame de entrada
            embedded_cols (dict): 
                chave = nome do novo campo embedded
                valor = lista de colunas que irão dentro desse campo

                Exemplo:
                {
                    "endereco": ["rua", "cidade", "estado"],
                    "cliente_info": ["nome", "idade"]
                }

        Return:
            List[dict]: lista de documentos prontos para o insert_many
        """

        df_copy = df.copy()

        # Se houver colunas para embed
        if embedded_cols:
            for embed_name, col_list in embedded_cols.items():

                # Cria o campo embedded
                df_copy[embed_name] = df_copy[col_list].apply(
                    lambda row: row.dropna().to_dict(), axis=1
                )

                # Remove as colunas originais que viraram embed
                df_copy.drop(columns=col_list, inplace=True)

        # Transforma o DF em lista de dicionários (formato mongo)
        mongo_docs = df_copy.to_dict(orient="records")

        return mongo_docs
    
    def _insert_documents(self, collection, documents):
        """
        Insere múltiplos documentos em uma coleção do MongoDB.

        Params:
            collection (Collection): coleção do MongoDB
            documents (list): lista de documentos a serem inseridos
        """

        if documents:
            try:
                collection.insert_many(documents)
            except Exception as e:
                print(f"Erro ao inserir documentos: {e}")
        else:
            print("Nenhum documento para inserir.")

    def load_data(self, df: pd.DataFrame, 
                  collection_name: str,
                  db_name: str = 'vendas_db', 
                  mongo_uri: str = 'mongodb://localhost:27017/',
                  embedded_cols: dict = None):

        print("Preparando para carregar dados no MongoDB...")
        client = self._connect_to_mongo(mongo_uri)
        db = self._connect_to_db(client, db_name)
        collection = db[collection_name]
        mongo_docs = self._prepare_collection(df, embedded_cols)

        print(f"Iniciando carregamento de dados para MongoDB na coleção '{collection_name}'...")
        self._insert_documents(collection, mongo_docs)
        print(f"Dados carregados na coleção '{collection_name}' do banco '{db_name}'.")

        self._disconnect_from_mongo(client)