import getpass


class Mulitplayer():

    def __init__(self):
        self.all_choices = ['Rock', 'Scissors', 'Paper']
        self.win_list = [['Rock', 'Scissors'], ['Scissors', 'Paper'], ['Paper', 'Rock']]
        self.count = 0
        self.player_1_count = 0
        self.player_2_count = 0
        self.even_count = 0

    def game(self):
        # best of 3
        while self.count < 3:
            try:
                player_1_input = '''Player1 choose your choice: 0.Rock 1.Scissors 2.Paper'''
                player_2_input = '''Player2 choose your choice: 0.Rock 1.Scissors 2.Paper'''

                # limit the input is integer
                # invisible the input, for fair game, use a real terminal, rather than terminal inside Pycharm
                index_1 = int(getpass.getpass(player_1_input))
                index_2 = int(getpass.getpass(player_2_input))

                # limit the input value between 0 to 2
                if (index_1 >= 0 and index_1 < 3) and (index_2 >= 0 and index_2 < 3):
                    palyer_1 = self.all_choices[index_1]
                    palyer_2 = self.all_choices[index_2]
                    print('Player1：%s,Player2：%s' % (palyer_1, palyer_2))
                    if palyer_1 == palyer_2:
                        print('\033[32;1mEven\033[0m')
                        self.even_count += 1
                    elif [palyer_1, palyer_2] in self.win_list:
                        print('\033[31;1mPlayer1 win this round!\033[0m')
                        self.player_1_count += 1

                    elif [palyer_2, palyer_1] in self.win_list:
                        print('\033[31;1mPlayer2 wins this round!\033[0m')
                        self.player_2_count += 1

                    self.count += 1
                else:
                    print('Choose from 0-2, please')
            except ValueError:
                print('Please choose from 0,1,2')
        return self.player_1_count, self.player_2_count, self.even_count

    def win(self, playcount1, playcount2, evencount):
        msg = None
        if playcount1 == 2 or playcount1 == 3 or (playcount1 == 2 and evencount == 1) or (
                playcount1 == 1 and evencount == 2):
            print('\033[31;1mGame over! Player1 win the game!\033[0m')
            msg = 'Game over! Player1 win the game!'
        elif playcount2 == 2 or playcount2 == 3 or (playcount2 == 2 and evencount == 1) or (
                playcount2 == 1 and evencount == 2):
            print('\033[31;1mGame over! Player2 win the game!\033[0m')
            msg = 'Game over! Player2 win the game!'
        elif evencount == 3 or playcount1 == playcount2 == evencount == 1:
            print('\033[32;1mGame over! Even\033[0m')
            msg = 'Game over! Even'
        return msg


if __name__ == '__main__':
    m = Mulitplayer()
    p1_count, p2_count, even_count = m.game()
    m.win(p1_count, p2_count, even_count)
