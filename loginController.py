#Só lembrando que esse código vai ser mudado devido que não é uma classe e também não temos nossa base de dados
import psycopg2 as psy
#Definindo os variaveis de entrada
idDigitado = "01505010"
senhaDigitada = "Rua Anita Ferraz"
#Conectando a database
conn = psy.connect( dbname="Vendas", user="postgres", password="Poney2507")
#Criando o cursor para poder fazer operações sql
cur = conn.cursor()
cur.execute("SELECT cep.cepid, cep.logradouro FROM cep WHERE cepid = %s and logradouro = %s", (idDigitado, senhaDigitada))
#Adicionando o resultado da consulta em uma variavel
resultado = cur.fetchall()
if resultado == None:
    print("Resultado não encontrado")
#Printando o resultado
for res in resultado:
    print(res)