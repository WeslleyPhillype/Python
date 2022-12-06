from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')

computador = randint (0, 2)

print(''' Suas Opções :
[0] pedra
[1] papel
[2] tesoura''')

jogador = int(input('Qual é a sua jogada? ' ))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(2)
print('-=' *11)

print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')
print('-=' *11)

if computador == 0:
    if jogador == 0:
        print('EMPATE!')

    elif jogador == 1:
        print('JOGADOR VENCE!')

    elif jogador == 2:
        print('COMPUTADOR VENCE!')

    else:
        print('JOGADA INVÁLIDA!')


if computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')

    elif jogador == 1:
        print('EMPATE!')

    elif jogador == 2:
        print('JOGADOR VENCE!')

    else:
        print('JOGADA INVÁLIDA!')


if computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')

    elif jogador == 1:
        print('COMPUTADOR VENCE!')

    elif jogador == 2:
        print('EMPATE!')

    else:
        print('JOGADA INVÁLIDA!')


    

