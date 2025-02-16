# if, elif, else
##########################################
saldo = 2000.0
saque = float(input("Informe o valor: "))

if saldo > saque:
    print("Realizando saque!")

elif saldo == saque:
    print("Realizando saque, mas ficou zerado!")
    
else:
    print("Saldo insuficiente!")


# if ternário
############################################
saldo = 2000
saque = 3000
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque")