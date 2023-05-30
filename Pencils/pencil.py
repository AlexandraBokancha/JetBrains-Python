import random

name_1, bot = 'John', 'Jack'
pencils_showed = 0
real_name = ''
possible_values = ["1", "2", "3"]


def bot_playing():
    global pencils_showed

    if pencils_showed % 4 == 0:
        pencils_showed -= 3
        print("3")
    elif pencils_showed % 4 == 3:
        print("2")
        pencils_showed -= 2
    elif pencils_showed % 4 == 2:
        print("1")
        pencils_showed -= 1
    elif pencils_showed % 4 == 1 and pencils_showed != 1:
        random_num = random.randint(1, 3)
        print(random_num)
        pencils_showed -= random_num


def check_num(value):
    try:
        if value.isdigit() is False:
            print('The number of pencils should be numeric')
        elif int(value) <= 0:
            print('The number of pencils should be positive')
    except ValueError:
        print('The number of pencils should be numeric')


def user_playing():
    global possible_values
    global pencils_showed
    while True:

        pencils_taken = input()

        if pencils_taken not in possible_values:
            print("Possible values: '1', '2' or '3'")
        elif pencils_taken in possible_values and int(pencils_taken) > pencils_showed:
            print('Too many pencils were taken')

        if pencils_taken in possible_values and int(pencils_taken) <= pencils_showed:
            pencils_showed -= int(pencils_taken)
            print(pencils_showed * "|")
            break


print('How many pencils would you like to use: ')

while True:
    number = input()
    check_num(number)
    if number.isdigit() is True and int(number) > 0:
        pencils_showed += int(number)
        break

print('Who will be the first (John, Jack): ')

while True:
    name = input()
    if (name != name_1) and (name != bot):
        print('Choose between John and Jack')

    if name == name_1 or name == bot:
        real_name += name
        print(int(pencils_showed) * "|")
        break

while int(pencils_showed) > 0:

    if pencils_showed != 0:
        if real_name == name_1:
            print("John's turn!")
            real_name = bot
            user_playing()
        else:
            real_name = name_1
            print("Jack's turn: ")
            bot_playing()
            print(int(pencils_showed) * "|")

    if pencils_showed == 0:
        print(f'{real_name} won!')
        break
