import tkinter as tk
from tkinter import ttk  # Importe o módulo ttk separadamente
import sqlite3

def criar_tabela_produtos():
    conn = sqlite3.connect('banco_cassio.db')
    cursor = conn.cursor()

    # Verificar se a tabela já existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                            id INTEGER PRIMARY KEY,
                            descricao TEXT,
                            preco_venda REAL,
                            preco_compra REAL,
                            quantidade_estoque INTEGER,
                            quantidade_minima INTEGER
                        )''')

    conn.commit()
    conn.close()

def cadastrar_produto():
    # Conectar ao banco de dados
    conn = sqlite3.connect('banco_cassio.db')
    cursor = conn.cursor()

    # Obter valores dos campos
    id = id_entry.get()
    descricao = descricao_entry.get()
    preco_venda = preco_venda_entry.get()
    preco_compra = preco_compra_entry.get()
    quantidade_estoque = quantidade_estoque_entry.get()
    quantidade_minima = quantidade_minima_entry.get()

    # Inserir os dados na tabela
    cursor.execute("INSERT INTO produtos (id, descricao, preco_venda, preco_compra, quantidade_estoque, quantidade_minima) VALUES (?, ?, ?, ?, ?, ?)",
                   (id,descricao, preco_venda, preco_compra, quantidade_estoque, quantidade_minima))

    # Commit e fechar a conexão
    conn.commit()
    conn.close()

    # Limpar os campos após a inserção
    id_entry.delete(0, tk.END)
    descricao_entry.delete(0, tk.END)
    preco_venda_entry.delete(0, tk.END)
    preco_compra_entry.delete(0, tk.END)
    quantidade_estoque_entry.delete(0, tk.END)
    quantidade_minima_entry.delete(0, tk.END)

    # Atualizar a grade de consulta
    listar_produtos()

    # Exibir uma mensagem de confirmação
    mensagem_label.config(text="Produto cadastrado com sucesso!")

def listar_produtos():
    # Conectar ao banco de dados
    conn = sqlite3.connect('banco_cassio.db')
    cursor = conn.cursor()

    # Limpar a grade de consulta
    for row in produtos_tree.get_children():
        produtos_tree.delete(row)

    # Consultar todos os produtos
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    # Preencher a grade de consulta com os produtos
    for produto in produtos:
        produtos_tree.insert("", "end", values=produto)

    # Fechar a conexão
    conn.close()

# Chame a função para criar a tabela no início do programa
criar_tabela_produtos()

# Configurar a janela principal
root = tk.Tk()
root.title("Cadastro de Produtos")

# Criar os campos e rótulos
id_label = tk.Label(root, text="ID:")
id_label.pack()
id_entry = tk.Entry(root)
id_entry.pack()

# Criar os campos e rótulos
descricao_label = tk.Label(root, text="Descrição do Produto:")
descricao_label.pack()
descricao_entry = tk.Entry(root)
descricao_entry.pack()

preco_venda_label = tk.Label(root, text="Preço de Venda:")
preco_venda_label.pack()
preco_venda_entry = tk.Entry(root)
preco_venda_entry.pack()

preco_compra_label = tk.Label(root, text="Preço de Compra:")
preco_compra_label.pack()
preco_compra_entry = tk.Entry(root)
preco_compra_entry.pack()

quantidade_estoque_label = tk.Label(root, text="Quantidade em Estoque:")
quantidade_estoque_label.pack()
quantidade_estoque_entry = tk.Entry(root)
quantidade_estoque_entry.pack()

quantidade_minima_label = tk.Label(root, text="Quantidade Mínima:")
quantidade_minima_label.pack()
quantidade_minima_entry = tk.Entry(root)
quantidade_minima_entry.pack()

# Botão de cadastro
cadastrar_button = tk.Button(root, text="Cadastrar Produto", command=cadastrar_produto)
cadastrar_button.pack()

# Grade de consulta
produtos_tree = tk.ttk.Treeview(root, columns=("ID", "Descrição", "Preço de Venda", "Preço de Compra", "Quantidade em Estoque", "Quantidade Mínima"))
produtos_tree.heading("#1", text="ID")
produtos_tree.heading("#2", text="Descrição")
produtos_tree.heading("#3", text="Preço de Venda")
produtos_tree.heading("#4", text="Preço de Compra")
produtos_tree.heading("#5", text="Quantidade em Estoque")
produtos_tree.heading("#6", text="Quantidade Mínima")
produtos_tree.pack()

# Atualizar a grade de consulta inicialmente
listar_produtos()

# Rótulo de mensagem
mensagem_label = tk.Label(root, text="")
mensagem_label.pack()

root.mainloop()














