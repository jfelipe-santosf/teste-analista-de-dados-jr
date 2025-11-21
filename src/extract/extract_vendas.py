import sqlite3
import pandas as pd

class ExtractVendas:
    def _connect_db(self):
        db_path = 'data/vendas.db' # conexão simples com sqlite3 ao banco local

        try:
            self.conn = sqlite3.connect(db_path) #declaração da conexão
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise
    
    def _close_db(self):
        if self.conn:
            self.conn.close()

    def _execute_query(self):
        query = open('data/select.sql', 'r').read() # Lê a query SQL do arquivo externo
        try:
        # Executa a consulta e armazena o resultado em um DataFrame
            df = pd.read_sql_query(query, self.conn)
        except Exception as e:
            print(f"Erro ao executar a consulta SQL: {e}")
            raise
        finally:
            self._close_db()

        if df.empty:
            print("Nenhum dado extraído do banco de dados.")
            raise ValueError("DataFrame vazio retornado pela consulta SQL.")
        else:
            print(f"{len(df)} registros extraídos do banco de dados.")
            return df
        

    def extract_data(self):
        ''' Extrai dados de vendas e clientes do banco de dados SQLite e retorna um DataFrame.
        Fonte: Banco de dados SQLite localizado em 'data/vendas.db'.
        Returns:
            pd.DataFrame: DataFrame contendo os dados extraídos.
        '''
        self._connect_db()

        return self._execute_query()