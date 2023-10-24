import tkinter as tk
from tkinter import ttk
import sqlite3

def criar_tabela_usuario():
    # Conectar ao banco de dados e inserir o novo usuário
    conn = sqlite3.connect('banco_unimodho.db')
    cursor = conn.cursor()

    #AUTOINCREMENT - insere o valor sequncialmente de forma automatica
    # NOT NULL - Campo não pode ser vazio

    #Criar a tabela usuario
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    usuario TEXT NOT NULL, 
                    senha TEXT NOT NULL, 
                    perfil INTERGER NOT NULL)
    ''')

    conn.commit()
    conn.close()


def cadastrar_usuario():
    # Obter os valores dos campos de entrada
    usuario = usuario_var.get()
    senha = senha_var.get()
    perfil = perfil_var.get()

    # Conectar ao banco de dados e inserir o novo usuário
    conn = sqlite3.connect('banco_unimodho.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO usuarios (usuario, senha, perfil) VALUES (?, ?, ?)", (usuario, senha, perfil))
    conn.commit()
    conn.close()

    # Limpar os campos após o cadastro
    usuario_var.set("")
    senha_var.set("")
    perfil_var.set(1)

def login():
    # Obter os valores dos campos de entrada
    usuario = usuario_login_var.get()
    senha = senha_login_var.get()

    # Conectar ao banco de dados e verificar as credenciais
    conn = sqlite3.connect('banco_unimodho.db')
    cursor = conn.cursor()

    cursor.execute("SELECT perfil FROM usuarios WHERE usuario=? AND senha=?", (usuario, senha))
    perfil = cursor.fetchone()

    conn.close()

    if perfil:
        perfil = perfil[0]
        if perfil == 1:
            # Direcionar para a tela de vendas (ou a lógica desejada)
            abrir_tela_de_vendas()
        elif perfil == 2:
            # Direcionar para o menu de acesso às telas de cadastro
            abrir_menu_de_acesso()
    else:
        # Exibir uma mensagem de erro de login inválido
        erro_login_label.config(text="Usuário ou senha inválidos")

def abrir_tela_de_vendas():
    # Implemente a lógica para abrir a tela de vendas aqui
    import trab_tela_vendas
    trab_tela_vendas()
    pass

def abrir_menu_de_acesso():
    import tkinter as tk
    from tkinter import ttk
    import sqlite3

    # Função para abrir a tela de cadastro de produtos
    def abrir_cadastro_produtos():
        # Implemente a lógica para abrir a tela de cadastro de produtos aqui
        #import prj_cadastro_de_prod
        #prj_cadastro_de_prod()
        pass

    # Função para abrir a tela de consulta de produtos
    def abrir_consulta_produtos():
        # Implemente a lógica para abrir a tela de consulta de produtos aqui
        import prj_tela_consulta
        prj_tela_consulta()
        pass

    # Função para abrir a tela de vendas
    def abrir_tela_vendas():
        # Implemente a lógica para abrir a tela de vendas aqui
        import prj_tela_de_vendas
        prj_tela_de_vendas()
        pass

    # Configurar a janela principal
    root = tk.Tk()
    root.title("Menu Principal")

    # Botões interativos no menu
    cadastro_usuario_button = ttk.Button(root, text="Cadastro de Usuarios", command=cadastrar_usuario)
    cadastro_usuario_button.pack()

    cadastro_produtos_button = ttk.Button(root, text="Cadastro de Produtos", command=abrir_cadastro_produtos)
    cadastro_produtos_button.pack()

    #consulta_produtos_button = ttk.Button(root, text="Consulta de Produtos", command=abrir_consulta_produtos)
    #consulta_produtos_button.pack()

    tela_vendas_button = ttk.Button(root, text="Ir para PDV", command=abrir_tela_vendas)
    tela_vendas_button.pack()

    root.mainloop()
    pass


#Chamar a função de criar a tabela usuari
criar_tabela_usuario()

# Configurar a janela principal
root = tk.Tk()
root.title("Cadastro de Usuários")

# Campos de entrada para cadastrar usuário
usuario_var = tk.StringVar()
senha_var = tk.StringVar()
perfil_var = tk.IntVar()
perfil_var.set(1)  # Perfil padrão

usuario_label = ttk.Label(root, text="Usuário:")
usuario_label.pack()
usuario_entry = ttk.Entry(root, textvariable=usuario_var)
usuario_entry.pack()

senha_label = ttk.Label(root, text="Senha:")
senha_label.pack()
senha_entry = ttk.Entry(root, textvariable=senha_var, show="*")
senha_entry.pack()

perfil_label = ttk.Label(root, text="Perfil:")
perfil_label.pack()
perfil_combobox = ttk.Combobox(root, textvariable=perfil_var, values=[1, 2])
perfil_combobox.pack()

cadastrar_button = ttk.Button(root, text="Cadastrar Usuário", command=cadastrar_usuario)
cadastrar_button.pack()

# Campos de entrada para login
usuario_login_var = tk.StringVar()
senha_login_var = tk.StringVar()

usuario_login_label = ttk.Label(root, text="Usuário:")
usuario_login_label.pack()
usuario_login_entry = ttk.Entry(root, textvariable=usuario_login_var)
usuario_login_entry.pack()

senha_login_label = ttk.Label(root, text="Senha:")
senha_login_label.pack()
senha_login_entry = ttk.Entry(root, textvariable=senha_login_var, show="*")
senha_login_entry.pack()

login_button = ttk.Button(root, text="Login", command=login)
login_button.pack()

erro_login_label = ttk.Label(root, text="", foreground="red")
erro_login_label.pack()

root.mainloop()