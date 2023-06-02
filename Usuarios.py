from Banco import Banco

class Usuarios(object):
    def __init__(self, id=0, nome='', telefone='', email='', usuario='', senha=''):
        self.info = {}
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insert_user(self):
        banco = Banco()

        try:
            cursor = banco.conn.cursor()

            cursor.execute(
                f"""
                    INSERT INTO usuarios (nome, telefone, email, usuario, senha)
                    VALUES (
                        '{self.nome}', 
                        '{self.telefone}', 
                        '{self.email}',
                        '{self.usuario}',
                        '{self.senha}'
                    )
                """
            )

            banco.conn.commit()
            cursor.close()

            return "Usuário cadastrado com sucesso!"

        except Exception as e:
            return f"Ocorreu um erro na inserção do usuário \n{e}"

    def update_user(self):
        banco = Banco()

        try:
            cursor = banco.conn.cursor()

            cursor.execute(
                f"""
                    UPDATE usuarios SET 
                    nome = '{self.nome}', 
                    telefone = '{self.telefone}',
                    email = '{self.email}',
                    usuario = '{self.usuario}',
                    senha = '{self.senha}'
                    WHERE id = {self.id}
                """
            )
            banco.conn.commit()
            cursor.close()

            return "Usuário atulizado com sucesso"
        except Exception as e:
            return f"Ocorreu um erro na alteração do usuário \n{e}"

    def delete_user(self):
        banco = Banco()

        try:
            cursor = banco.conn.cursor()

            cursor.execute(
                f"""
                    DELETE FROM usuarios
                    WHERE id = {self.id}
                """
            )

            banco.conn.commit()
            cursor.close()

            return "Usuário excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do usuário \n{e}"

    def select_user(self, id):
        banco = Banco()

        try:
            cursor = banco.conn.cursor()

            cursor.execute(
                f"""
                    SELECT * FROM usuarios
                    WHERE id = {id}
                """
            )

            for user in cursor:
                self.id = user[0]
                self.nome = user[1]
                self.telefone = user[2]
                self.email = user[3]
                self.usuario = user[4]
                self.senha = user[5]

            cursor.close()

            return "Busca feita com sucesso!"

        except Exception as e:
            return f"Ocorreu um erro na busca do usuário \n{e}"
