import sqlite3

# Criar ou conectar ao banco de dados
conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

# Criar tabela Clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT,
    cidade TEXT,
    telefone TEXT
);
""")

# Criar tabela Produtos
cursor.execute("""
CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    categoria TEXT
);
""")

# Criar tabela Pedidos
cursor.execute("""
CREATE TABLE IF NOT EXISTS Pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_compra TEXT NOT NULL,
    vendedor TEXT NOT NULL,
    cliente_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
);
""")

# Criar tabela ItensPedido (tabela de junção entre Pedidos e Produtos)
cursor.execute("""
CREATE TABLE IF NOT EXISTS ItensPedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER,
    valor_unitario REAL,
    FOREIGN KEY (pedido_id) REFERENCES Pedidos(id),
    FOREIGN KEY (produto_id) REFERENCES Produtos(id)
);
""")

# Confirmar e fechar a conexão
conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso.")
