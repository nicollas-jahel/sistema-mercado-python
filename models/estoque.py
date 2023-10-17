from models.carrinho import Carrinho
from models.produto import Produto


class Estoque:
    __lista_produtos = []
    __estoque = []

    def __init__(self):
        pass

    # cadatra um produto no sistema
    def cadastrar_produto(self, codigo, nome) -> None:
        produto = Produto(codigo=codigo, nome=nome)
        self.__lista_produtos.append(produto)

    # inclui produto no estoque para venda
    def incluir_produto_estoque(self, codigo, nome, preco, quantidade):

        if len(self.__estoque) > 0:
            for i in self.__estoque:
                if i.codigo == codigo:
                    if i.preco == preco:
                        novaQuantidade = i.quantidade + quantidade
                        i.quantidade = novaQuantidade
                    else:
                        resposta = input('Deseja alterar o valor do produto? [1 - Sim, 0 - Não]: ')
                        if resposta == '1':
                            novaQuantidade = i.quantidade + quantidade
                            i.quantidade = novaQuantidade
                            i.preco = preco
                        else:
                            i.quantidade = i.quantidade + quantidade
                    break
                else:
                    produto = Produto(codigo=codigo, nome=nome, preco=preco, quantidade=quantidade)
                    self.__estoque.append(produto)
                    break
        else:
            produto = Produto(codigo=codigo, nome=nome, preco=preco, quantidade=quantidade)
            self.__estoque.append(produto)

    # lista um produto específico
    def listar_produto(self) -> object:
        codigo = str(input('Informe o código do produto: '))

        if len(self.__lista_produtos) > 0:
            dados = []

            for i in self.__lista_produtos:
                if i.codigo == codigo:
                    print('-----------------------------------')
                    print(f'Cod. do produto: {i.codigo}')
                    print(f'Nome: {i.nome}')
                    print('-----------------------------------')
                    dados.append(i.codigo)
                    dados.append(i.nome)

            if dados == None:
                print('Produto não cadastrado.')
            else:
                return dados

        else:
            print('Não há produto cadastrado.')

    # lista todos os produtos em estoque
    def produtos_estoque(self):

        for i in self.__estoque:
            print('-----------------------------------')
            print(f'Cod. do produto: {i.codigo}')
            print(f'Nome: {i.nome}')
            print(f'Quantidade: {i.quantidade}')
            print(f'Preço: {i.preco}')
        print('-----------------------------------')

    def incluir_carrinho(self):
        codigo = str(input('Informe o código do produto: '))
        quantidade = int(input('Informe a quantidade a ser comprada: '))
        carrinho = Carrinho()

        for i in self.__estoque:
            if i.codigo == codigo:
                if i.quantidade >= quantidade:
                    codigo = i.codigo
                    nome = i.nome
                    preco = i.preco
                    quantidadeComprada = quantidade
                    produto = Produto(codigo=codigo, nome=nome, preco=preco, quantidade=quantidadeComprada)
                    carrinho.adicionar_cesta(produto)
                else:
                    print('Não há essa quantidade em estoque')

    def diminui_estoque(self, codigo, quantidade):

        for i in self.__estoque:
            if codigo == i.codigo:
                if quantidade <= i.quantidade:
                    valor = i.quantidade
                    i.quantidade = valor - quantidade
                else:
                    print('Não há essa quantidade em estoque')

    def fechar_compra(self):

        carrinho = Carrinho()
        valores = carrinho.itens_comprados()

        for i in valores:
            codigo = i[0]
            quantidade = i[1]
            self.diminui_estoque(codigo, quantidade)

        print('Compra realizada!')
        print('Obrigado. Volte sempre!')
