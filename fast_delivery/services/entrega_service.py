from modelos.entregador import Entregador

class EntregaService:
    def __init__(self):
        self.__entregadores = []

    def cadastrar_entregador(self, nome: str, veiculo: str, cnh: str) -> Entregador:
        novo = Entregador(nome, veiculo, cnh)
        self.__entregadores.append(novo)
        print("\n Entregador cadastrado com sucesso!")
        return novo

    def listar_entregadores(self):
        if not self.__entregadores:
            print("\n Nenhum entregador cadastrado.")
            return
        print("\n=== LISTA DE ENTREGADORES ===")
        for e in self.__entregadores:
            print(f"Nome: {e.nome} | Veículo: {e.veiculo} | CNH: {e.cnh}")