#2
#Defina uma classe BankAccount com atributos privados balance e account_number. Crie métodos deposit e withdraw para manipular o saldo.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance
    
    def sacar(self, valor):
        if self.__balance > valor:
            self.__balance -= valor
            return self.__balance
        else:
            print('Saldo insuficiente')
    
    def depositar(self,valor):
        self.__balance += valor
        return self.__balance
    
bank = BankAccount('3345978',2000)
bank2 = BankAccount('4654625',5000)

print(bank.sacar(200))
print(bank.depositar(400))

print(bank2.sacar(1000))
print(bank2.depositar(2000))