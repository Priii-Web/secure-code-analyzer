def gerar_relatorio(findings):
    texto = "Relatório SAST\n"

    for finding in findings:
        texto += "---\n"
        texto += f"Rule ID: {finding.rule_id}\n"
        texto += f"Título: {finding.titulo}\n"
        texto += f"CWE: {finding.cwe}\n"
        texto += f"Arquivo: {finding.arquivo}\n"
        texto += f"Linha: {finding.linha}\n"
        texto += f"Snippet: {finding.snippet}\n"
        texto += f"Mensagem: {finding.mensagem}\n"
        texto += f"Impacto: {finding.impacto}\n"
        texto += f"Recomendação: {finding.recomendacao}\n"

    return texto

def salvar_relatorio(relatorio):
    with open("relatorio.md","w") as arquivo_relatorio:
        arquivo_relatorio.write(relatorio)

















