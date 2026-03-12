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
    
quantia = contaBancaria(0)

opcao = 1
valor = 0
while opcao != 0:
    opcao = int(input("Escolha sua opção(1-Depósito/2-Sacar/0-Sair): "))
    if opcao != 0:
        valor = float(input("Digite o valor(R$) : "))
        if opcao == 1:
            quantia.depositar(valor)
        if opcao ==2:
            if valor > quantia.verSaldo():
                print("Saldo Insuficiente!")
            else:
                quantia.retirar(valor)
        print("Saldo Atualizado..: ",f" {quantia.verSaldo():,.2f}")

        class gestaoEstoque:
            def __init__(self):
                self.__produtos = []

            def adicionarProduto(self,produto):
                self.__produtos.append(produto)
                print(f"Sucesso: [produto.nome] cadastrado.")

            def listarProdutos(self):
                print("/n--- RELATÒRIO DE INVENTÀRIO ---")
                for p in self.__produtos:
                    print(f"Item: {p.nome.ljust(15)} | Qtd: {p.quantidade:02d} | Unitário R$(p.preco:,.2f) ")

            def obterValorTotalEstoque(self):
                        total = sum(p.calcularSubtotal() for p in self.__produtos)
                        return total

            def listarEsroqueBaixo(self, limite):
                print(f"/n--- ALERTAS DE ESTOQUE (Limite: {limite})")   
                criticos = [p for in self.__produtos if p.quantidade < limite]

                if not criticos:
                    print("Nenhum item abaixo do limite")

                for p in criticos:
                    print(f"ALERTA: {p.nome} tem apenas {p.quantidade} unidades")

        sistema = gestaoEstoque()

        sistema.adicionarProduto(Produto("Mouse sem fio", 15, 89.90))
        sistema.adicionarProduto(Produto("Monitor Led", 3, 1200.00))
        sistema.adicionarProduto(Produto("Cabo HDMI", 2, 45.00))

        sistema.listarInventario()

        valorTotal = sistema.obterValorTotalEstoque()
        print(f"/nPatrimonio Total em Estoque: R${valorTotal:,.2f}")

        sistema.listarEstoqueBaixo(5)
        
