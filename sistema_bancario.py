class ContaBancaria:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de {valor} realizado com sucesso.')
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque de {valor} realizado com sucesso.')
        else:
            print('Saldo insuficiente para realizar o saque.')

    def extrato(self):
        print(f'Extrato da conta de {self.nome}:')
        print(f'Saldo atual: {self.saldo}')

def cadastrar_conta():
    nome = input('Digite o seu nome: ')
    saldo_inicial = float(input('Digite o saldo inicial: '))
    return ContaBancaria(nome, saldo_inicial)

def main():
    conta = None
    while True:
        print('\nBem-vindo ao Sistema Bancário')
        print('1. Criar conta')
        print('2. Depositar')
        print('3. Sacar')
        print('4. Extrato')
        print('5. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            conta = cadastrar_conta()
        elif opcao == '2':
            if conta:
                valor = float(input('Digite o valor a ser depositado: '))
                conta.depositar(valor)
            else:
                print('Por favor, crie uma conta primeiro.')
        elif opcao == '3':
            if conta:
                valor = float(input('Digite o valor a ser sacado: '))
                conta.sacar(valor)
            else:
                print('Por favor, crie uma conta primeiro.')
        elif opcao == '4':
            if conta:
                conta.extrato()
            else:
                print('Por favor, crie uma conta primeiro.')
        elif opcao == '5':
            print('Obrigado por utilizar o Sistema Bancário.')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

if __name__ == "__main__":
    main()
