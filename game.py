import pygame
import sys
import random
from numbers_generators import UlamNumbersGenerator
from numbers_generators import PrimeNumbersGenerator
#from numbers_generators import LuckyNumbersGenerator

class Game():
    def __init__(self):
        self.hero = Hero()
        self.ulam_generator = UlamNumbersGenerator()
        self.prime_generator = PrimeNumbersGenerator()

    def start_game(self):
        while(self.hero.level < 4 and self.hero.health > 0):
            self.ask_question()

        if(self.hero.health == 0):
            self.lose_game()

        if(self.hero.level == 4):
            self.win_game()

    def ask_question(self):
        sequence_length = random.randint(10, 25)
        number = random.randint(0, sequence_length - 1)
        sequence = self.prime_generator.get_sequence(sequence_length)
        print('Enter', (number+1), 'number of prime sequences:')
        answer = int(input())

        if(answer == sequence[number]):
            self.check_answer(True)

        else:
            self.check_answer(False)


    def check_answer(self, answer):
        if answer:
            print("Right! You are passing to next level")
            self.hero.level += 1

        else:
            print("Wrong! You are losing one life")
            self.hero.health -= 1

    def win_game(self):
        print("Congratulations!!! You are winner!!")
        sys.exit()

    def lose_game(self):
        print("Game over. You are loser!!!")
        sys.exit()

class Hero():
    def __init__(self):
        self.level = 0
        self.health = 3

game = Game()
game.start_game()