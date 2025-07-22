import sqlite3

# Função para inserir um novo cliente
def criar_cliente():
    try:
        nome = input("Nome do cliente: ")
        email = input("Email: ")
        cidade = input("Cidade: ")
        telefone = input("Telefone: ")

        cursor.execute("""
        INSERT INTO Clientes (nome, email, cidade, telefone)
        VALUES (?, ?, ?, ?)
        """, (nome, email, cidade, telefone))

        conexao.commit()
        print("[SUCESSO] Cliente cadastrado com sucesso!")

    except sqlite3.IntegrityError as e:
        print(f"[ERRO de Integridade] Falha ao inserir cliente: {e}")

# Função para editar um cliente existente
def editar_cliente():
    try:
        cliente_id = int(input("ID do cliente a ser editado: "))
        novo_nome = input("Novo nome: ")
        novo_email = input("Novo email: ")
        novo_telefone = input("Novo telefone: ")

        cursor.execute("""
        UPDATE Clientes SET nome = ?, email = ?, telefone = ? WHERE id = ?
        """, (novo_nome, novo_email, novo_telefone, cliente_id))

        if cursor.rowcount == 0:
            print("[ERRO] Cliente não encontrado.")
        else:
            conexao.commit()
            print("[SUCESSO] Cliente atualizado com sucesso!")

    except sqlite3.IntegrityError as e:
        print(f"[ERRO de Integridade] Falha ao atualizar cliente: {e}")
    except ValueError:
        print("[ERRO] ID do cliente deve ser um número inteiro.")

# Função para inserir um novo produto
def criar_produto():
    try:
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        categoria = input("Categoria: ")

        cursor.execute("""
        INSERT INTO Produtos (nome, preco, categoria)
        VALUES (?, ?, ?)
        """, (nome, preco, categoria))

        conexao.commit()
        print("[SUCESSO] Produto cadastrado com sucesso!")

    except sqlite3.IntegrityError as e:
        print(f"[ERRO de Integridade] Falha ao inserir produto: {e}")
    except ValueError:
        print("[ERRO] Preço deve ser um número.")

# Função para deletar um produto
def deletar_produto():
    try:
        produto_id = int(input("ID do produto a ser deletado: "))

        cursor.execute("DELETE FROM Produtos WHERE id = ?", (produto_id,))

        if cursor.rowcount == 0:
            print("[ERRO] Produto não encontrado.")
        else:
            conexao.commit()
            print("[SUCESSO] Produto deletado com sucesso!")

    except ValueError:
        print("[ERRO] ID do produto deve ser um número inteiro.")

# Função para criar um pedido (associado a um cliente existente)
def criar_pedido():
    try:
        data_compra = input("Data da compra (YYYY-MM-DD): ")
        vendedor = input("Nome do vendedor: ")
        cliente_id = int(input("ID do cliente: "))

        cursor.execute("""
        INSERT INTO Pedidos (data_compra, vendedor, cliente_id)
        VALUES (?, ?, ?)
        """, (data_compra, vendedor, cliente_id))

        conexao.commit()
        print("[SUCESSO] Pedido criado com sucesso!")

    except sqlite3.IntegrityError:
        print("[ERRO de Integridade] Cliente não encontrado para registrar o pedido.")
    except ValueError:
        print("[ERRO] ID do cliente deve ser um número inteiro.")

# Conectar ao banco de dados
conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

# Menu principal
while True:
    print("\n===== MENU =====")
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Produto")
    print("3. Criar Pedido")
    print("4. Editar Cliente")
    print("5. Deletar Produto")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_cliente()
    elif opcao == "2":
        criar_produto()
    elif opcao == "3":
        criar_pedido()
    elif opcao == "4":
        editar_cliente()
    elif opcao == "5":
        deletar_produto()
    elif opcao == "6":
        break
    else:
        print("[ERRO] Opção inválida. Tente novamente.")

# Fechar conexão
conexao.close()
