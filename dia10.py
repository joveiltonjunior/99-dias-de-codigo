import random 

def distribuir_cartas ():
    '''Retorna cartas aleatórias da lista de cartas'''
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    carta = random.choice(cartas)
    return carta

def calculadora_score (cartas):
    ''''Pega a lista de cartas e retorna a soma dos pontos calculados'''
    if sum(cartas) == 21 and len(cartas )== 2:
        return 0
    if 11 in cartas and sum(cartas)> 21:
        cartas.remove(11)
        cartas.append(1)

    return sum(cartas)

def comparação (p_jogador,p_dealer):
    if p_jogador == p_dealer:
        return 'Empate'
    elif p_dealer == 0:
        return 'O Dealer Ganhou você perdeu GAME OVER'
    elif p_jogador == 0 :
        return 'Parabéns você ganhou, você tem 21 pontos'
    elif p_jogador > 21:
        return 'você passou de 21 pontos perdeu GAME OVER'
    elif p_dealer > 21:
        return 'Parabéns você ganhou, o dealer passou dos 21 pontos'
    elif p_jogador > p_dealer:
        return 'Parabéns você ganhou,'
    else:
        return 'Você perdeu GAME OVER'


carta_jogador = []
carta_dealer = []
pontos_dealer = -1
pontos_jogador = -1
game_over = False

for _ in range (2):
    carta_jogador.append(distribuir_cartas())
    carta_dealer.append(distribuir_cartas())

while not game_over:
    pontos_jogador =calculadora_score(carta_jogador)
    pontos_dealer = calculadora_score(carta_dealer)
    print (f'suas cartas são {carta_jogador} a soma e {pontos_jogador}')
    print (f'A primeira carta do dealer é {carta_dealer[0]}')

    if pontos_jogador == 0 or pontos_dealer == 0 or pontos_jogador > 21:
        game_over = True

    else:
        outra_carta = input ('Você gostaria de mais uma carta [s] sim e [n] para não: ')
        if outra_carta == 's':
            carta_jogador.append(distribuir_cartas())
        else:
            game_over = True

while pontos_dealer != 0 and pontos_dealer <17:
    carta_dealer.append(distribuir_cartas())
    pontos_dealer = calculadora_score(carta_dealer)

print (comparação(pontos_jogador, pontos_dealer))