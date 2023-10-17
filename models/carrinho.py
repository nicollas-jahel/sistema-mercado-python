

class Carrinho:

    __itens_comprados = []

    def __init__(self):
        pass

    def lista_itens(self):
        for i in self.__itens_comprados:
            print('-----------------------------------')
            print(f'Cod. do produto: {i.codigo}')
            print(f'Quantidade: {i.quantidade}')
            print(f'Nome: {i.nome}')
            print(f'Preço: {i.preco}')
        print('-----------------------------------')

        total = 0
        for i in self.__itens_comprados:
            total += i.preco * i.quantidade

        print(f'Valor total: {total}')


    def adicionar_cesta(self, produto):
        self.__itens_comprados.append(produto)

    def itens_comprados(self):

        itens = []

        for i in self.__itens_comprados:
            itens.append([i.codigo, i.quantidade])

        return itens




