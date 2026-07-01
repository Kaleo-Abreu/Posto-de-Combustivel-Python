class BombaDeCombustivel:
    def __init__(self, numero):
        self.id = None
        self.numero = numero
        self.combustivel = None

    def associar_combustivel(self, combustivel):
        self.combustivel = combustivel

    def realizar_abastecimento(self, litros):
        if litros <= 0:
            raise ValueError("Litros inválidos")

        if not self.combustivel:
            raise ValueError("Bomba sem combustível")

        return self.combustivel.calcular_valor(litros)