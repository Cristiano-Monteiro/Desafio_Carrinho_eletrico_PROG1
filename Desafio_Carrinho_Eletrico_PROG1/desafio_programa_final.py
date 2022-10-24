def calculo_tempo(posicao_inicial, posicao_final, carga):
    variacao_posicao = posicao_final - posicao_inicial
    velocidade = carga / variacao_posicao
    tempo = variacao_posicao / velocidade
    return tempo

# Restrição:  1 ≤ N ≤ 1000
while(True):
    N = int(input('Numero de baterias: ')) 
    if(1 <= N <= 1000):
        break

# Restrição:  1.0 ≤ D ≤ 10000.0
while(True):
    D = float(input('Comprimento da pista: ')) 
    if(1 <= D <= 10000):
        break

lista_baterias = []
lista_posicoes = []

for i in range(0, N):
    print('---'*20)
    # Sempre existe uma bateria na posição 0.0
    if(i == 0):
        print('Posição da bateria: 0.0')
        P = 0.0
        # Restrição: 0.0 < C < 100.0
        while(True):
            C = float(input('Carga da bateria: '))
            if(0 < C < 100):
                break
    else:
        # Restrição:  0.0 ≤ P < D
        while(True):
            P = float(input('Posição da bateria: '))
            if(0 <= P < D):
                break

        # Restrição: 0.0 < C < 100.0
        while(True):
            C = float(input('Carga da bateria: '))
            if(0 < C < 100):
                break
    lista_posicoes.append(P)
    lista_baterias.append(C)

posicao = 0

tempo = 0

total_tempo = 0

for i in range(N):
    if(i == N-1):
        tempo_atual = calculo_tempo(lista_posicoes[i], D, lista_baterias[i])
        tempo_comparacao = calculo_tempo(lista_posicoes[posicao], D, lista_baterias[posicao])
    else:
        tempo_atual = calculo_tempo(lista_posicoes[i], lista_posicoes[i+1], lista_baterias[i])
        tempo_comparacao = calculo_tempo(lista_posicoes[posicao], lista_posicoes[i+1], lista_baterias[posicao])

    if(tempo_atual <= tempo_comparacao):
        posicao = i
    else:
        tempo = tempo_comparacao

    if(tempo_atual <= tempo_comparacao or i == N-1):
        total_tempo += tempo
        tempo = tempo_atual

print('---'*20)
print('Menor tempo: {:.3f}'.format(total_tempo))