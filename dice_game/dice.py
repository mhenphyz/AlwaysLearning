from random import randrange


class DiceGame():

    def __init__(self):
        self.line_separator = (('=' * 50) + '\n')
        print(f'{self.line_separator} Welcome to the Dice Game \n{self.line_separator}')
        self.points_player_1 = 0
        self.points_player_2 = 0
        self.points_computer = 0
        self.type_of_game = 2

    def config(self):
        print('The game can be played by two players or by one player vs computer')
        print('\nSelect one option:')
        print('1 - 1 vs 1:')
        print('2 - 1 vs Computer')
        self.type_of_game = int(input())

    def player_vs_player(self):
        print('Player 1:')
        self.points_player_1 = randrange(1,7)
        print(self.points_player_1)
        print('Player 2:')
        self.points_player_2 = randrange(1,7)
        print(self.points_player_2)

        if self.points_player_1 > self.points_player_2:
            print('Player 1 wins')
        elif self.points_player_1 == self.points_player_2:
            print('It\'s a Draw')
        else:
            print('Player 2 Wins')

    def player_vs_computer(self):
        print('Player 1:')
        self.points_player_1 = randrange(1,7)
        print(self.points_player_1)
        print('Computer:')
        self.points_computer = randrange(1,7)
        print(self.points_computer)

        if self.points_player_1 > self.points_computer:
            print('Player 1 wins')
        elif self.points_player_1 == self.points_computer:
            print('It\'s a Draw')
        else:
            print('Computer Wins')

    def start(self):
        print(self.line_separator)
        print('Starting game', end='\n\n\n')

        print(type(self.type_of_game))

        if self.type_of_game is not 2:
            self.player_vs_player()
        else:
            self.player_vs_computer()

        


if __name__ == '__main__':
    
    game = DiceGame()
    game.config()
    game.start()
