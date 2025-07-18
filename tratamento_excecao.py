import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

# ======= 1. Tratamento de sqlite3.IntegrityError - valor NULL em campo obrigatório =======
try:
    cursor.execute("""
    INSERT INTO Clientes (nome, email, cidade, telefone)
    VALUES (NULL, 'teste@example.com', 'Cidade X', '99999-9999');
    """)
    conexao.commit()
except sqlite3.IntegrityError as e:
    print(f"[ERRO de Integridade] Falha ao inserir cliente: {e}")

# ======= 2. Tratamento de sqlite3.IntegrityError - cliente_id inexistente =======
try:
    cursor.execute("""
    INSERT INTO Pedidos (data_compra, vendedor, cliente_id)
    VALUES ('2025-07-18', 'Vendedor Teste', 999);  -- cliente_id 999 provavelmente não existe
    """)
    conexao.commit()
except sqlite3.IntegrityError:
    print("[ERRO de Integridade] Falha: Cliente não encontrado para registrar a venda.")

# ======= 3. Tratamento de sqlite3.OperationalError - erro de digitação no SQL =======
try:
    cursor.execute("""
    UPDAT Clientes SET cidade = 'Cidade Corrigida' WHERE nome = 'Lucas';
    """)  # 'UPDATE' está escrito errado como 'UPDAT'
except sqlite3.OperationalError as e:
    print(f"[ERRO de Operação] Comando SQL inválido: {e}")

# Fechar conexão
conexao.close()
