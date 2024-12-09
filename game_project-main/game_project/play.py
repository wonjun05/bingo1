import os
import pygame
from Cube import *
from True_bingo import *
from Fore_bingo import *

pygame.mixer.init()
pygame.mixer.music.load("smvwleo.mp3")
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(loops=-1)


def f_retry():
    difficulty = int(input("난이도를 선택하세요 (2, 3, 4): "))
    if difficulty < 2 or difficulty > 4:
        print("잘못된 입력입니다. 난이도는 2~4 사이여야 합니다.")
        f_retry()
    os.system('cls')


    num_range = {1:9, 2: 20, 3: 50, 4: 70}[difficulty]
    a = Fore_bingo(difficulty,num_range)
    a.fore_play_game()

def t_retry():
    difficulty = 1


    game = TrueBingo(difficulty)
    game.true_play_game()

def play():


    game_choice = input('사칙빙고와 진실빙고 중에 고르시오:')
    if game_choice == '사칙빙고':
        os.system('cls')
        f_retry()
        play()
    elif game_choice == '진실빙고':
        os.system('cls')
        t_retry()
        play()
    else:
        play()
play()