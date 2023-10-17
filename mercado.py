from models.produto import Produto
from models.estoque import Estoque
from models.carrinho import Carrinho
import platform


def main():
    shop()

def shop():

    estoque = Estoque()
    carrinho = Carrinho()

    def cadastrar():
        codigo = str(input('Informe o código do produto: '))
        nome = str(input('Informe o nome do produto: '))
        estoque.cadastrar_produto(codigo, nome)

        print()
        continuar = input('Deseja continuar? [1-Sim, 0-Não]: ')
        if continuar == '1':
            menu()
        else:
            sair()

    def incluir_estoque():
        valores = estoque.listar_produto()

        if valores == None:
            print()
            continuar = input('Deseja continuar? [1-Sim, 0-Não]: ')
            if continuar == '1':
                menu()
            else:
                sair()

        codigo = valores[0]
        nome = valores[1]

        preco = float(input('Informe o preço do produto: '))
        quantidade = int(input('Informe a quantidade a ser incluída no estoque: '))
        estoque.incluir_produto_estoque(codigo, nome, preco, quantidade)

        print()
        continuar = input('Deseja continuar? [1-Sim, 0-Não]: ')
        if continuar == '1':
            menu()
        else:
            sair()

    def listar():
        estoque.listar_produto()

        print()
        continuar = input('Deseja continuar? [1-Sim, 0-Não]: ')
        if continuar == '1':
            menu()
        else:
            sair()

    def comprar():
        estoque.produtos_estoque()
        estoque.incluir_carrinho()

        print()
        continuar = input('Deseja continuar? [1-Sim, 0-Não]: ')
        if continuar == '1':
            menu()
        else:
            sair()

    def visualizar_carrinho():
        carrinho.lista_itens()

        print()
        continuar = input('Deseja continuar? [1-Sim, 0-Não]: ')
        if continuar == '1':
            menu()
        else:
            sair()

    def fechar_pedido():
        estoque.fechar_compra()

        print()
        continuar = input('Deseja continuar? [1-Sim, 0-Não]: ')
        if continuar == '1':
            menu()
        else:
            sair()

    def sair():
        print('Volte sempre!')

    def menu():
        print('===========================================')
        print('===============Bem-vindo===================')
        print('===============Shopping====================')
        print('')
        print('Selecione uma opção abaixo:')
        print('')
        print('1. Cadastrar produto')
        print('2. Incluir produto no estoque')
        print('3. Listar produto')
        print('4. Comprar produto')
        print('5. Visualizar carrinho')
        print('6. Fechar pedido')
        print('7. Sair do sistema')
        print('')
        opcao = int(input('Opção: '))

        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            incluir_estoque()
        elif opcao == 3:
            listar()
        elif opcao == 4:
            comprar()
        elif opcao == 5:
            visualizar_carrinho()
        elif opcao == 6:
            fechar_pedido()
        elif opcao == 7:
            sair()

    menu()

if __name__ == '__main__':
    main()