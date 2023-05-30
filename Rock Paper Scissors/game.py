import random

player_name = input('Enter your name: ')
print(f'Hello, {player_name}')
player_scores = {}

with open('rating.txt', 'r') as file:
    for line in file:
        name, score = line.strip().split()
        player_scores[name] = int(score)

score = player_scores.get(player_name, 0)

while True:
    chose_options = input('')
    print("Okay, let's start")
    if chose_options == '':
        users_options = ['rock', 'paper', 'scissors']
        break
    else:
        users_options = chose_options.split(',')
        break

while True:
    comp_choice = random.choice(users_options)
    make_move = input()
    if make_move == '!exit':
        print('Bye!')
        break
    elif make_move == '!rating':
        print(f'Your rating: {score}')
    elif make_move not in users_options:
        print('Invalid input')
        continue
    else:
        i_user_move = users_options.index(make_move)
        new_list = users_options[i_user_move + 1:] + users_options[:i_user_move]
        take_half = int(len(new_list) / 2)
        win_position = new_list[:take_half]
        loose_position = new_list[take_half:]
        if make_move == comp_choice:
            print(f'There is a draw ({comp_choice})')
            score += 50
        elif comp_choice in loose_position:
            print(f'Well done. The computer chose {comp_choice} and failed')
            score += 100
        elif comp_choice in win_position:
            print(f'Sorry, but the computer chose {comp_choice}')
