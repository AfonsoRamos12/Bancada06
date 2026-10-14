"""Seis tarefas de teste. Substituir cada self.fail por asserções verificáveis.

Os nomes identificam famílias de comportamento. Pode utilizar subTest ou
separar os métodos: a quantidade de testes não constitui uma classificação.
"""
import unittest
import math
import json
from copy import deepcopy
from pathlib import Path
from gl02_normalizacao.erros import ErroValidacao
from gl02_normalizacao.validacao import normalizar_valor, normalizar_observacao
from gl02_normalizacao.app import processar_linhas
from tests.test_contrato import mensagem

RAIZ = Path(__file__).resolve().parents[1]

class TestGrupo(unittest.TestCase):
    def test_negativos_e_tipo(self):
        self.assertEqual(normalizar_valor(-4), -4)
        self.assertEqual(normalizar_valor(-2.5), -2.5)
        self.assertIs(type(normalizar_valor(-4)), int)
        self.assertIs(type(normalizar_valor(-2.5)), float)
        """G3.1: -4 e -2.5 preservados, incluindo o tipo numérico."""
        # ChatGPT - Prompt 1: 'self.assertEqual(normalizar_valor(...) correto?'
        # ChatGPT - Prompt 2: 'Adiciona G3.1'
       
    def test_booleanos(self):
        for valor in (True, False):
            with self.subTest(valor=valor), self.assertRaises(ErroValidacao): 
                normalizar_valor(valor)
        """G3.2: True e False rejeitados; verificar campo e motivo."""
        

    def test_nao_finitos(self):
        for valor in (math.nan, math.inf, -math.inf):
            with self.subTest(valor=valor), self.assertRaises(ErroValidacao) as c: 
                normalizar_valor(valor)
            self.assertEqual(c.exception.motivo, 'nao_finito')
        """G3.3: float('nan'), float('inf') e -float('inf') rejeitados."""
      

    def test_coerencia_quality(self):
        casos = [
        (None, "valid"),
        (0, "missing"),
        ]

        for valor, qualidade in casos:
            with self.subTest(valor=valor, qualidade=qualidade):
                obs = mensagem()
                obs["value"] = valor
                obs["quality"] = qualidade

                original = deepcopy(obs)

                with self.assertRaises(ErroValidacao):
                    normalizar_observacao(obs)

                self.assertEqual(obs, original)

        """G3.4: (None, valid) e (0, missing) rejeitados, sem autocorreção."""
        # ChatGPT - 'Faz casos em coerencia_quality de acordo com G3.4'

    def test_copia_e_preservacao(self):
        
        obs = mensagem()
        original = deepcopy(obs)
        
        resultado = normalizar_observacao(obs)
        
        self.assertEqual(obs, original)
        self.assertIsNot(resultado, obs)
        
        for campo in obs:
            if campo not in ("value",):
                self.assertEqual(resultado[campo], original[campo])
        """G3.5: entrada intacta, saída distinta, metadados preservados."""
        # ChaGPT - def test_copia_e_preservacao(self): """G3.5: entrada intacta, saída distinta, metadados preservados."""

    def test_lote_e_repeticao(self):
        """G3.6: 4 aceites/6 rejeitadas; zero final é aceite e repetido."""
        amostras = []

    # 4 observações aceites, incluindo dois zeros
        for valor in (1, 2, 0, 0):
            obs = mensagem()
            obs["value"] = valor
            amostras.append(json.dumps(obs))

    # 6 observações rejeitadas
        for valor in (True, None, math.nan, math.inf, -math.inf, "abc"):
            obs = mensagem()
            obs["value"] = valor
            amostras.append(json.dumps(obs))

        aceites, rejeicoes = processar_linhas(amostras)

    # Verificar quantidades
        self.assertEqual(len(aceites), 4)
        self.assertEqual(len(rejeicoes), 6)

    # Verificar que os dois zeros foram aceites
        zeros = [obs for obs in aceites if obs["value"] == 0]
        self.assertEqual(len(zeros), 2)

    # Verificar as linhas físicas das rejeições
        self.assertEqual(
            [r["linha"] for r in rejeicoes],
            [5, 6, 7, 8, 9, 10],
        )
        # ChatGPT: Prompt 1 (G3.6 inserido)
        # ChatGPT: Prompt 2 (Código inteiro de test_lote_e_repeticao inserido) & função processar_linhas enviado
