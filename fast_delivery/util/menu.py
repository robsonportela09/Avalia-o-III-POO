class Menu:
    @staticmethod
    def exibir_principal():
        print("\n|==============================|")
        print("|    FASTDELIVERY EXPRESS      |")
        print("|==============================|")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Buscar Cliente por CPF")
        print("4. Cadastrar Entregador")
        print("5. Listar Entregadores")
        print("6. Criar Novo Pedido")
        print("7. Listar Todos os Pedidos")
        print("8. Atualizar Status de Pedido")
        print("0. Sair do Sistema")
        print("==============================")
        return input("Escolha uma opção: ")