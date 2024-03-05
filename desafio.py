import sqlite3

conexao = sqlite3.connect('desafio')
cursor = conexao.cursor()

#1 - Criação da tabela alunos
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR );')

#2 - Inserção de 5 registros de alunos
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (1,"Aurora",19,"Engenharia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (2,"Beatriz",22,"Pedagogia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (3,"Cida",35,"Engenharia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (4,"Djavan",43,"Musica")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (5,"Eunice",17,"Engenharia")')

#3 - Consultas básicas
# Selecionar todos os registros
tresA = cursor.execute('SELECT * FROM alunos')
for alunos in tresA:
    print(alunos)

# Selecionar nome e idade de alunos com idade>20
tresB = cursor.execute('SELECT nome,idade FROM alunos WHERE idade>20')
for alunos in tresB:
    print(alunos)

# Selecionar alunos de Engenharia em ordem alfabética
tresC = cursor.execute('SELECT nome FROM alunos WHERE curso="Engenharia" ORDER BY nome')
for alunos in tresC:
    print(alunos)

# Contar número total de alunos
tresD = cursor.execute('SELECT COUNT(*) FROM alunos')
for alunos in tresD:
    print(alunos)

# 4 - Atualização e remoção
#Atualize a idade de um aluno
cursor.execute('UPDATE alunos SET idade=55 WHERE nome = "Djavan"')

#Remova um aluno pelo id
cursor.execute('DELETE FROM alunos WHERE id=1')

# 5 - Criar uma tabela e inserir dados
cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY NOT NULL, nome VARCHAR(100), idade INT, saldo FLOAT);')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (1,"Aurora",19,"3.25")')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (2,"Bianca",55,"16.75")')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (3,"Clélia",58,"325.00")')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (4,"Djavan",43,"100.05")')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (5,"Eunice",17,"20.16")')

# 6 - Consultas e funções agregadas
#Selecione nome e idade de clientes com mais de 30 anos
seisA = cursor.execute('SELECT * FROM clientes WHERE idade>30')
for clientes in seisA:
    print(clientes)

# Calcule o saldo médio dos clientes
seisB = cursor.execute('SELECT AVG(saldo) FROM clientes')
for clientes in seisB:
    print(clientes)

# Encontre o cliente com saldo máximo
seisC = cursor.execute('SELECT MAX(saldo) FROM clientes')
for clientes in seisC:
    print(clientes)

# Conte quantos clientes tem saldo acima de 1000
seisD = cursor.execute('SELECT * FROM clientes WHERE saldo>1000')
for clientes in seisD:
    print(clientes)

# 7 - Atualização e remoção com condições
# Atualize o saldo de um cliente
cursor.execute('UPDATE clientes SET saldo = 1000.00 WHERE id = 4')

# Remova o cliente pelo id
cursor.execute('DELETE FROM clientes WHERE id=1')

# Junção de tabelas
cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY NOT NULL, cliente_id INT, produto VARCHAR(150), valor INT);')
cursor.execute('ALTER TABLE compras ADD FOREIGN KEY (cliente_id) REFERENCES clientes (id);')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES (1,1,"Patins",139)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES (2,3,"Espelho",26)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES (3,4,"Pratos",150)')

oito = cursor.execute('SELECT * FROM compras INNER JOIN clientes ON compras.cliente_id = cliente.id')
for usuario in oito:
    print(clientes)


conexao.commit()
conexao.close