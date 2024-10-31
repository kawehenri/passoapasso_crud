# primeiro é necessário criar modelo logico e conceitual
# criar o ambiente do codigo
# conectar ao banco com pip install mysql-connector-python
# criar a database (novo banco)
# criar as tabelas
# na pasta conexao é preciso importar (import mysql.connector ) e (conexao=mysql.connector.connect) 
# em seguida colocar as informaçoes do banco criado (senha, host e etc, tudo em ingles)
# host = localhost
# nao esquecer de virgula e parentese
# criar o cursor (cursor = conexao.cursor()) para encerrar (cursor.close()) e (conexao.close())
# agora na pasta de services:
# fazer a importacao com a conexao (from conexao import *)
# criar a funçao def com as variaveis (nome, senha)
# verificar com print se o banco esta conectado
# criar um comando (comando = aspas simples INSERT INTO NOME DA nome da tabela (criar_usuario, criar_senha) VALUES ({...}))
# definir os values
# executar o comando ( cursor.execute(comando))
# editar o banco de dados (conexao.commit())
# ler o banco (cursor.fetchall)



