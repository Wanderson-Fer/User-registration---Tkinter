from sqlite3 import connect
import pandas as pd

class Banco:
    def __init__(self):
        self.conn = connect('database/banco.db')
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()

        cursor.execute(
            """
                create table if not exists usuarios (
                    id integer primary key autoincrement,
                    nome text,
                    telefone text,
                    email text,
                    usuario text,
                    senha text
                )
            """
        )

        self.conn.commit()
        cursor.close()

    def get_dataframe(self):
        return pd.read_sql('SELECT * FROM usuarios', self.conn, dtype=str)
