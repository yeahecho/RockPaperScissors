import random


all_choioces = ['Rock', 'Scissors', 'Paper']
win_list = [['Rock', 'Scissors'], ['Scissors', 'Paper'], ['Paper', 'Rock']]
poeple_count = 0
compute_count = 0
while poeple_count < 2 and compute_count < 2:
    computer = random.choice(all_choioces)
    people = '''Please choose your choice: 0.Rock 1.Scissors 2.Paper\n'''
    try:
        index = int(input(people))
        poeple = all_choioces[index]
        print('你出的：%s,计算机出的是：%s' % (poeple, computer))
        if poeple == computer:
            print('\033[32;1m平局\033[0m')
        elif [poeple, computer] in win_list:
            print('\033[31;1m你赢了\033[0m')
            poeple_count += 1
        else:
            print('\033[31;1m计算机赢了\033[0m')
            compute_count += 1
    except ValueError:
        print('Please choose from 0-2')
