# Saque deposito estrato

saque = 0
deposito = 0
extrato = 0
quantidadeSaqueDia = 0
saques = []
depositos = []

def opcoes():
    print("[1] - Saque")
    print("[2] - Deposito")
    print("[3] - Extrato")

while (True):

    opcoes()

    usuarioDeseja = int(input("Qual operação deseja realizar: "))

    if(usuarioDeseja == 1):
        saqueUser = float(input("Qual o valor que deseja sacar: "))

        if(saqueUser > deposito or saqueUser >= 500):
            print("Não foi possivel sacar o dinheiro por falta de saldo")
            break
        elif(quantidadeSaqueDia == 3):
            print("Limite diario de saque atingido")
        else:
            deposito -= saqueUser
            print("Saque de R${} realizado com SUCESSO".format(saqueUser))
            quantidadeSaqueDia += 1
            saques.append(saqueUser)
            print(" ")

    elif(usuarioDeseja == 2):
        depositoUser = float(input("Qual o valor que deseja depositar: "))

        if(depositoUser <= 0):
            print("Deposito Invalido")
        else:
            deposito += depositoUser
            depositos.append(depositoUser)

    elif (usuarioDeseja == 3):
        print("Saques Realizados - ", saques)
        print("Depositos Realizados - ", depositos)
            
        break
    else:
        print("Operação Invalida")
        break