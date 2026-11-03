from scanner import analisar_arquivo


def test_scanner_detecta_finding(tmp_path):
    arquivo_teste = tmp_path / "codigo_teste.py"

    arquivo_teste.write_text(
        "requests.get(url, verify=False)"
    )

    findings = analisar_arquivo(arquivo_teste)

    assert len(findings) == 1
    assert findings[0].rule_id == "PY-TLS-001"
    assert findings[0].linha == 1
    assert findings[0].snippet == "requests.get(url, verify=False)"
    assert findings[0].arquivo == arquivo_teste


def test_scanner_nao_detecta_verify_true(tmp_path):
    arquivo_teste = tmp_path / "codigo_seguro.py"

    arquivo_teste.write_text(
        "requests.get(url,verify=True)"
    )

    findings = analisar_arquivo(arquivo_teste)

    assert len(findings)  == 0


def test_scanner_detecta_multiplos_findings(tmp_path):
    arquivo_teste = tmp_path / "codigo_multiplos.py"

    arquivo_teste.write_text(
        "requests.get(url1, verify=False)\n"
        "requests.post(url2, verify=False)\n"
        "requests.get(url3, verify=False)"
    )

    findings = analisar_arquivo (arquivo_teste)

    assert len(findings) == 3

