import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

print("=== JOIN entre Pedidos e Clientes ===")
cursor.execute("""
    SELECT Pedidos.id, Pedidos.data_compra, Pedidos.vendedor, Clientes.nome, Clientes.cidade
    FROM Pedidos
    JOIN Clientes ON Pedidos.cliente_id = Clientes.id
    LIMIT 5
""")
for linha in cursor.fetchall():
    print(linha)

print("\n=== JOIN entre ItensPedido, Produtos e Pedidos ===")
cursor.execute("""
    SELECT ItensPedido.id, Produtos.nome, Produtos.categoria, ItensPedido.quantidade, ItensPedido.valor_unitario, Pedidos.data_compra
    FROM ItensPedido
    JOIN Produtos ON ItensPedido.produto_id = Produtos.id
    JOIN Pedidos ON ItensPedido.pedido_id = Pedidos.id
    LIMIT 5
""")
for linha in cursor.fetchall():
    print(linha)

print("\n=== Consulta com WHERE por cliente (exemplo: clientes com nome LIKE 'Ana%') ===")
cursor.execute("""
    SELECT id, nome, email, cidade FROM Clientes
    WHERE nome LIKE 'Ana%'
""")
for linha in cursor.fetchall():
    print(linha)

print("\n=== Consulta com WHERE por data (exemplo: pedidos a partir de 2025-06-01) ===")
cursor.execute("""
    SELECT id, data_compra, vendedor FROM Pedidos
    WHERE data_compra >= '2025-06-01'
    LIMIT 5
""")
for linha in cursor.fetchall():
    print(linha)

print("\n=== Consulta com WHERE por produto (exemplo: produtos na categoria 'Áudio') ===")
cursor.execute("""
    SELECT id, nome, preco FROM Produtos
    WHERE categoria = 'Áudio'
""")
for linha in cursor.fetchall():
    print(linha)

print("Top 5 Clientes:")
cursor.execute("""
    SELECT 
        c.id,
        c.nome,
        SUM(ip.quantidade) AS total_itens_comprados
    FROM Clientes c
    JOIN Pedidos p ON c.id = p.cliente_id
    JOIN ItensPedido ip ON p.id = ip.pedido_id
    GROUP BY c.id, c.nome
    ORDER BY total_itens_comprados DESC
    LIMIT 5;
""")
for row in cursor.fetchall():
    print(row)

print("\nTop 5 Produtos:")
cursor.execute("""
    SELECT 
        pr.id,
        pr.nome,
        SUM(ip.quantidade) AS total_vendido
    FROM Produtos pr
    JOIN ItensPedido ip ON pr.id = ip.produto_id
    GROUP BY pr.id, pr.nome
    ORDER BY total_vendido DESC
    LIMIT 5;
""")
for row in cursor.fetchall():
    print(row)

conexao.close()

