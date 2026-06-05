from modelos.pedido import Pedido
from modelos.cliente import Cliente
from modelos.entrega import EntregaComum, EntregaExpressa, EntregaPremium

class PedidoService:
    def __init__(self):
        self.__pedidos = []

    def criar_pedido(self, codigo: str, cliente: Cliente, peso: float, distancia: float, opcao_entrega: int):
        if opcao_entrega == 1:
            tipo = EntregaComum()
        elif opcao_entrega == 2:
            tipo = EntregaExpressa()
        elif opcao_entrega == 3:
            tipo = EntregaPremium()
        else:
            print("\n Tipo de entrega inválido!")
            return

        #Passando os dados validados e a classe de entrega para criar o objeto
        novo_pedido = Pedido(codigo, cliente, peso, distancia, tipo)
        self.__pedidos.append(novo_pedido)
        print(f"\n Pedido {codigo} criado! Valor do frete: R$ {novo_pedido.valor_frete:.2f}")

    def listar_pedidos(self):
        if not self.__pedidos:
            print("\n Nenhum pedido registrado.")
            return
        print("\n=== HISTÓRICO DE PEDIDOS ===")
        for p in self.__pedidos: #Getter pra pegar as informações
            print(f"Cód: {p.codigo} | Cliente: {p.cliente.nome} | Frete: R$ {p.valor_frete:.2f} | Status: [{p.status}]")

    def atualizar_status(self, codigo: str, novo_status: int): # Mapeia o num que o usuário escolhe 
        status_map = {1: "Em preparação", 2: "Saiu para entrega", 3: "Entregue", 4: "Cancelado"}
        
        if novo_status not in status_map:
            print("\n Opção de status inválida.")
            return

        for p in self.__pedidos: #Percorre a lista pra achar/att o status pelo setter
            if p.codigo == codigo:
                p.status = status_map[novo_status]
                print(f"\n Status do pedido {codigo} atualizado para '{p.status}'.")
                return
        print("\n Pedido não encontrado.")