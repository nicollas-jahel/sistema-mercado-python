class Produto:

    def __init__(self, **kwargs) -> None:

        self.__codigo: str = kwargs.get('codigo')
        self.__nome: str = kwargs.get('nome')
        self.__preco: float = kwargs.get('preco')
        self.__quantidade: int = kwargs.get('quantidade')

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def preco(self) -> float:
        return self.__preco

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade
