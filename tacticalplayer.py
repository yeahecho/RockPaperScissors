import random


class Tacticalplayer():

    def __init__(self):
        self.all_choices = ['Paper', 'Scissors', 'Rock']
        self.win_list = [['Rock', 'Scissors'], ['Scissors', 'Paper'], ['Paper', 'Rock']]
        self.count = 0
        self.people_count = 0
        self.computer_count = 0
        self.even_count = 0
        self.computer_previous_choice = -1

    def game(self):

        # best of 3
        while self.count < 3:
            try:
                people_input = '''Choose your choice: 0.Paper 1.Scissors 2.Rock'''
                if self.computer_previous_choice == -1:
                    computer_tmp = random.choice(self.all_choices)
                    self.computer_previous_choice = self.all_choices.index(computer_tmp)
                else:
                    index_tmp = self.computer_previous_choice + 1
                    if index_tmp > 2:
                        index_tmp = 0
                    computer_tmp = self.all_choices[index_tmp]
                    self.computer_previous_choice = index_tmp

                if computer_tmp:
                    computer = computer_tmp

                else:
                    computer = random.choice(self.all_choices)
                    if range(len(self.all_choices)):
                        com_index = self.all_choices.index(computer_tmp)

                        computer_tmp = self.all_choices[com_index + 1]
                        computer = computer_tmp

                # limit the input is integer
                index = int(input(people_input))
                # limit the input value between 0 to 2
                if index >= 0 and index < 3:
                    people = self.all_choices[index]
                    print('You：%s,Computer：%s' % (people, computer))
                    if people == computer:
                        print('\033[32;1mEven\033[0m')
                        self.even_count += 1
                    elif [people, computer] in self.win_list:
                        print('\033[31;1mYou win this round!\033[0m')
                        self.people_count += 1
                    elif [computer, people] in self.win_list:
                        print('\033[31;1mComputer wins this round!\033[0m')
                        self.computer_count += 1

                    self.count += 1
                # else:
                #     print('Choose from 0-2, please')
            except ValueError:
                print('Please choose from 0,1,2')

        return self.people_count, self.computer_count, self.even_count

    def win(self, peoplecount, computercount, evencount):
        if peoplecount == 2 or peoplecount == 3 or (peoplecount == 2 and evencount == 1) or (
                peoplecount == 1 and evencount == 2):
            print('\033[31;1mGame over! You win the game!\033[0m')
        elif computercount == 2 or computercount == 3 or (computercount == 2 and evencount == 1) or (
                computercount == 1 and evencount == 2):
            print('\033[31;1mComputer wins the game!\033[0m')
        elif evencount == 3 or peoplecount == computercount == evencount == 1:
            print('\033[32;1mGame over! Even\033[0m')


if __name__ == '__main__':
    t = Tacticalplayer()
    peoplecount, computercount, evencount = t.game()
    t.win(peoplecount, computercount, evencount)
