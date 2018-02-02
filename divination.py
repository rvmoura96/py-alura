# -*- coding: UTF-8 -*-
import random

def play_divination():

    print('*' * 32)
    print('Bem Vindo ao jogo de adivinhação')
    print('Qual nível de dificuldade?')
    print('*' * 32)
    level = int(input('1 - Fácil, 2 - Médio, 3 - Dificil '))
    points = 1000
    secret_number = random.randrange(1, 101)
    attempts = 0

    if(level==1):
        attempts = 20
    elif(level==2):
        attempts = 10
    else:
        attempts =  5

    for i in range(1, attempts + 1):
        print("Tentativa {} de {}".format(i, attempts))
        user_number = int(input('Insira seu número entre 1 e 100: '))
        
        if(user_number < 1 or user_number > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue
        hit = user_number == secret_number
        lesser = user_number < secret_number
        bigger = user_number > secret_number

        if(hit):
            print('Você acertou')
            break
        elif(bigger):
            print('Você errou, seu chute foi maior que o número secreto')
        elif(lesser):
            print('Você errou, seu chute foi menor que o número secreto')

    print('Você fez {}'.format(points))
    print('Fim do jogo.')

if(__name__ == '__main__'):
    play_divination()