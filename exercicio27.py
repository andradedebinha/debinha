class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def calcularSubtotal(self):
        return self.quantidade * self.preco


class gestaoEstoque:
    def __init__(self):
        self.__produtos = []

    def adicionarProduto(self, produto):
        self.__produtos.append(produto)
        print(f"Sucesso: [produto.nome] cadastrado.")

    def listarInventario(self):
        print("/n--- RELATÒRIO DE INVENTÀRIO ---")
        for p in self.__produtos:
            print(
                f"Item: {p.nome.ljust(15)} | Qtd: {p.quantidade:02d} | Unitário R$(p.preco:,.2f) ")

    def obterValorTotalEstoque(self):
        total = sum(p.calcularSubtotal() for p in self.__produtos)
        return total

    def listarEstoqueBaixo(self, limite):
        print(f"/n--- ALERTAS DE ESTOQUE (Limite: {limite})")
        criticos = [
            p for p in self.__produtos if p.quantidade < limite]

        if not criticos:
            print("Nenhum item abaixo do limite")

        for p in criticos:
            print(
                f"ALERTA: {p.nome} tem apenas {p.quantidade} unidades")


sistema = gestaoEstoque()

sistema.adicionarProduto(Produto("Mouse sem fio", 15, 89.90))
sistema.adicionarProduto(Produto("Monitor Led", 3, 1200.00))
sistema.adicionarProduto(Produto("Cabo HDMI", 2, 45.00))

sistema.listarInventario()

valorTotal = sistema.obterValorTotalEstoque()
print(f"\nPatrimonio Total em Estoque: R${valorTotal:,.2f}")

sistema.listarEstoqueBaixo(5)
