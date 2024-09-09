import pandas as pd
import psycopg2

def ler_salvar(solana_csv, solananew):
    df = pd.read_csv(solana_csv)

    df.to_csv(solananew, sep=';', index=False )

    print(f'O arquivo foi salvo em {solananew}. ')
    print(df.head())

class Config:
    def __init__(self, host, dbname, user, password, port="5432"):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password

class Connection:
    def __init__(self, config):
        self.config = config
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host = self.config.host,
                dbname = self.config.dbname,
                user = self.config.user,
                password = self.config.password,
        )
            print("The database connection was successful")
        except psycopg2.Error as e:
            print(f"Error to connect to the database: {e}")
            self.conn = None

    def query(self, sql_query, params=None):
        if self.conn is None:
            print("The connection failed.")
            return None
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_query, params)
            results = cursor.fetchall()
            return results
        except psycopg2.Error as e:
            print(f"Error to execute a query: {e}")
            return None

    def close(self):
        if self.conn:
            self.conn.close()
            print("Close Connection")

if __name__ == "__main__":
    config = Config(
        host="localhost",
        dbname="dbsolana",
        user="postgres",
        password="010622",
        port="5432"
    )

    connection = Connection(config)
    connection.connect()

    query_results = connection.query("SELECT Open FROM information.schema.tables WHERE table_schema = 'public';")

    if query_results:
        print("tables in dbsolana: ")
        for table in query_results:
            print(table[1])

    solana_csv = 'C:/Users/Nicolas/Desktop/Projeto Crypto/data/solana.csv'
    solananew = 'data/solananew.csv'

    ler_salvar(solana_csv, solananew)

    connection.close()






