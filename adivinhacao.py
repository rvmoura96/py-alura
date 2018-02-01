# -*- coding: UTF-8 -*-
print('*' * 32)
print('Bem Vindo ao jogo de adivinhação')
print('*' * 32)

secret_number = 42
attempts = 3
shout = 1
while(shout <= attempts):
    print("Rodada", shout, " de ", attempts)
    user_number = int(input('Insira seu número: '))
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
    shout = shout + 1

print('Suas tentativas acabaram.')
print('Fim do jogo.')