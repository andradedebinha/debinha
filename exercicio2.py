class Animal:
    print("Alimenta")

    class Cachorro(Animal):
        def som(self):
            print("late")

class Gato(Animal):
         def som(self)
        print("Mia")

class Passaro(Animal):
    def som(self)
        print("canta")
    

    ser = int(input("Escolha o animal(1-Cachorro / 2-Gato / 3-Passaro)"))
    a2 = Animal()
    if ser = 1:
        a1 = Cachorro
        a2 = Animal
        a1.som()
        a2.comer()


class contaBancaria():
    def __init__(self, saldoInicial):
        self.__saldo = saldoInicial

        def depositar(self, valor):
            if valor > 0:
                self.__saldo += valor

     def retirar(self, valor):
        if valor > 0:
            self.__saldo -= valor

    def verSaldo(self):
        return self.__saldo
    
quantia = contaBancaria


