from interfaces.calculo_frete_interface import CalculoFreteInterface

# POLIMORFISMO, todas calculam o frete da sua maneira, mas todas assinam o contrato da interface.
class EntregaComum(CalculoFreteInterface):
    def calcular_frete(self, distancia: float) -> float:
        return distancia * 1.5 # Fórmula da entrega comum pedida no trabalho

class EntregaExpressa(CalculoFreteInterface):
    def calcular_frete(self, distancia: float) -> float:
        return distancia * 3.0 # Fórmula da entrega expressa

class EntregaPremium(CalculoFreteInterface):
    def calcular_frete(self, distancia: float) -> float:
        return (distancia * 5.0) + 20.0 # Fórmula da entrega premium + taxa