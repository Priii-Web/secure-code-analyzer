
import pytest

from rules.verify_false import VerifyFalseRule


def test_detecta_verify_false():
    rule = VerifyFalseRule()

    linha = "requests.get(url, verify=False)"

    resultado = rule.detectar(linha)

    assert resultado is True



def test_nao_detecta_verify_true():
    rule = VerifyFalseRule()

    linha = "requests.get(url, verify=True)"

    resultado = rule.detectar(linha)

    assert resultado is False


def test_detecta_verify_false_em_post():
    rule = VerifyFalseRule()

    linha = "requests.post(url, verify=False)"

    resultado = rule.detectar(linha)

    assert resultado is True


@pytest.mark.xfail(reason="V1 usa busca textual exata e não reconhece espaços")
def test_detecta_verify_false_com_espacos():
    rule = VerifyFalseRule()

    linha = "requests.get(url,verify = False)"

    resultado = rule.detectar(linha)

    assert resultado is True


@ pytest.mark.xfail(reason="V1 não diferencia código executável de comentários")
def test_nao_detecta_verfy_false_em_comentario():
    rule = VerifyFalseRule()

    linha = "# não use verify=False em produção"

    resultado = rule.detectar(linha)

    assert resultado is False

    