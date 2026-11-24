from models.finding import Finding
from rules.verify_false import VerifyFalseRule
from report.report import gerar_relatorio, salvar_relatorio

def analisar_arquivo(caminho_arquivo):
    rule = VerifyFalseRule()
    findings = []
    

with open(caminho_arquivo,"r") as arquivo:
    for numero_linha, linha in enumerate(arquivo, start=1):
        if rule.detectar(linha):
            snippet = linha.strip()

            finding = Finding(
                rule.rule_id,
                rule.titutlo,
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

        relatorio = gerar_relatorio(finding)
        salvar_relatorio(relatorio)