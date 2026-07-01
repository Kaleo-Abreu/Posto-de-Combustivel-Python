class Combustivel:
    def __init__(self, nome, preco_litro):
        self.id = None
        self.nome = nome
        self.preco_litro = preco_litro

    def calcular_valor(self, litros):
        return self.preco_litro * litros


class Gasolina(Combustivel):
    def __init__(self, preco_litro, aditivada=False):
        super().__init__("Gasolina", preco_litro)
        self.aditivada = aditivada

    def calcular_valor(self, litros):
        valor = super().calcular_valor(litros)
        return valor * 1.05 if self.aditivada else valor


class Diesel(Combustivel):
    def __init__(self, preco_litro, aditivado=False):
        super().__init__("Diesel", preco_litro)
        self.aditivado = aditivado

    def calcular_valor(self, litros):
        valor = super().calcular_valor(litros)
        return valor * 1.04 if self.aditivado else valor


class Etanol(Combustivel):
    def __init__(self, preco_litro, origem="cana"):
        super().__init__("Etanol", preco_litro)
        self.origem = origem

    def calcular_valor(self, litros):
        valor = super().calcular_valor(litros)
        return valor * 1.03 if self.origem == "milho" else valor