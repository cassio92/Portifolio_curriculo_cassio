import tkinter as tk
from tkinter import ttk
import sqlite3

def criar_tabela_login():
    #Conectar ao banco de dados
    conn = sqlite3.connect('banco_unimodho.db')
    cursor = conn.cursor()


    #Criar a tabela perfil
    cursor.execute('''CREATE TABLE IF NOT EXISTS perfil (
                    id_perfil INTEGER PRIMARY KEY AUTOINCREMENT, 
                    desc_perfil TEXT NOT NULL, 
                    setores_perfil TEXT NOT NULL)
    ''')

    #Executei o comando
    conn.commit()

    #Encerrei o comando
    conn.close()


def cadastro_perfil():
    #Obter os valos dos campos de entrada
    desc_perfil = desc_perfil_var.get()
    setores_perfil = setores_perfil_var.get()

    #Conectar ao banco de dados
    conn = sqlite3.connect('banco_unimodho.db')
    cursor = conn.cursor()


    cursor.execute("INSERT INTO perfil (desc_perfil, setores_perfil) VALUES (?, ?)", (desc_perfil, setores_perfil))

    #Executei o comando
    conn.commit()

    #Encerrei o comando
    conn.close()

    #Limpar os campos após cadastro
    desc_perfil_var.set("")
    setores_perfil_var.set("")

    mensagem_label.config(text='Cadastrado com sucesso')


#CRIAR A TELA

criar_tabela_login()


#Configurar a interface grafica
root = tk.Tk()
root.title("Cadastro de Perfil")


#Determinando os campos da tela
desc_perfil_var = tk.StringVar()
setores_perfil_var = tk.StringVar()

desc_perfil_label = ttk.Label(root, text="Descrição do Perfil: ")
desc_perfil_label.pack()
desc_perfil_entry = ttk.Entry(root, textvariable=desc_perfil_var)
desc_perfil_entry.pack()

setores_perfil_label = ttk.Label(root, text="Setores do Perfil: ")
setores_perfil_label.pack()
setores_perfil_entry = ttk.Entry(root, textvariable=setores_perfil_var)
setores_perfil_entry.pack()


#Criando o botão para cadastrar
cad_perfil_button = ttk.Button(root, text='Cadastrar Perfil', command=cadastro_perfil)
cad_perfil_button.pack()

mensagem_label = ttk.Label(root, foreground="green")
mensagem_label.pack()


root.mainloop()