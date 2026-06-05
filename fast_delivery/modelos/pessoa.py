class Pessoa:
    def __init__(self, nome: str):
        # usei o __ para deixar o atributo privado (Encapsulamento)
        # ninguém consegue mudar o nome direto de fora da classe
        self.__nome = nome  

    @property #GETTER
    def nome(self) -> str:
        return self.__nome

    @nome.setter #SETTER
    def nome(self, novo_nome: str):
        if novo_nome.strip():
            self.__nome = novo_nome