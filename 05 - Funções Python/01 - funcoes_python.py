# Função é um bloco de código identificado por um
# nome e pode receber uma lista de parâmetros,
# esses parâmetros podem ou não ter valores padrões.
# Usar funções torna o código mais legível e 
# possibilita o reaproveitamento de código.
# Programar baseado em funções, é o mesmo que dizer
# que estamos programando de maneira estruturada.

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Fernando"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome = "Fer")
exibir_mensagem_3()
exibir_mensagem_3(nome = "Feroli")
print()
print('====================================')
print()
print()


# Args e kwargs
# Podemos combinar parâmetros obrigatórios com
# args e kwargs. Quando esses são definidos 
# (*args e **kwargs), o método recebe os
# valores como tupla e dicionário respectivamente



def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação entre {a} e {b} = {resultado}")

exibir_resultado(10, 10, somar)
print()
exibir_resultado(10, 10, subtrair)
print()
print()

########################################
# usar variaveis globais em funções
salario = 1950
print(salario)

def salario_mensal(bonus):
    global salario
    
    salario += bonus
    return salario

salario_com_bonus = salario_mensal(500)
print(salario_com_bonus)