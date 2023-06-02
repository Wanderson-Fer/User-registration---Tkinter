from Banco import Banco

import tkinter as tk


class Application:
    def __init__(self, master=None):
        self.font_default = ('Consolas', '12')
        self.font_title = ('Consolas', '14', 'bold')

        self.c_title = tk.Frame(master)
        self.c_title['padx'] = 20  # Espaçamento interno horizontal
        self.c_title['pady'] = 5   # Espaçamento interno vertical
        self.c_title.pack()

        self.label_title = tk.Label(self.c_title)
        self.label_title['text'] = 'Table with Tkinter'
        self.label_title['font'] = self.font_title
        self.label_title['width'] = 25
        self.label_title.pack(side=tk.TOP)

        self.c_button = tk.Frame(master)
        self.c_button['padx'] = 20
        self.c_button['pady'] = 5
        self.c_button.pack()

        self.button_get_table = tk.Button(self.c_button)
        self.button_get_table['text'] = 'Get table'
        self.button_get_table['font'] = self.font_default
        self.button_get_table['width'] = 12
        self.button_get_table['command'] = self.get_table
        self.button_get_table['activebackground'] = 'green'
        self.button_get_table.pack(side=tk.RIGHT)

        self.c_table = tk.Frame(master)
        self.c_table['padx'] = 10
        self.c_table['pady'] = 5
        self.c_table.pack()

    def get_table(self):
        bd = Banco()
        df_users = bd.get_dataframe()
        print('Dados carregados com sucesso!')

        row, col = df_users.shape
        columns = df_users.columns
        header = df_users.keys()

        for i in range(row + 1):
            for j in range(col):
                label_cel = tk.Label(self.c_table)
                if i == 0:
                    label_cel['text'] = header[j]
                    label_cel['font'] = self.font_title
                    label_cel['width'] = 15
                    label_cel['height'] = 2
                else:
                    label_cel['text'] = df_users.loc[i-1, columns[j]]
                    label_cel['font'] = self.font_default
                label_cel.grid(row=i+1, column=j)


if __name__ == '__main__':
    print('Inicializando aplicação')

    root = tk.Tk()
    root.title('Data view')
    Application(root)
    root.mainloop()

    print('Aplicação finalizada!')
