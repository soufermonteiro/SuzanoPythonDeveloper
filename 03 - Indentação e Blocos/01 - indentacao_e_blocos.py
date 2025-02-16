# 4 espaços em branco por nível de indentação por convenção em paython
def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente!")

def depositar(valor):
    saldo = 500
    saldo += valor


    print(f"{saldo} É seu saldo! Obrigado por ser nosso cliente!")

sacar(600)
depositar(600)