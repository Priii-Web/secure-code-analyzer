from models.finding import Finding
from report.report import gerar_relatorio

def test_gerar_relatorio_com_finding():
    finding = Finding(
        "PY-TLS-001",
        "Validação de certificado TLS desabilitada",
        "CWE-295",
        "Foi identificado uso de verify=False.",
        "Impacto de teste",
        "Recomendação de teste",
        "app.py",
        5,
        "requests.get(url, verify=False)"

    )

    findings = [finding]

    relatorio = gerar_relatorio(findings)

    assert "PY-TLS-001" in relatorio
    assert "CWE-295" in relatorio
    assert "app.py" in relatorio
    assert "Linha: 5" in relatorio
    assert "requests.get(url, verify=False)" in relatorio