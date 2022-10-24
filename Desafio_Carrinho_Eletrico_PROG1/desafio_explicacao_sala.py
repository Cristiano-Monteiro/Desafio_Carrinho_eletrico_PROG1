def calculo_tempo(posicao_inicial, posicao_final, carga):
    variacao_posicao = posicao_final - posicao_inicial
    velocidade = carga / variacao_posicao
    tempo = variacao_posicao / velocidade
    return tempo

# DADOS RETIRADOS DO EXEMPLO NO PDF:

""" 
4      10.000
0.000  1.000
1.200  0.100
3.000  10.000
7.700  1.000 
"""

quantidade_bateria = 4
tamanho_pista = 10

posicoes = [0.0, 1.2, 3, 7.7]
baterias = [1, 0.1, 10, 1]

posicao = 0

tempo = 0

total_tempo = 0

for i in range(quantidade_bateria):
    print('---'*30)
    if(i == quantidade_bateria-1):
        tempo_atual = calculo_tempo(posicoes[i], tamanho_pista, baterias[i])
        print('Tempo atual:       ', posicoes[i], ' -- ', tamanho_pista, ' -- ', baterias[i], ' = ', tempo_atual)
        tempo_comparacao = calculo_tempo(posicoes[posicao], tamanho_pista, baterias[posicao])
        print('Tempo comparação:  ', posicoes[posicao], ' -- ', tamanho_pista, ' -- ', baterias[posicao], ' = ', tempo_comparacao)
    else:
        tempo_atual = calculo_tempo(posicoes[i], posicoes[i+1], baterias[i])
        print('Tempo atual:       ', posicoes[i], ' -- ', posicoes[i+1], ' -- ', baterias[i], ' = ', tempo_atual)
        tempo_comparacao = calculo_tempo(posicoes[posicao], posicoes[i+1], baterias[posicao])
        print('Tempo comparação:  ', posicoes[posicao], ' -- ', posicoes[i+1], ' -- ', baterias[posicao], ' = ', tempo_comparacao)

    if(tempo_atual <= tempo_comparacao):
        posicao = i
    else:
        tempo = tempo_comparacao

    if(tempo_atual <= tempo_comparacao or i == quantidade_bateria-1):
        total_tempo += tempo
        tempo = tempo_atual
    print('---'*30)

print('Menor tempo: {:.3f}'.format(total_tempo))