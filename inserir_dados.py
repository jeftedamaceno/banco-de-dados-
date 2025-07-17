import sqlite3
from random import randint, choice
from datetime import datetime, timedelta
# Criar ou conectar ao banco de dados
conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()
produtos = [
    ("Notebook Dell Inspiron", 3500.00, "Informática"),
    ("Smartphone Samsung Galaxy S21", 4200.00, "Telefonia"),
    ("Monitor LG 24''", 899.90, "Informática"),
    ("Impressora HP Deskjet", 499.00, "Periféricos"),
    ("Teclado Mecânico Redragon", 250.00, "Periféricos"),
    ("Mouse Logitech M170", 69.90, "Periféricos"),
    ("Cadeira Gamer DT3", 1199.00, "Móveis"),
    ("HD Externo 1TB Seagate", 320.00, "Armazenamento"),
    ("SSD Kingston 480GB", 299.00, "Armazenamento"),
    ("Tablet Samsung Galaxy Tab A8", 1100.00, "Telefonia"),
    ("Roteador TP-Link Archer", 189.00, "Redes"),
    ("Webcam Logitech C920", 499.00, "Periféricos"),
    ("Caixa de Som JBL Go 3", 229.00, "Áudio"),
    ("Headset HyperX Cloud Stinger", 349.00, "Áudio"),
    ("TV LG 50'' 4K", 2599.00, "Eletrônicos"),
    ("Controle Xbox Series", 499.00, "Games"),
    ("Console PlayStation 5", 4499.00, "Games"),
    ("Placa de Vídeo RTX 3060", 2499.00, "Hardware"),
    ("Processador Ryzen 5 5600X", 1199.00, "Hardware"),
    ("Memória RAM 16GB DDR4", 399.00, "Hardware"),
    ("Fonte Corsair 650W", 459.00, "Hardware"),
    ("Gabinete Gamer RGB", 359.00, "Hardware"),
    ("Kindle 11ª Geração", 499.00, "Leitura"),
    ("Aspirador Robô WAP", 899.00, "Eletrodomésticos"),
    ("Fone Bluetooth Xiaomi", 199.90, "Áudio"),
    ("Carregador Turbo Motorola", 99.00, "Acessórios"),
    ("Pendrive 64GB Sandisk", 45.00, "Armazenamento"),
    ("Cabo USB-C 1m", 29.90, "Acessórios"),
    ("Suporte Celular Veicular", 35.00, "Acessórios"),
    ("Smartwatch Amazfit Bip U", 379.00, "Wearables"),
]

clientes = [
    ("Ana Paula Souza", "ana.souza@gmail.com", "São Paulo", "(11)91234-5678"),
    ("Carlos Henrique Lima", "carloshl@gmail.com", "Rio de Janeiro", "(21)99876-5432"),
    ("Fernanda Oliveira", "fernanda.oli@yahoo.com", "Belo Horizonte", "(31)98321-1234"),
    ("João Pedro Silva", "joaopedro@outlook.com", "Curitiba", "(41)99811-2233"),
    ("Mariana Castro", "maricast@gmail.com", "Fortaleza", "(85)99123-3344"),
    ("Lucas Ribeiro", "lucas.ribeiro@hotmail.com", "Brasília", "(61)98776-1122"),
    ("Juliana Mendes", "julimendes@live.com", "Salvador", "(71)99234-7788"),
    ("André Luiz Rocha", "andreluizr@gmail.com", "Recife", "(81)98122-6655"),
    ("Patrícia Martins", "patymartins@terra.com", "Manaus", "(92)99321-5544"),
    ("Vinícius Almeida", "vinialm@globo.com", "Porto Alegre", "(51)99887-7788"),
    ("Rafael Gonçalves", "rafa.goncalves@gmail.com", "Goiânia", "(62)99811-3344"),
    ("Camila Brito", "camilabrito@uol.com", "São Luís", "(98)98765-4411"),
    ("Rodrigo Nunes", "rodrinunes@gmail.com", "Natal", "(84)98877-9911"),
    ("Laura Teixeira", "laura.teixeira@ig.com", "Campo Grande", "(67)99119-2244"),
    ("Diego Costa", "diegocosta@bol.com", "Belém", "(91)98123-3377"),
    ("Beatriz Ramos", "bia.ramos@icloud.com", "João Pessoa", "(83)98832-1144"),
    ("Thiago Lima", "thi.lima@gmail.com", "Teresina", "(86)99213-8877"),
    ("Luana Pereira", "luana_pereira@outlook.com", "Florianópolis", "(48)98887-2233"),
    ("Felipe Rocha", "felipe.rocha@hotmail.com", "Aracaju", "(79)98119-5588"),
    ("Sofia Martins", "sofiama@gmail.com", "Palmas", "(63)99111-7722"),
    ("Gustavo Moreira", "gustavo_moreira@gmail.com", "São Paulo", "(11)99777-6655"),
    ("Isabela Dias", "isabela.dias@yahoo.com", "Rio de Janeiro", "(21)98123-8899"),
    ("Bruno Silveira", "brunosilveira@uol.com", "Belo Horizonte", "(31)98222-3344"),
    ("Vanessa Lopes", "vanessa.lopes@live.com", "Recife", "(81)99876-2211"),
    ("Leonardo Almeida", "leonardo.almeida@gmail.com", "Fortaleza", "(85)98888-6655"),
    ("Larissa Ferreira", "lari.ferreira@gmail.com", "Brasília", "(61)99122-8899"),
    ("Pedro Henrique", "pedro.henrique@terra.com", "Salvador", "(71)98765-1233"),
    ("Renata Costa", "renatac@gmail.com", "Curitiba", "(41)99112-3322"),
    ("Marcelo Antunes", "marcelo.antunes@hotmail.com", "São Paulo", "(11)99888-3344"),
    ("Daniela Moraes", "danimoraes@yahoo.com", "Porto Alegre", "(51)98113-2244"),
]


# # Inserir clientes
# for cliente in clientes:
#     cursor.execute("""
#         INSERT INTO Clientes (nome, email, cidade, telefone)
#         VALUES (?, ?, ?, ?)
#     """, cliente)

# # Inserir produtos
# for produto in produtos:
#     cursor.execute("""
#         INSERT INTO Produtos (nome, preco, categoria)
#         VALUES (?, ?, ?)
#     """, produto)

# # Confirmar e fechar
# conexao.commit()


print("Dados inseridos com sucesso.")

a = input("deseja inserir um novo cliente(s/n)")
if a == 's':
    nome = input('diga seu nome')
    email = input('diga seu email')
    telefone = input('diga seu telefone')
    cidade = input('diga seu cidade')
    cursor.execute("""
         INSERT INTO Clientes (nome, email, cidade, telefone)
         VALUES (?, ?, ?, ?)
     """,[nome, email,cidade,telefone])

    # Confirmar e fechar
    conexao.commit()
pergunta = input("Deseja inserir um novo produto (s/n)? ").lower()
if pergunta == 's':
    nome = input('Diga o nome do produto: ')
    preco = float(input('Diga o preço: '))
    categoria = input('Diga a categoria: ')
  
    cursor.execute("""
        INSERT INTO Produtos (nome, preco, categoria)
        VALUES (?, ?, ?)
    """, (nome, preco, categoria))

    # Confirmar alteração no banco
    conexao.commit()


# Função para gerar uma data aleatória nos últimos 60 dias
def data_aleatoria():
    hoje = datetime.now()
    dias_antes = randint(0, 60)
    data = hoje - timedelta(days=dias_antes)
    return data.strftime("%Y-%m-%d")

# Exemplo de vendedores
vendedores = ["Lucas", "Mariana", "Carlos", "Fernanda", "João"]

for i in range(10):  # 10 pedidos
    data_compra = data_aleatoria()
    vendedor = choice(vendedores)
    cliente_id = randint(1, 30)  # cliente aleatório

    # Inserir pedido
    cursor.execute("""
        INSERT INTO Pedidos (data_compra, vendedor, cliente_id)
        VALUES (?, ?, ?)
    """, (data_compra, vendedor, cliente_id))

    pedido_id = cursor.lastrowid  # ID do pedido inserido

    # Itens do pedido: entre 1 e 5 produtos
    quantidade_itens = randint(1, 5)

    for _ in range(quantidade_itens):
        produto_id = randint(1, 30)
        quantidade = randint(1, 3)

        # Para pegar o preço do produto, busca na tabela Produtos
        cursor.execute("SELECT preco FROM Produtos WHERE id = ?", (produto_id,))
        preco_unitario = cursor.fetchone()[0]

        # Inserir item do pedido
        cursor.execute("""
            INSERT INTO ItensPedido (pedido_id, produto_id, quantidade, valor_unitario)
            VALUES (?, ?, ?, ?)
        """, (pedido_id, produto_id, quantidade, preco_unitario))

conexao.commit()
conexao.close()

print("Pedidos e itens inseridos com sucesso.")



conexao.close()
