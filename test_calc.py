from calc import soma, subtracao, multiplicacao, divisao

import pytest

def test_soma():
    assert soma(2, 3) == 4
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0

def test_subtracao():
    assert subtracao(5, 3) == 2
    assert subtracao(10, -3) == 13
    assert subtracao(0, 0) == 0

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(-1, 5) == -5
    assert multiplicacao(0, 10) == 0

def test_divisao():
    assert divisao(10, 2) == 5
    assert divisao(15, 3) == 5
    assert divisao(0, 5) == 0

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)
