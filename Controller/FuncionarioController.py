import psycopg2 as psy

class FuncionarioController:
    #Metodo utilizado para o cadastro do funcionario
    def cadastrarFuncionario(self,nivelDeAcesso,nomeFuncionario, enderecoFuncionario, CPF,CEP,telefone,senha,funcao):
        #Conectando a database
        conn = psy.connect( dbname="Vendas", user="postgres", password="Koi.io")
        #Criando o cursor para poder fazer operações sql
        cur = conn.cursor()
        #Inserção de todos os atributos do funcionario cadastrado
        cur.execute("INSERT INTO Funcionario VALUES(DEFAULT,%d,%s,%s,%s,%s,%s,%s,%s)",(nivelDeAcesso,nomeFuncionario, enderecoFuncionario, CPF,CEP,telefone,senha,funcao))
        
    #Consulta todos os funcionario, isso é para ajudar na interface para mostrar os usuários
    def consultarFuncionario(idFuncionario, CPF):

    #Verifica se o funcionario já existe, caso já exista então o cadastro sera reprovado. 
    def verificarFuncionarioExistente(nomeFuncionario, CPF):

    def verificarDadosValidos():

