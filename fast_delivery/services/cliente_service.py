from modelos.cliente import Cliente

class ClienteService:
    def __init__(self):
        self.__clientes = []  

    def cadastrar_cliente(self, nome: str, cpf: str, telefone: str, endereco: str) -> Cliente:
    
        if self.buscar_por_cpf(cpf):
            print("\n Erro: Já existe um cliente cadastrado com este CPF.")
            return None
        
        novo_cliente = Cliente(nome, cpf, telefone, endereco)
        self.__clientes.append(novo_cliente)
        print("\n Cliente cadastrado com sucesso!")
        return novo_cliente

    def listar_clientes(self):
        if not self.__clientes:
            print("\n Nenhum cliente cadastrado.")
            return
        print("\n=== LISTA DE CLIENTES ===")
        for c in self.__clientes:
            print(f"Nome: {c.nome} | CPF: {c.cpf} | Tel: {c.telefone} | Endereço: {c.endereco}")

    def buscar_por_cpf(self, cpf: str) -> Cliente:
        for c in self.__clientes:
            if c.cpf == cpf:
                return c
        return None