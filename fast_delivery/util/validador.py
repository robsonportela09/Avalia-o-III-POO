class Validador:
    @staticmethod
    def campo_vazio(texto: str) -> bool:
        return len(texto.strip()) == 0