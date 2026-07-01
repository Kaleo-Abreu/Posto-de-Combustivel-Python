from datetime import datetime


class Abastecimento:

    def __init__(self, bomba, combustivel, litros, valor):
        self.bomba = bomba
        self.combustivel = combustivel
        self.litros = litros
        self.valor = valor
        self.data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")