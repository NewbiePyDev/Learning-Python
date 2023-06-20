import random
import time
import pygame
import colorama
from colorama import Fore, Style


colorama.init()
pygame.mixer.init()

inputs = ['y', 'yes', 'YES', 'yesss', 'YEs', 'yEs', 'yES', 'yeS', 'YeS', 'Y', 'yessir']
inputs2 = ['no', 'n', 'nO', 'No', 'NO', 'N', 'nope', 'la', 'LA', 'La', 'LA']

volume = 0.03

boom = pygame.mixer.Sound('boom sound effect.wav')
yes = pygame.mixer.Sound('yes.wav')
womp = pygame.mixer.Sound('womp.wav')

yes.set_volume(volume)
womp.set_volume(volume)

while True:
    number = random.randint(1, 25)
    max_guesses = random.randint(4, 8)
    
    for i in range(max_guesses):
        x = input(Fore.YELLOW + "\nGuess the number I'm thinking about (1-25): ")
        if x.isdigit():
            x = int(x)
            if x > number:
                print(Fore.BLUE +'\tToo high! Try lower.\n')
            elif x < number:
                print(Fore.BLUE + '\tToo low! Try higher.\n')
            else:
                print(Fore.GREEN + "You're right, the number is", number)
                boom.play()
                break
        else:
            print('Please guess a valid number.')

    else:
        if x != number:
            print(Fore.RED + "You didn't guess the right number. The correct number was:", number)
            womp.play()
            time.sleep(1)

    while True:
        y = input('Do you want to play again? (yes/no) ')
        if y in inputs or y in inputs2:
            yes.play()
            break
        else:
            print(Fore.BLUE+ 'Please input "yes" or "no".\n')

    if y in inputs2:
        break
