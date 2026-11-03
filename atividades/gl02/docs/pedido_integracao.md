# Pedido de integração GL02 (registo local ou equivalente institucional)
Título: Normalização de mensagens e revisão de código  Grupo: B06  Ramo: gl02/normalizacao
Autor(es): Afonso Ramos, Luís Costa, Diogo Almeida  Revisor(es): Afonso Ramos, Luís Costa, Diogo Almeida  Data: 14/10/26
Commit do código revisto: "Implementa normalizacao e testse GL02"  Destino: main (ou ramo acordado)

## Objetivo e âmbito
Regras S__ cobertas: Houve interação com todas as regras desde S1 a S8.
Código fornecido/reutilizado e adaptações: 
Código fornecido pelo docente; MT02
Código fornecido por um LLM; ChatGPT -> test_grupo.py

Ficheiros alterados: docs/contrato_e_tests.md, gl02_normalizacao/validacao.py, gl02/tests/test_grupo.py
## Evidências
Comando de teste e resultado:
./.venv/bin/python -m unittest tests.test_contrato -v
./.venv/bin/python -m unittest tests.test_grupo -v
./.venv/bin/python -m unittest discover -s tests -v
./.venv/bin/python -m gl02_normalizacao dados/lote_gl02.jsonl
./.venv/bin/python comparar_candidatos.py
Todos os testes dão um output de 'ok' sem errors depois de resolvidos.

Lote: 14 (De ./.venv/bin/python -m unittest discover -s tests -v)  Contraexemplo escolhido pelo revisor: ___

## Revisão por outro elemento
| Observação concreta (ficheiro/regra) | Consequência | Decisão e justificação |
|---|---|---|
| | | |
| | | |
A apreciação pode confirmar uma opção correta; não é necessário inventar defeitos.
## Decisão
[ ] Aceitar  [ ] Solicitar alteração  [ ] Não integrar; motivo: ___
Novo commit revisto após correções (quando exista): ___
Limitações: validação só de quatro campos; sem deduplicação/IoT/persistência.

Se forem alterados código ou testes após a revisão, voltar a apresentar o diff.
O hash final de integração é registado na ficha de evidências, não se tenta
incluir num ficheiro o hash do commit que ainda o irá conter.
