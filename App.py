from Usuarios import Usuarios
import tkinter as tk

class Application:
    def __init__(self, master=None):
        self.fonte_default = ('Verdana', '10')
        self.fonte_title = ('Calibri', '12', 'bold')

        # Container 1
        self.c_titulo = tk.Frame(master)
        self.c_titulo['pady'] = 10  # padding vertical
        self.c_titulo.pack()

        # Widget 1.1
        self.titulo = tk.Label(self.c_titulo)
        self.titulo['text'] = 'Informe os dados: '
        self.titulo['font'] = self.fonte_title
        self.titulo.pack()

        # Container 2
        self.c_id = tk.Frame(master)
        self.c_id['padx'] = 20  # padding horizontal
        self.c_id['pady'] = 5  # padding vertical
        self.c_id.pack()

        # Widget 2.1
        self.label_id = tk.Label(self.c_id)
        self.label_id['text'] = 'Código: '
        self.label_id['font'] = self.fonte_default
        self.label_id['width'] = 10
        self.label_id.pack(side=tk.LEFT)

        # Widget 2.2
        self.entry_id = tk.Entry(self.c_id)
        self.entry_id['font'] = self.fonte_default
        self.entry_id['width'] = 14
        self.entry_id.pack(side=tk.LEFT)

        # Widget 2.3
        self.button_search = tk.Button(self.c_id)
        self.button_search['text'] = 'Buscar'
        self.button_search['font'] = self.fonte_default
        self.button_search['width'] = 10
        self.button_search['command'] = self.buscar_usuario
        self.button_search.pack(side=tk.RIGHT)

        # Container 3
        self.c_nome = tk.Frame(master)
        self.c_nome['padx'] = 20
        self.c_nome['pady'] = 5
        self.c_nome.pack()

        # Widget 3.1
        self.label_nome = tk.Label(self.c_nome)
        self.label_nome['text'] = 'Nome: '
        self.label_nome['font'] = self.fonte_default
        self.label_nome['width'] = 10
        self.label_nome.pack(side=tk.LEFT)

        # Widget 3.2
        self.entry_nome = tk.Entry(self.c_nome)
        self.entry_nome['font'] = self.fonte_default
        self.entry_nome['width'] = 25
        self.entry_nome.pack(side=tk.LEFT)

        # Container 4
        self.c_telefone = tk.Frame(master)
        self.c_telefone['padx'] = 20
        self.c_telefone['pady'] = 5
        self.c_telefone.pack()

        # Widget 4.1
        self.label_telefone = tk.Label(self.c_telefone)
        self.label_telefone['text'] = 'Telefone: '
        self.label_telefone['font'] = self.fonte_default
        self.label_telefone['width'] = 10
        self.label_telefone.pack(side=tk.LEFT)

        # Widget 4.2
        self.entry_telefone = tk.Entry(self.c_telefone)
        self.entry_telefone['font'] = self.fonte_default
        self.entry_telefone['width'] = 25
        self.entry_telefone.pack(side=tk.LEFT)

        # Container 5
        self.c_email = tk.Frame(master)
        self.c_email['padx'] = 20
        self.c_email['pady'] = 5
        self.c_email.pack()

        # Widget 5.1
        self.label_email = tk.Label(self.c_email)
        self.label_email['text'] = 'E-mail: '
        self.label_email['font'] = self.fonte_default
        self.label_email['width'] = 10
        self.label_email.pack(side=tk.LEFT)

        # Widget 5.2
        self.entry_email = tk.Entry(self.c_email)
        self.entry_email['font'] = self.fonte_default
        self.entry_email['width'] = 25
        self.entry_email.pack(side=tk.LEFT)

        # Container 6
        self.c_usuario = tk.Frame(master)
        self.c_usuario['padx'] = 20
        self.c_usuario['pady'] = 5
        self.c_usuario.pack()

        # Widget 6.1
        self.label_usuario = tk.Label(self.c_usuario)
        self.label_usuario['text'] = 'Usuário: '
        self.label_usuario['font'] = self.fonte_default
        self.label_usuario['width'] = 10
        self.label_usuario.pack(side=tk.LEFT)

        # Widget 6.2
        self.entry_usuario = tk.Entry(self.c_usuario)
        self.entry_usuario['font'] = self.fonte_default
        self.entry_usuario['width'] = 25
        self.entry_usuario.pack(side=tk.LEFT)

        # Container 7
        self.c_senha = tk.Frame(master)
        self.c_senha['padx'] = 20
        self.c_senha['pady'] = 5
        self.c_senha.pack()

        # Widget 7.1
        self.label_senha = tk.Label(self.c_senha)
        self.label_senha['text'] = 'Senha: '
        self.label_senha['font'] = self.fonte_default
        self.label_senha['width'] = 10
        self.label_senha.pack(side=tk.LEFT)

        # Widget 7.2
        self.entry_senha = tk.Entry(self.c_senha)
        self.entry_senha['font'] = self.fonte_default
        self.entry_senha['show'] = '*'
        self.entry_senha['width'] = 25
        self.entry_senha.pack(side=tk.LEFT)

        # Container 8
        self.c_buttons = tk.Frame(master)
        self.c_buttons['padx'] = 20
        self.c_buttons['pady'] = 10
        self.c_buttons.pack()

        # Widget 8.1
        self.button_insert = tk.Button(self.c_buttons)
        self.button_insert['text'] = 'Inserir'
        self.button_insert['font'] = self.fonte_default
        self.button_insert['width'] = 12
        self.button_insert['command'] = self.inserir_usuario
        self.button_insert.pack(side=tk.LEFT)

        # Widget 8.2
        self.button_update = tk.Button(self.c_buttons)
        self.button_update['text'] = 'Alterar'
        self.button_update['font'] = self.fonte_default
        self.button_update['width'] = 12
        self.button_update['command'] = self.alterar_usuario
        self.button_update.pack(side=tk.LEFT)

        # Widget 8.3
        self.button_delete = tk.Button(self.c_buttons)
        self.button_delete['text'] = 'Excluir'
        self.button_delete['font'] = self.fonte_default
        self.button_delete['width'] = 12
        self.button_delete['command'] = self.excluir_usuario
        self.button_delete.pack(side=tk.LEFT)

        # Container 9
        self.c_msg = tk.Frame(master)
        self.c_msg['pady'] = 15
        self.c_msg.pack()

        # Widget 9.1
        self.label_msg = tk.Label(self.c_msg)
        self.label_msg['text'] = ''
        self.label_msg['font'] = ('Verdana', '10', 'italic')
        self.label_msg.pack()

    def buscar_usuario(self):
        user = Usuarios()

        search_id = self.entry_id.get()

        self.label_msg['text'] = user.select_user(search_id)

        self.clean_entrys()

        self.entry_id.insert(tk.INSERT, user.id)
        self.entry_nome.insert(tk.INSERT, user.nome)
        self.entry_telefone.insert(tk.INSERT, user.telefone)
        self.entry_email.insert(tk.INSERT, user.email)
        self.entry_usuario.insert(tk.INSERT, user.usuario)
        self.entry_usuario.insert(tk.INSERT, user.senha)

    def inserir_usuario(self):
        user = Usuarios()

        user.nome = self.entry_nome.get()
        user.telefone = self.entry_telefone.get()
        user.email = self.entry_email.get()
        user.usuario = self.entry_usuario.get()
        user.senha = self.entry_senha.get()

        self.label_msg['text'] = user.insert_user()

        self.clean_entrys()

    def alterar_usuario(self):
        user = Usuarios()

        user.id = self.entry_id.get()
        user.nome = self.entry_nome.get()
        user.telefone = self.entry_telefone.get()
        user.email = self.entry_email.get()
        user.usuario = self.entry_usuario.get()
        user.senha = self.entry_senha.get()

        self.label_msg['text'] = user.update_user()

        self.clean_entrys()

    def excluir_usuario(self):
        user = Usuarios()

        user.id = self.entry_id.get()

        self.label_msg['text'] = user.delete_user()

        self.clean_entrys()

    def clean_entrys(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nome.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_usuario.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('User form')
    Application(root)
    root.mainloop()
