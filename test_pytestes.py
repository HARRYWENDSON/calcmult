import pytest
from meuapp import soma

@pytest.mark.parametrize('num1,num2,valoresperado', [(0, 0, 0), (-2,-5,-7), (-2, 5,3), (7.5, 5.4,12.9), (-1.0, -2.0,-3.0), ('DOIS', 2, None)])
def test_soma(num1,num2, valoresperado):
    assert soma(num1,num2) == valoresperado
