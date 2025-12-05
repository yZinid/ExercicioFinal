import pytest
from energia import (
    calcular_fornecimento,
    calcular_icms,
    calcular_cofins,
    calcular_pis_pasep,
    calcular_fatura
)

def fixture_casos_teste_obrigatorios():
    return [
        (0, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000),
        (50, 14.0860, 1.9208, 0.8659, 0.1880, 0.1181, 0.0256, 17.2044),
        (100, 28.1720, 3.8416, 1.7318, 0.3760, 0.2362, 0.0513, 34.4088),
        (150, 42.2580, 5.7624, 2.5977, 0.5640, 0.3542, 0.0769, 51.6132),
        (200, 56.3440, 7.6832, 3.4636, 0.7520, 0.4723, 0.1025, 68.8176),
        (250, 70.4300, 23.4766, 5.1467, 1.1174, 1.7156, 0.3725, 102.2587),
        (300, 84.5160, 28.1720, 6.1760, 1.3409, 2.0587, 0.4470, 122.7105),
        (500, 140.8600, 46.9533, 10.2934, 2.2348, 3.4311, 0.7449, 204.5174),
        (800, 225.3760, 75.1253, 16.4694, 3.5756, 5.4898, 1.1919, 327.2279),
        (1200, 338.0640, 112.6879, 24.7041, 5.3634, 8.2347, 1.7878, 490.8419),
    ]

@pytest.mark.parametrize("consumo, esperado", 
                         [(d[0], d[1]) for d in fixture_casos_teste_obrigatorios()])
def test_calcular_fornecimento(consumo: float, esperado: float):
    resultado = calcular_fornecimento(consumo)
    assert round(resultado, 4) == round(esperado, 4)

@pytest.mark.parametrize("consumo, esperado", 
                         [(d[0], d[2]) for d in fixture_casos_teste_obrigatorios()])
def test_calcular_icms(consumo: float, esperado: float):
    resultado = calcular_icms(consumo)
    assert round(resultado, 4) == round(esperado, 4)

@pytest.mark.parametrize("consumo, esperado", 
                         [(d[0], d[3]) for d in fixture_casos_teste_obrigatorios()])
def test_calcular_cofins(consumo: float, esperado: float):
    resultado = calcular_cofins(consumo)
    assert round(resultado, 4) == round(esperado, 4)

@pytest.mark.parametrize("consumo, esperado", 
                         [(d[0], d[4]) for d in fixture_casos_teste_obrigatorios()])
def test_calcular_pis_pasep(consumo: float, esperado: float):
    resultado = calcular_pis_pasep(consumo)
    assert round(resultado, 4) == round(esperado, 4)

@pytest.mark.parametrize("consumo, esperado", 
                         [(d[0], d[7]) for d in fixture_casos_teste_obrigatorios()])
def test_calcular_fatura(consumo: float, esperado: float):
    resultado = calcular_fatura(consumo)
    assert round(resultado, 4) == round(esperado, 4)