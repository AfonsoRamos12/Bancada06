"""A completar no GL02: duas funções sem entrada/saída ou acesso à rede.

Base conceptual: MT02, EX03. Consultar CONTRATO_GL02.md antes de alterar.
O normalizador verifica apenas quantity, unit, value e quality.
"""
from collections.abc import Mapping
from math import isfinite


from .erros import ErroValidacao

Valor = int | float | None


def normalizar_valor(valor: object) -> int | float | None:
    """Completar: entradas admitidas, rejeições e preservação de tipo/valor."""
    # G2a: None; exclusão de bool/tipos inválidos; finitude dos floats.
    # Não converter em float, arredondar, imprimir ou corrigir silenciosamente.
    
    if valor is None:
        return None
    if isinstance(valor, bool) or not isinstance(valor, (int,float)):
        raise ErroValidacao("value", "tipo_invalido")
    if isinstance(valor,float) and not isfinite(valor):
        raise ErroValidacao("value", "nao_finito")
    return valor
    raise NotImplementedError("G2a: implementar normalizar_valor")


def normalizar_observacao(mensagem: Mapping[str, object]) -> dict[str, object]:
    """Completar: quatro campos verificados, cópia superficial e limites."""
    # G2b: formato; campos obrigatórios; grandeza/unidade; valor; coerência.
    # Preservar todos os restantes campos, sem afirmar que foram validados.
    if not isinstance(mensagem, Mapping):
        raise ErroValidacao("mensagem", "formato_invalido")
    for campo in ("quantity", "unit", "value", "quality"):
        if campo not in mensagem:
            raise ErroValidacao(campo, "campo_em_falta")
        if mensagem["quantity"] != "indice_demo":
            raise ErroValidacao("quantity", "grandeza_nao_admitida")
        if mensagem["unit"] != "u_demo":
            raise ErroValidacao("unit", "unidade_nao_admitida")
        
    valor = normalizar_valor(mensagem["value"])
    qualidade = "missing" if valor is None else "valid"
    if mensagem["quality"] != qualidade:
        raise ErroValidacao("quality", "incoerente")
    
    saida = dict(mensagem)
    saida["value"] = valor
    return saida
            
    raise NotImplementedError("G2b: implementar normalizar_observacao")
