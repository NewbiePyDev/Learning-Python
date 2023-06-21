import random
import time
import pygame
import colorama
from colorama import Fore, Style

colorama.init()
pygame.mixer.init()


class NumberGuessingGame:
    def __init__(self):
        self.inputs = ['y', 'yes', 'YES', 'yesss', 'YEs', 'yEs', 'yES', 'yeS', 'YeS', 'Y', 'yessir']
        self.inputs2 = ['no', 'n', 'nO', 'No', 'NO', 'N', 'nope', 'la', 'LA', 'La', 'LA']
        self.volume = 0.03
        self.boom = pygame.mixer.Sound('boom sound effect.wav')
        self.yes = pygame.mixer.Sound('yes.wav')
        self.womp = pygame.mixer.Sound('womp.wav')

        self.yes.set_volume(self.volume)
        self.womp.set_volume(self.volume)

    def play_game(self):
        while True:
            number = random.randint(1, 25)
            max_guesses = random.randint(4, 8)

            for i in range(max_guesses):
                x = input(Fore.YELLOW + "\nGuess the number I'm thinking about (1-25): ")
                try:
                    x = int(x)
                    if x > number:
                        print(Fore.BLUE + '\tToo high! Try lower.\n')
                    elif x < number:
                        print(Fore.BLUE + '\tToo low! Try higher.\n')
                    else:
                        print(Fore.GREEN + "You're right, the number is", number)
                        self.boom.play()
                        break
                except ValueError:
                    print('Please guess a valid number.')

            else:
                if x != number:
                    print(Fore.RED + "You didn't guess the right number. The correct number was:", number)
                    self.womp.play()
                    time.sleep(1)

            while True:
                y = input('Do you want to play again? (yes/no) ')
                if y in self.inputs or y in self.inputs2:
                    self.yes.play()
                    break
                else:
                    print(Fore.BLUE + 'Please input "yes" or "no".\n')

            if y in self.inputs2:
                break


game = NumberGuessingGame()
game.play_game()
