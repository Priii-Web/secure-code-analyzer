class VerifyFalseRule:
    def __init__(self):
        self.rule_id = "PY-TLS-001"
        self.titulo = "Validação de certificado TLS desabilitada"
        self.cwe = "CWE-295"
        self.mensagem = "Foi identificado uso de verify=False."
        self.impacto = (
            "A validação inadequada do certificado pode facilitar "
            "ataques MITM em determinadas condições."
        )
        self.recomendacao = (
            "Mantenha a validação do certificado habilitada "
            "e evite verify=False."
        )

    def detectar(self, linha):
        return "verify=False" in linha
        
