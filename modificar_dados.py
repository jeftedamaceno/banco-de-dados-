import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

# ==== UPDATE ====
# Exemplo: alterar o e-mail de um cliente com nome "Lucas"
cursor.execute("""
UPDATE Clientes
SET email = 'lucas.novoemail@example.com'
WHERE id = 6;
""")
print("Email do cliente 'Lucas' atualizado com sucesso.")

# ==== DELETE ====
# Exemplo 1: deletar um item do pedido específico
cursor.execute("""
DELETE FROM ItensPedido
WHERE id = 1;
""")
print("Item de pedido com id 1 removido com sucesso.")

# Exemplo 2: deletar um pedido (lembre: pode ser necessário deletar os itens antes se houver restrição de chave estrangeira)
cursor.execute("""
DELETE FROM Pedidos
WHERE id = 30;
""")
print("Pedido com id 30 removido com sucesso.")

# Confirmar e fechar conexão
conexao.commit()
conexao.close()
