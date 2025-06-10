from abc import ABC, abstractmethod

class EstrategiaMulta(ABC):
    @abstractmethod
    def calcular_multa(self, dias: int) -> float:
        pass

class SemMulta(EstrategiaMulta):
    def calcular_multa(self, dias: int) -> float:
        return 0.0

class MultaSimples(EstrategiaMulta):
    def calcular_multa(self, dias: int) -> float:
        return (dias - 7) * 1.50 if dias > 7 else 0.0

class MultaGrave(EstrategiaMulta):
    def calcular_multa(self, dias: int) -> float:
        if dias <= 7:
            return 0.0
        elif dias <= 14:
            return (dias - 7) * 5.00
        else:
            return (7 * 5.00) + ((dias - 14) * 10.00)
