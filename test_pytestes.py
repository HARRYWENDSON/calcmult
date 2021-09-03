import pytest
from meuApp import mult

@pytest.mark.parametrize('num1,num2,valoresperado', [(0, 10, 0), (2, 5, 7), ( 2, 5, 3), (7.5, 5.4,12.9), ( 1.0, 2.0, 3.0)])
def test_soma(num1,num2, valoresperado):
    assert mult(num1,num2) != valoresperado
