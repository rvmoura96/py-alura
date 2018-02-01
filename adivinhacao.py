# -*- coding: UTF-8 -*-
print('*' * 32)
print('Bem Vindo ao jogo de adivinhação')
print('*' * 32)

secret_number = 42
attempts = 3

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

print('Suas tentativas acabaram.')
print('Fim do jogo.')