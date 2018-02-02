# -*- coding: UTF-8 -*-
from divination import play_divination
from hangman_game import play_hangman_game

def show_menu():  
    print('*' * 32)
    print('Bem Vindo a central de jogos')
    print('1 - Para jogo da Forca')
    print('2 - Para jogo da adivinhação')
    print('*' * 32)
    game=int(input('Escolha seu jogo: '))

    if(game==1):
        play_hangman_game()
    elif(game==2):
        play_divination()

if(__name__ == '__main__'):
    show_menu()