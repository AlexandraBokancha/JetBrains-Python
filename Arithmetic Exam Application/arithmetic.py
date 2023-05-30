import random

op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y}
right_answer = 0
turn = 5
level = 0
number = 0
no_list = ['no', 'No', 'NO', 'n']
yes_list = ['yes', 'Yes', 'YES', 'y']


def check_answer():
    global number
    while True:
        try:
            number = float(input())
        except ValueError:
            print('Wrong format! Try again.')
            continue
        else:
            break


def check_level():
    global level
    while True:
        try:
            level = float(input('Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - '
                                'integral squares of 11-29\n'))
        except ValueError:
            print('Incorrect format')
            continue

        if level > 2 or level < 1:
            print('Incorrect format')
            continue
        else:
            break


check_level()

while True:
    if level == 1:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        random_op = random.choice(list(op.keys()))
        print(f'{num1} {random_op} {num2}')
        result = op[random_op](num1, num2)
        check_answer()
        if number == result:
            print('Right!')
            right_answer += 1
            turn -= 1
        else:
            print('Wrong!')
            turn -= 1
    elif level == 2:
        num = random.randint(11, 29)
        print(num)
        check_answer()
        result = num ** 2
        if number == result:
            print('Right!')
            right_answer += 1
            turn -= 1
        elif number != result:
            print('Wrong')
            turn -= 1
    if turn == 0:
        break

save = input(f'Your mark is {right_answer}/5. Would you like to save the result? Enter yes or no.\n')

while True:
    if save in yes_list:
        if level == 1:
            f = open('results.txt', 'a')
            name = input('What is your name?\n')
            f.write(f'{name}: {right_answer}/5 in level {int(level)} (simple operations with numbers 2-9)')
            f.close()
            print('The results are saved in "results.txt".')
            break
        elif level == 2:
            f = open('results.txt', 'a')
            name = input('What is your name?\n')
            f.write(f'{name}: {right_answer}/5 in level {level} (integral squares 11-29)')
            f.close()
            print('The results are saved in "results.txt".')
            break
    else:
        break
