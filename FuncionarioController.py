import psycopg2 as psy

class FuncionarioController:
    #Metodo utilizado para o cadastro do funcionario
    def cadastrarFuncionario(idFuncionario, nomeFuncionario, enderecoFuncionario, CPF):
        
    #Consulta todos os funcionario, isso é para ajudar na interface para mostrar os usuários
    def consultarFuncionario(idFuncionario, CPF):

    #Verifica se o funcionario já existe, caso já exista então o cadastro sera reprovado. 
    def verificarFuncionarioExistente(nomeFuncionario, CPF):

