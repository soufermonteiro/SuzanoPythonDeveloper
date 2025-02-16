######################################
###    For

texto =  "Juca foi ao mercado" # input("Informe um texto: ")
VOGAIS= "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
    elif letra.upper() == " ":
        print()
else:
    print()

# range(stop) -> range object
# range(start, fim, step)
for numero in range(10, 51, 10):
    print(numero, end=" ")
else:
    print()

######################################
###    While

opcao = -1

while opcao != 0:
    opcao = int(input("Opcoes: \n [1] Sacar \n [2] Extrato \n [0] Sair:\n"))

    if opcao == 1:
        print()
        print("Sacando...")
        print()
    elif opcao == 2:
        print()
        print("Exibindo o extrato...")
        print()
    elif opcao == 0:
        print()
        print("Saindo do programa...")
        print()
    else:
        print()
        print("Opção inválida... Saindo do programa...")
        print()
        break # se eu usar a palavra reservada continue ele pula a execução

