import sys

from models.finding import Finding
from rules.verify_false import VerifyFalseRule
from report.report import gerar_relatorio, salvar_relatorio


def analisar_arquivo(caminho_arquivo):
    rule = VerifyFalseRule()
    findings = []

    with open(caminho_arquivo, "r") as arquivo:
        for numero_linha, linha in enumerate(arquivo, start=1):
            if rule.detectar(linha):
                snippet = linha.strip()

                finding = Finding(
                    rule.rule_id,
                    rule.titulo,
                    rule.cwe,
                    rule.mensagem,
                    rule.impacto,
                    rule.recomendacao,
                    caminho_arquivo,
                    numero_linha,
                    snippet
                )

                findings.append(finding)

    return findings


if __name__ == "__main__":
    caminho_arquivo = "app.py"

    findings = analisar_arquivo(caminho_arquivo)

    relatorio = gerar_relatorio(findings)
    salvar_relatorio(relatorio)

    print("\n=== SECURITY SCAN RESULTS ===")
    print(f"Findings detected: {len(findings)}")

    for finding in findings:
        print(f"\nRule: {finding.rule_id}")
        print(f"Title: {finding.titulo}")
        print(f"CWE: {finding.cwe}")
        print(f"File: {finding.arquivo}")
        print(f"Line: {finding.linha}")
        print(f"Message: {finding.mensagem}")
        print(f"Impact: {finding.impacto}")
        print(f"Recommendation: {finding.recomendacao}")
        print(f"Snippet: {finding.snippet}")

    if findings:
        print("\nSecurity Gate: BLOCKED")
        sys.exit(1)

    print("\nSecurity Gate: PASSED")
    sys.exit(0)