#Só lembrando que esse código vai ser mudado devido que não é uma classe e também não temos nossa base de dados
import psycopg2 as psy
#Definindo os variaveis de entrada
idDigitado = "01505010"
senhaDigitada = "Rua Anita Ferraz"
#Conectando a database
conn = psy.connect( dbname="Vendas", user="postgres", password="Koi.io")
#Criando o cursor para poder fazer operações sql
cur = conn.cursor()#teste
cur.execute("SELECT cep.cepid, cep.logradouro FROM cep WHERE cepid = %s and logradouro = %s", (idDigitado, senhaDigitada))
#Adicionando o resultado da consulta em uma variavel
resultado = cur.fetchall()
#Printando o resultado
if len(resultado) == 0:
    print("Resultado nao encontrado")
else:
    print(resultado)

