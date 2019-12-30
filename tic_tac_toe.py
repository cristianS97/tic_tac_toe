import os

class Tic_tac_toe:
    def __init__(self):
        self._board = ['-' for i in range(9)]
        self.winner = [False, None]
        self.game_start()

    def game_start(self):
        while True:
            self.print_board()
            self.press_X()
            self.print_board()
            if self.winner[0]:
                break
            self.print_board()
            self.press_O()
            self.print_board()
            if self.winner[0]:
                break

    def print_board(self):
        os.system('cls')
        for i in range(1, 10):
            print(self._board[i-1], end="\t")
            if i % 3 == 0:
                print('\n')

    def press_X(self):
        print('Turno X')
        while True:
            try:
                self._pos = int(input('Ingresa un número entre el 1 y e 9 para hacer la jugada: '))
            except ValueError:
                print('Ingrese un número')
            else:
                if self._pos > 0 and self._pos < 10 and self._board[self._pos - 1] == '-':
                    self._board[self._pos - 1] = 'X'
                    break
        self.verifications()

    def press_O(self):
        print('Turno O')
        while True:
            try:
                self._pos = int(input('Ingresa un número entre el 1 y e 9 para hacer la jugada: '))
            except ValueError:
                print('Ingrese un número')
            else:
                if self._pos > 0 and self._pos < 10 and self._board[self._pos - 1] == '-':
                    self._board[self._pos - 1] = 'O'
                    break
        self.verifications()

    def verifications(self):
        self.diagonal_verification()
        self.horizontal_verifications()
        self.vertical_verifications()
        self.tie_verification()

    def diagonal_verification(self):
        self.diagonal1 = [self._board[0], self._board[4], self._board[8]]
        self.diagonal2 = [self._board[2], self._board[4], self._board[6]]

        self.diagonal1 = set(self.diagonal1)
        self.diagonal2 = set(self.diagonal2)

        if 'X' in self.diagonal1 and not '-' in self.diagonal1:
            self.winner = [True, 'X']
        elif 'O' in self.diagonal1 and not '-' in self.diagonal1:
            self.winner = [True, 'O']
        elif 'X' in self.diagonal2 and not '-' in self.diagonal2:
            self.winner = [True, 'X']
        elif 'O' in self.diagonal2 and not '-' in self.diagonal2:
            self.winner = [True, 'O']

    def horizontal_verifications(self):
        self.horizontal1 = [self._board[0], self._board[1], self._board[2]]
        self.horizontal2 = [self._board[3], self._board[4], self._board[5]]
        self.horizontal3 = [self._board[6], self._board[7], self._board[8]]

        self.horizontal1 = set(self.horizontal1)
        self.horizontal2 = set(self.horizontal2)
        self.horizontal3 = set(self.horizontal3)

        if 'X' in self.horizontal1 and not '-' in self.horizontal1 and not 'O' in self.horizontal1:
            self.winner = [True, 'X']
        elif 'O' in self.horizontal1 and not '-' in self.horizontal1 and not 'X' in self.horizontal1:
            self.winner = [True, 'O']
        elif 'X' in self.horizontal2 and not '-' in self.horizontal2 and not 'O' in self.horizontal2:
            self.winner = [True, 'X']
        elif 'O' in self.horizontal2 and not '-' in self.horizontal2 and not 'X' in self.horizontal2:
            self.winner = [True, 'O']
        elif 'X' in self.horizontal3 and not '-' in self.horizontal3 and not 'O' in self.horizontal3:
            self.winner = [True, 'X']
        elif 'O' in self.horizontal3 and not '-' in self.horizontal3 and not 'X' in self.horizontal2:
            self.winner = [True, 'O']

    def vertical_verifications(self):
        self.vertical1 = [self._board[0], self._board[3], self._board[6]]
        self.vertical2 = [self._board[1], self._board[4], self._board[7]]
        self.vertical3 = [self._board[2], self._board[5], self._board[8]]

        self.vertical1 = set(self.vertical1)
        self.vertical2 = set(self.vertical2)
        self.vertical3 = set(self.vertical3)

        if 'X' in self.vertical1 and not '-' in self.vertical1 and not 'O' in self.vertical1:
            self.winner = [True, 'X']
        elif 'O' in self.vertical1 and not '-' in self.vertical1 and not 'X' in self.vertical1:
            self.winner = [True, 'O']
        elif 'X' in self.vertical2 and not '-' in self.vertical2 and not 'O' in self.vertical2:
            self.winner = [True, 'X']
        elif 'O' in self.vertical2 and not '-' in self.vertical2 and not 'X' in self.vertical2:
            self.winner = [True, 'O']
        elif 'X' in self.vertical3 and not '-' in self.vertical3 and not 'O' in self.vertical3:
            self.winner = [True, 'X']
        elif 'O' in self.vertical3 and not '-' in self.vertical3 and not 'X' in self.vertical3:
            self.winner = [True, 'O']

    def tie_verification(self): # Empate
        if '-' not in self.horizontal1 and '-' not in self.horizontal2 and '-' not in self.horizontal3:
            self.winner = [True, None]

    def get_winnner(self):
        return self.winner

########################
### Bloque principal ###
########################

game = Tic_tac_toe()
winner = game.get_winnner()

if winner[1] != None:
    print(f'El ganador es {winner[1]}')
else:
    print('Ha sido un empate')