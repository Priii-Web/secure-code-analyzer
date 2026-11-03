from models.finding import Finding

def tests_finding_guarda_dados():
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

    assert finding.rule_id == "PY-TLS-001"
    assert finding.arquivo == "app.py"
    assert finding.linha == 5
    assert finding.snippet == "requests.get(url, verify=False)"