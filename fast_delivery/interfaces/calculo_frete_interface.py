from abc import ABC, abstractmethod

class CalculoFreteInterface(ABC):
    
    @abstractmethod 
    def calcular_frete(self, distancia: float) -> float:
        """Método abstrato para o cálculo de frete (Polimorfismo)"""
        pass