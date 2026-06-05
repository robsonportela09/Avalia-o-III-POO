from services.cliente_service import ClienteService
from services.entrega_service import EntregaService
from services.pedido_service import PedidoService
from util.menu import Menu
from util.formatador import Formatador
from util.validador import Validador

def main():
    cliente_service = ClienteService()
    entrega_service = EntregaService()
    pedido_service = PedidoService()

    while True:
        opcao = Menu.exibir_principal()
        Formatador.limpar_tela()

        if opcao == "1":
            print("--- CADASTRO DE CLIENTE ---")
            nome = input("Nome: ")
            cpf = input("CPF: ")
            tel = input("Telefone: ")
            end = input("Endereço: ")
            
            if Validador.campo_vazio(nome) or Validador.campo_vazio(cpf):
                print("\n Nome e CPF são obrigatórios.")
            else:
                cliente_service.cadastrar_cliente(nome, cpf, tel, end)

        elif opcao == "2":
            cliente_service.listar_clientes()

        elif opcao == "3":
            print("--- BUSCAR CLIENTE ---")
            cpf = input("Digite o CPF do cliente: ")
            cli = cliente_service.buscar_por_cpf(cpf)
            if cli:
                print(f"\n Encontrado: {cli.nome} | Endereço: {cli.endereco}")
            else:
                print("\n Cliente não encontrado.")

        elif opcao == "4":
            print("--- CADASTRO DE ENTREGADOR ---")
            nome = input("Nome do Entregador: ")
            veiculo = input("Veículo: ")
            cnh = input("CNH: ")
            entrega_service.cadastrar_entregador(nome, veiculo, cnh)

        elif opcao == "5":
            entrega_service.listar_entregadores()

        elif opcao == "6":
            print("--- CRIAR PEDIDO ---")
            cpf = input("CPF do Cliente cadastrado: ")
            cliente = cliente_service.buscar_por_cpf(cpf)
            
            if not cliente:
                print("\n Cliente não encontrado! Cadastre o cliente primeiro.")
                continue
                
            cod = input("Código do Pedido: ")
            peso = float(input("Peso da carga (kg): "))
            dist = float(input("Distância da entrega (km): "))
            
            print("\nTipos de Entrega:")
            print("1 - Comum (Distância * 1.5)")
            print("2 - Expressa (Distância * 3.0)")
            print("3 - Premium (Distância * 5.0 + 20.0)")
            tipo_op = int(input("Escolha o tipo de entrega: "))
            
            pedido_service.criar_pedido(cod, cliente, peso, dist, tipo_op)

        elif opcao == "7":
            pedido_service.listar_pedidos()

        elif opcao == "8":
            print("--- ATUALIZAR STATUS ---")
            cod = input("Código do Pedido: ")
            print("\nStatus Disponíveis:\n1. Em preparação\n2. Saiu para entrega\n3. Entregue\n4. Cancelado")
            novo_st = int(input("Escolha o novo status: "))
            pedido_service.atualizar_status(cod, novo_st)

        elif opcao == "0":
            print("\nSistema encerrado. Até mais!")
            break
        else:
            print("\n Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()