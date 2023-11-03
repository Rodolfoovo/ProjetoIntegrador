#Só lembrando que esse código vai ser mudado devido que não é uma classe e também não temos nossa base de dados
import psycopg2 as psy
class loginController:
#Definindo os variaveis de entrada
    def __init__(self,loginId,senha):
        self.loginId = "01505010"
        self.senha = "Rua Anita Ferraz"
    def verificaUsuario(self):
        #Conectando a database
        conn = psy.connect( dbname="Vendas", user="postgres", password="Koi.io")
        #Criando o cursor para poder fazer operações sql
        cur = conn.cursor()
        cur.execute("SELECT cep.cepid, cep.logradouro FROM cep WHERE cepid = %s and logradouro = %s", (self.loginId, self.senha))
        #Adicionando o resultado da consulta em uma variavel
        resultado = cur.fetchall()
        #Printando o resultado
        if len(resultado) == 0:
            return False
        else:
            return True
    def verificaNivelDeAcesso(self):
        conn = psy.connect( dbname="Vendas", user="postgres", password="Koi.io")
        #Criando o cursor para poder fazer operações sql
        cur = conn.cursor()
        cur.execute("SELECT cep.cepid, cep.logradouro, cep.nivelDeAcesso FROM cep WHERE cepid = %s and logradouro = %s", (self.loginId, self.senha))
        #Precisa fazer a implementação da verificação de nivel de acesso.
    
