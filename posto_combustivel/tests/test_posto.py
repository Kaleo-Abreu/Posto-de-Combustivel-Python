from models.combustivel import Combustivel, Gasolina, Diesel, Etanol
from models.bomba import BombaDeCombustivel
from models.abastecimento import Abastecimento


def test_combustivel():
    c = Combustivel("Comum", 5.50)
    assert c.calcular_valor(10) == 55.0




def test_gasolina():
    g = Gasolina(6.00)
    assert g.calcular_valor(10) == 60.0


def test_gasolina_aditivada():
    gasolina = Gasolina(6.00, aditivada=True)
    assert gasolina.calcular_valor(10) == 63.0




def test_diesel():
    d = Diesel(5.00)
    assert d.calcular_valor(20) == 100.0


def test_diesel_aditivado():
    diesel = Diesel(5.00, aditivado=True)
    assert diesel.calcular_valor(20) == 104.0




def test_etanol():
    e = Etanol(4.00)
    assert e.calcular_valor(10) == 40.0


def test_etanol_milho():
    etanol = Etanol(4.00, origem="milho")
    assert etanol.calcular_valor(10) == 41.2




def test_bomba():
    bomba = BombaDeCombustivel(1)
    gasolina = Gasolina(6.00)

    bomba.associar_combustivel(gasolina)

    assert bomba.combustivel == gasolina
    assert bomba.realizar_abastecimento(10) == 60.0




def test_abastecimento():
    bomba = BombaDeCombustivel(1)
    gasolina = Gasolina(6.00)

    abastecimento = Abastecimento(
        bomba=bomba,
        combustivel=gasolina,
        litros=20,
        valor=120.0
    )

    assert abastecimento.bomba == bomba
    assert abastecimento.combustivel == gasolina
    assert abastecimento.litros == 20
    assert abastecimento.valor == 120.0