from CreateTables import engine_fin
from sqlalchemy import create_engine
import pandas as pd


class DatabaseSqlAlchemy:

    def __init__(self, url: str):
        self.url = url
        self.__create_connection()

    def __create_connection(self):
        self.__engine = create_engine(self.url, pool_size=9, echo=False)
        self.__conn = self.__engine.connect()

    def __close_connection(self):
        self.__conn.close()
        self.__engine.dispose()

    def read_sql_table(self, table_name: str, index_col: str = None):

        df = pd.read_sql_table(table_name=table_name, con=self.__conn, index_col=index_col)
        self.__close_connection()
        return df

    def read_sql(self, sql: str):
        df = pd.read_sql(sql=sql, con=self.__conn)
        self.__close_connection()
        return df
