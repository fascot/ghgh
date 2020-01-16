""" This is the code with games and calculator functions """

import random

class GAMES():
    """ This is the class with games(methods) """

    def __init__(self, color, doors, tires, vtype):
        """Constructor"""

        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def my_game1(self):
        """ this is the 'Guess number' """

        print('I was thinking of the number from 1 to 1000, can you guess it?')
        attempt = 10
        larger = 'No, your number is too little.'
        smaller = 'No, your number is too big. '
        rightly = 'Yes, it is the number I was thinking of! '
        number = random.randint(1, 1000)
        if self.color == 0:
            return None
        while attempt != 0:
            attempt -= 1
            inputer = int(input())
            if inputer != number:
                if inputer > number:
                    print(smaller)
                elif inputer < number:
                    print(larger)
            else:
                return rightly
            print('You have', attempt, 'attempts')
        if attempt == 0:
            return 'Game over'

    def my_game2(self):
        """ Tis is the 'Guess number' from the internet """

        print('I was thinking of the number from 1 to 100, can you guess it?')
        attempt = 10
        larger = 'No, your number is too little.'
        smaller = 'No, your number is too big. '
        rightly = 'Yes, it is the number I was thinking of! '
        number = random.randint(1, 100)
        if self.color == 0:
            return None
        while attempt != 0:
            attempt -= 1
            inputer = int(input())
            if inputer != number:
                if inputer > number:
                    print(smaller)
                elif inputer < number:
                    print(larger)
            else:
                return rightly
            print('You have', attempt, 'attempts')
        if attempt == 0:
            return 'Game over'

    def your_game_choise(self):
        """ This is the game choise method """

        print('Choise the game: "First game" or "Second game"?')
        inputer = str(input())
        if inputer == 'First game':
            print(self.my_game1())
        elif inputer == 'Second game':
            print(self.my_game2())
        return "Thank, you!"

class CALCULATOR():
    """This is the calculator function class"""

    def __init__(self, afer, bufer):
        self.afer = afer
        self.bufer = bufer

    def my_sum(self, afer, bufer):
        """Sum function"""

        if self.afer == afer and self.bufer == bufer:
            return afer + bufer
        return afer + bufer

    def my_difference(self, afer, bufer):
        """Difference function"""

        if self.afer == afer and self.bufer == bufer:
            return afer - bufer
        return afer - bufer

    def my_composition(self, afer, bufer):
        """Composition function"""

        if self.afer == afer and self.bufer == bufer:
            return afer * bufer
        return afer * bufer

    def my_perticular(self, afer, bufer):
        """Perticular function"""

        if self.afer == afer and self.bufer == bufer:
            return afer / bufer
        return afer / bufer

    def my_square_root(self, afer):
        """Square root function"""

        if self.afer == afer:
            return afer ** 0.5
        return afer ** 0.5

    def your_calculator_function_choise(self):
        """This is the calculator function choise method"""



        print('''Choise what function you will use: "Sum"
, "Differense, "Composition", "Perticular" or "Square root"''')
        inputer = str(input())
        if inputer == "Sum":
            print(self.my_sum(int(input()), int(input())))
        elif inputer == "Differense":
            print(self.my_difference(int(input()), int(input())))
        elif inputer == "Composition":
            print(self.my_composition(int(input()), int(input())))
        elif inputer == "Perticular":
            print(self.my_perticular(int(input()), int(input())))
        elif inputer == "Square root":
            print(self.my_square_root(int(input())))
        return "Thank, you!"

GAMES_OBJECT = GAMES(1, 1, 1, 1)
CALCULATOR_OBJECT = CALCULATOR(1, 1)
def games_or_calculator():
    """This is the choise class method"""

    print('Choise what will you use: "Games" or "Calculator"?')
    inputer = input()
    if inputer == "Games":
        print(GAMES_OBJECT.your_game_choise())
    elif inputer == "Calculator":
        print(CALCULATOR_OBJECT.your_calculator_function_choise())
    return "Goodbye!"

if __name__ == "__main__":
    print(games_or_calculator())
