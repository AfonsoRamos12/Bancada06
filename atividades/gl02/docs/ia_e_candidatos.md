# G4: Revisão crítica e utilização de IA
## Candidatos fixos
Os candidatos A/B são preparados para ensino. Não foram atribuídos a modelos.
| Candidato | Caso previsto | Resultado observado | Regra violada | Decisão |
|---|---|---|---|---|
| A | Este candidato provavelmente não cumpre a regra S1(Numeros e ausência) pois só aceita float. | Os 10 testes realizados demonstram que
o candidato A só passa o caso de float negativo, e por isso não respeita o contrato. | S1 (Números e ausência) | Devido à falta de
todas as regras, a proposta do candidato A é rejeitada. |
| B | O candidato B provavelmente não cumpre a regra S2(Tipos inválidos) pois não trata booleans. | O candidato B apresenta código que passa
todos os testes excepto os casos booleanos. Embora esteja quase correto, não respeita o contrato. | S2 (Tipos Inválidos) | O candidato B
somente precisa de uma correção para adicionar código relacionado a booleanos, por isso somente precisa dessa correção para validar. |

Os dez casos do comparador são uma amostra, não uma prova universal.
Sem inferências sobre produtividade, aprendizagem ou qualidade de uma ferramenta.
## Utilização efetiva de IA (opcional)
[ ] Não utilizada — comparação realizada com candidatos locais.
[ X ] Utilizada com autorização — preencher campos seguintes.
Ferramenta/modelo efetivamente identificado e data: ChatGPT
Finalidade e ficheiros influenciados: test_grupo.py
Excerto de pedido sem dados pessoais/segredos:
Contribuições aceites/rejeitadas e razão: 
Revisão independente, testes e versão: 

Não substituir este registo por declarações falsas de autoria ou de execução.
Usar apenas as amostras sintéticas fornecidas; sem credenciais ou dados de pessoas.

5.2
	1. Não. Um 'resultado igual a 0' é uma verificação de valor, que nada tem a haver com a preservação de tipo da variável.
	2. Não, pois o contrato deve ser respeitado de forma completa. Se houver duas falhas, não pode ser implementado.
	3. Tratar uma rejeição prevista leva a proposta a ser desafiada e corrigida. Esconder uma excepção traz consequências
	   a longo prazo que podem compremeter um programa inteiro.
	4. A evidência exigida é o entendimento e reproduzibildade do código utilizado.

6. 


