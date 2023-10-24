import tkinter as tk
from tkinter import ttk
import sqlite3

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

def atualizar_estoque():
    # Conectar ao banco de dados
    conn = sqlite3.connect('banco_cassio.db')
    cursor = conn.cursor()

    # Atualizar o estoque dos produtos em tempo real
    for item in venda_items:
        produto_id = item['id']
        quantidade_vendida = item['quantidade']

        cursor.execute("SELECT quantidade_estoque FROM produtos WHERE id=?", (produto_id,))
        estoque_atual = cursor.fetchone()[0]
        novo_estoque = estoque_atual - quantidade_vendida

        cursor.execute("UPDATE produtos SET quantidade_estoque=? WHERE id=?", (novo_estoque, produto_id))

    conn.commit()
    conn.close()

    # Atualizar a grade de consulta após a atualização do estoque
    listar_produtos()


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

def calcular_total(event):
    # Obter o item selecionado na grade de consulta de produtos
    item = produtos_tree.selection()[0]
    values = produtos_tree.item(item, "values")

    try:
        # Obter a quantidade inserida pelo usuário
        quantidade = int(quantidade_var.get())

        # Calcular o total
        preco_venda = float(values[2])
        total = preco_venda * quantidade

        # Atualizar o rótulo do total
        total_var.set(f"Total: R$ {total:.2f}")
    except ValueError:
        total_var.set("Total: R$ 0.00")

def adicionar_item():
    # Obter o item selecionado na grade de consulta de produtos
    item = produtos_tree.selection()[0]
    values = produtos_tree.item(item, "values")

    try:
        # Obter a quantidade inserida pelo usuário
        quantidade = int(quantidade_var.get())

        if quantidade <= 0:
            return

        # Calcular o total
        preco_venda = float(values[2])
        total = preco_venda * quantidade

        # Adicionar o item à lista de itens vendidos
        venda_items.append({
            'id': values[0],
            'descricao': values[1],
            'quantidade': quantidade,
            'total': total
        })

        # Atualizar a grade de itens vendidos
        itens_vendidos_tree.insert("", "end", values=(values[1], quantidade, f"R$ {total:.2f}"))

        # Limpar os campos de quantidade e total
        quantidade_var.set("")
        total_var.set("Total: R$ 0.00")
    except ValueError:
        pass

def finalizar_venda():
    # Obter a forma de pagamento selecionada
    forma_pagamento = forma_pagamento_var.get()

    # Atualizar o estoque dos produtos vendidos
    for item in venda_items:
        produto_id = item['id']
        quantidade_vendida = item['quantidade']

        # Conectar ao banco de dados e atualizar o estoque
        conn = sqlite3.connect('banco_cassio.db')
        cursor = conn.cursor()

        cursor.execute("SELECT quantidade_estoque FROM produtos WHERE id=?", (produto_id,))
        estoque_atual = cursor.fetchone()[0]
        novo_estoque = estoque_atual - quantidade_vendida

        cursor.execute("UPDATE produtos SET quantidade_estoque=? WHERE id=?", (novo_estoque, produto_id))

        conn.commit()
        conn.close()

    # Imprimir o cupom (neste exemplo, apenas exibimos no console)
    print("Cupom de Venda")
    print("--------------")
    for item in venda_items:
        print(f"Produto: {item['descricao']}")
        print(f"Quantidade: {item['quantidade']}")
        print(f"Total: R$ {item['total']:.2f}")
    print(f"Forma de Pagamento: {forma_pagamento}")
    print("--------------")

    # Limpar a lista de itens vendidos
    venda_items.clear()

    # Limpar a grade de itens vendidos
    itens_vendidos_tree.delete(*itens_vendidos_tree.get_children())

# Configurar a janela principal
root = tk.Tk()
root.title("Sistema de Vendas")

# Criar uma grade de consulta de produtos (a mesma usada anteriormente)
produtos_tree = ttk.Treeview(root, columns=("ID", "Descrição", "Preço de Venda", "Preço de Compra", "Quantidade em Estoque", "Quantidade Mínima"))
produtos_tree.heading("#1", text="ID")
produtos_tree.heading("#2", text="Descrição")
produtos_tree.heading("#3", text="Preço de Venda")
produtos_tree.heading("#4", text="Preço de Compra")
produtos_tree.heading("#5", text="Quantidade em Estoque")
produtos_tree.heading("#6", text="Quantidade Mínima")
produtos_tree.pack()

# Atualizar a grade de consulta inicialmente
listar_produtos()

# Campos de entrada
quantidade_var = tk.StringVar()
quantidade_label = ttk.Label(root, text="Quantidade:")
quantidade_label.pack()
quantidade_entry = ttk.Entry(root, textvariable=quantidade_var)
quantidade_entry.pack()

total_var = tk.StringVar()
total_label = ttk.Label(root, textvariable=total_var)
total_label.pack()

# Lista de itens vendidos
venda_items = []

# Forma de pagamento
forma_pagamento_var = tk.StringVar()
forma_pagamento_label = ttk.Label(root, text="Forma de Pagamento:")
forma_pagamento_label.pack()

# Opções de forma de pagamento
forma_pagamento_combo = ttk.Combobox(root, textvariable=forma_pagamento_var, values=["Dinheiro", "Cartão de Crédito", "Cartão de Débito", "PIX"])
forma_pagamento_combo.pack()

# Botão para calcular o total
calcular_button = ttk.Button(root, text="Calcular Total", command=lambda: calcular_total(None))
calcular_button.pack()

# Botão para adicionar item à venda
adicionar_button = ttk.Button(root, text="Adicionar Item", command=adicionar_item)
adicionar_button.pack()

# Botão para finalizar a venda
finalizar_button = ttk.Button(root, text="Finalizar Venda", command=finalizar_venda)
finalizar_button.pack()

# Botão para atualizar o estoque
atualizar_estoque_button = ttk.Button(root, text="Atualizar", command=atualizar_estoque)
atualizar_estoque_button.pack()

# Configurar evento de seleção na grade de consulta de produtos
produtos_tree.bind("<<TreeviewSelect>>", calcular_total)

# Grade de itens vendidos
itens_vendidos_tree = ttk.Treeview(root, columns=("Descrição", "Quantidade", "Total"))
itens_vendidos_tree.heading("#1", text="Descrição")
itens_vendidos_tree.heading("#2", text="Quantidade")
itens_vendidos_tree.heading("#3", text="Total")
itens_vendidos_tree.pack()

root.mainloop()

#Cassio alterou o codigo.
