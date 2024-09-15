# Alunos:
# Eduardo Fernandes Albuquerque
# João Pedro Vasconcelos de Lima
# Ladielma Carina Santos Teixeira
# Marcelo Malcher Gillet de Loreto Melo
# Virgilio Cardoso Dantas Neto

import re

def teste_estresse (lista_teste, funcao):
    # Função que vai fazer o teste de estresse com as respostas de aceitação ou não das cadeias
    # condicao para que caso a função seja a g, seguir para um menu de inputs
    if(funcao.__name__ == 'g'):
        # Inputs para os valores dos limites x e y (esses valores vão valer para todo o teste de estresse)
        x = int(input("Coloque um valor para o número x: "))
        y = int(input("Coloque um valor para o número y: "))

        # Laço para garantir que os valores de x e y sejam: x > 0, y > 0 e x <= y
        while(x < 0 or y < 0 or x > y):
            if(x < 0):
                x = int(input("Coloque outro valor para x que seja maior que 0: "))
            if(y < 0):
                y = int(input("Coloque outro valor para y que seja maior que 0: "))
            if(x > y):
                x = int(input("Coloque outro valor para x que seja menor ou igual que o de y: "))

        print("")
        print("")
        for a in lista_teste:
            # Formatação do print no console
            if(funcao(a, x, y)):
                print(f'"{a}" É uma sentença válida')
            else:
                print(f'"{a}" Não é uma sentença válida')
        print("")
        print("")
    else: 
        print("")
        print("")
        for a in lista_teste:
            # Formatação do print no console
            if(funcao(a)):
                print(f'"{a}" É uma sentença válida')
            else:
                print(f'"{a}" Não é uma sentença válida')
        print("")
        print("")

# Primeira questão (Máscaras de validação)
def validar_nome(nome):
    # A função recebe um uma string que contem um nome, e o regex verifica se o nome está no formato correto
    # O nome deve começar com uma letra maiúscula, e pode ter até 3 palavras (nome do meio é opcional), cada uma começando com letra maiúscula
    # Cada nome deve ser separa por um espaço em branco
    regex = re.compile(r"^([A-Z][a-z]*\s){,2}[A-Z][a-z]*$")

    validacao = regex.fullmatch(nome)

    return bool(validacao)

def validar_email(email):
    # A função recebe um uma string que contem um email, e o regex verifica se o email está no formato correto
    # A cadeia deve conter apenas letras minusculas, um símbolo @ e terminar com .br ou .com.br
    # O @ deve estar entre as letras minusculas e deve-se ter no mínimo duas (ex: a@b.com.br)
    regex = re.compile(r"^[a-z]+@[a-z]+\.((com\.)?)br$")

    validacao = regex.fullmatch(email)

    return bool(validacao)

def validar_senha(senha):
    # A função recebe um uma string que contem uma senha, e o regex verifica se a senha está no formato correto
    # A cadeia deve possuir comprimento 8 e conter pelo menos uma letra maiúscula e um número
    regex = re.compile(r"(?=.*[A-Z])(?=.*\d)[A-Za-z0-9]{8}")

    validacao = regex.fullmatch(senha)

    return bool(validacao)

def validar_cpf(cpf):
    # A função recebe um uma string que contem um cpf, e o regex verifica se o cpf está no formato correto
    # O cpf deve atender ao formato "xxx.xxx.xxx-xx", sendo o cpf digitado existente ou não
    regex = re.compile(r"(\d{3}\.){2}\d{3}[-]\d{2}")

    validacao = regex.fullmatch(cpf)

    return bool(validacao)

def validar_numero(telefone):
    # A função recebe um uma string que contem um número de telefone, e o regex verifica se o número está no formato correto
    # O número deve atender a um dos seguintes formatos: (xx) 9xxxx-xxxx, (xx) 9xxxxxxxx ou xx 9xxxxxxxx
    # Assim como o cpf, o número tem que estar dentro do formato, mas não precisa ser um número existente
    regex = re.compile(r"(\(\d{2}\)\s9\d{4}[-]\d{4}|\(\d{2}\)\s9\d{8}|\d{2}\s9\d{8})")

    validacao = regex.fullmatch(telefone)

    return bool(validacao)

def validar_data(data):
    # A função recebe um uma string que contem uma data, e o regex verifica se a data está no formato correto
    # A data deve atender ao formato "dd/mm/aaaa hh:mm:ss"
    # A data não precisa ser válida, apenas estar no formato correto
    regex = re.compile(r"(\d{2}/){2}\d{4}\s(\d{2}:){2}\d{2}")

    validacao = regex.fullmatch(data)

    return bool(validacao)

def validar_numero_real(num):
    # A função recebe um uma string que contem um número real, e o regex verifica se o número está no formato correto
    # Pode ou não conter os símbolos "+" ou "-", e deve conter pelo menos um número
    regex = re.compile(r"(\+|\-)?\d+(.\d+)?")

    validacao = regex.fullmatch(num)

    return bool(validacao)

# Segunda questão (Arranjos familiares)
def a(arranjo):
    # O regex verifica se o arranjo familiar é um casal heterossexual com pelo menos duas filhas ou pelo menos um filho
    regex = re.compile(r"(HM|MH)((h*m+h*m+(h|m)*|m*h+m*(h|m)*))")
    
    validacao = regex.fullmatch(arranjo)

    return bool(validacao)

def b(arranjo):
    # O regex verifica se o arranjo familiar é um casal heterossexual com número ímpar de filhas
    regex = re.compile(r"(HM|MH)(h*m(h*mh*m)*h*)")

    validacao = regex.fullmatch(arranjo)

    return bool(validacao)

def c(arranjo):
    # O regex verifica se o arranjo familiar é um casal heterossexual em que a filha mais velha é mulher e o mais novo é homem
    regex = re.compile(r"(HM|MH)(m(m|h)*h)")

    validacao = regex.fullmatch(arranjo)

    return bool(validacao)

def d(arranjo):
    # O regex verifica se o arranjo familiar é um casal homossexual com pelo menos seis filhos
    # Os dois primeiros filhos e os dois últimos filhos devem formar um casal
    regex = re.compile(r"(MM|HH)(mh|hm)(m|h){2}(m|h)*(mh|hm)")

    validacao = regex.fullmatch(arranjo)

    return bool(validacao)

def e(arranjo):
    # O regex verifica se o arranjo familiar é um casal homossexual em que o sexo dos filhos é alternada
    # A expressão não tá considerando que o casal não tenha filhos
    regex = re.compile(r"(MM|HH)((m(hm)*h?)|(h(mh)*m?))")

    validacao = regex.fullmatch(arranjo)

    return bool(validacao)

def f(arranjo):
    # O regex verifica se o arranjo familiar é um casal homossexual com qualquer número de filhos
    # A expressão não pode ter dois filhos homens consecutivos
    regex = re.compile(r"(MM|HH)h?(m(h?))*")

    validacao = regex.fullmatch(arranjo)

    return bool(validacao)

def g(arranjo, x, y):
    # O regex verifica se o arranjo familiar possui adultos dentro dos limites das variáveis x e y com qualquer número de filhos
    # A expressão não pode aceitar que os três últimos filhos sejam homens
    

    
    
    regex = re.compile(f"(H|M){{{x},{y}}}(((h|m)*(m|mh|mhh))|(h|hh))?")

    validacao = regex.fullmatch(arranjo)

    return bool(validacao)