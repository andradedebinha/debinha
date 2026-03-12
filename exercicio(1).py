class Cachorro:
    def __init__(self, latir, correr, comer):
        self.latir = latir
        self.correr = correr
        self.comer = comer

    def exibir_informacoes(self):
        print("latir {self.latir} correr {self.correr} comer {self.comer} comer")
        C1 = ("au Au", "correr", "comer")
        C1.exibir_informacoes()
