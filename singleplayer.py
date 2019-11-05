import random


class Singleplayer():

    def __init__(self):

        self.all_choioces = ['Rock', 'Scissors', 'Paper']
        self.win_list = [['Rock', 'Scissors'], ['Scissors', 'Paper'], ['Paper', 'Rock']]
        self.count = 0
        self.people_count = 0
        self.compute_count = 0
        self.even_count = 0

    def game(self):
        while self.count < 3:
            try:
                computer = random.choice(self.all_choioces)
                people_input = '''Please choose your choice: 0.Rock 1.Scissors 2.Paper'''
                # limit the input is integer
                index = int(input(people_input))
                # limit the input value between 0 to 2
                if index >= 0 and index < 3:
                    people = self.all_choioces[index]
                    print('You：%s,computer：%s' % (people, computer))
                    if people == computer:
                        print('\033[32;1mEven\033[0m')
                        self.even_count += 1
                    elif [people, computer] in self.win_list:
                        print('\033[31;1mYou win this round!\033[0m')
                        self.people_count += 1
                    elif [computer, people] in self.win_list:
                        print('\033[31;1mComputer wins this round!\033[0m')
                        self.compute_count += 1

                    self.count += 1
                else:
                    print('Choose from 0-2, please')
            except ValueError:
                print('Please choose from 0,1,2')
        return self.people_count, self.compute_count, self.even_count

    def win(self, peoplecount, computercount, evencount):
        if peoplecount == 2 or peoplecount == 3 or (peoplecount == 2 and evencount == 1) or (
                peoplecount == 1 and evencount == 2):
            print('\033[31;1mGame over! You win the game!\033[0m')
        elif computercount == 2 or computercount == 3 or (evencount == 1 and computercount == 2) or (
                computercount == 1 and evencount == 2):
            print('\033[31;1mGame over! Computer wins the game!\033[0m')
        elif (evencount == 3) or (peoplecount == computercount == evencount == 1):
            print('\033[32;1mGame over! Even\033[0m')


if __name__ == '__main__':
    s = Singleplayer()
    peoplecount, computercount, evencount = s.game()
    s.win(peoplecount, computercount, evencount)
