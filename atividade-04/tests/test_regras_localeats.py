import pytest

from src.regras_localeats import pedido_atingiu_valor_minimo


# Responsável: Pedro Vital


def test_pedido_no_limite_minimo_e_aceito():
    assert pedido_atingiu_valor_minimo(30) is True


def test_pedido_abaixo_do_minimo_nao_e_aceito():
    assert pedido_atingiu_valor_minimo(29.99) is False


def test_pedido_negativo_gera_value_error():
    with pytest.raises(ValueError, match="negativo"):
        pedido_atingiu_valor_minimo(-0.01)


