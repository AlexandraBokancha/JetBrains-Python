class CoffeeMachine():
    def __init__(self):
        self.machine_contents = {
            'water': 400,
            'milk': 540,
            'beans': 120,
            'cups': 9,
            'money': 550
        }

    def remaining(self):
        print(f'''The coffee machine has:
    {self.machine_contents["water"]} ml of water
    {self.machine_contents["milk"]} ml of milk
    {self.machine_contents["beans"]} g of coffee beans
    {self.machine_contents["cups"]} disposable cups
    ${self.machine_contents["money"]} of money \n''')

    def buy(self):
        choose = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: \n')
        if choose == 'back':
            pass
        elif choose == '1':
            if self.machine_contents['water'] < 250:
                print('Sorry, there is not enough water.')
            elif self.machine_contents['beans'] < 16:
                print('Sorry, there are not enough coffee beans.')
            elif self.machine_contents['cups'] < 1:
                print('Sorry, there are not enough disposable cups.')
            else:
                print('I have enough resources, making you a coffee!')
                self.machine_contents['water'] -= 250
                self.machine_contents['beans'] -= 16
                self.machine_contents['cups'] -= 1
                self.machine_contents['money'] += 4
        elif choose == '2':
            if self.machine_contents['water'] < 350:
                print('Sorry, there is not enough water.')
            elif self.machine_contents['milk'] < 75:
                print('Sorry, there is not enough milk.')
            elif self.machine_contents['beans'] < 20:
                print('Sorry, there are not enough coffee beans.')
            elif self.machine_contents['cups'] < 1:
                print('Sorry, there are not enough disposable cups.')
            else:
                print('I have enough resources, making you a coffee!')
                self.machine_contents['water'] -= 350
                self.machine_contents['milk'] -= 75
                self.machine_contents['beans'] -= 20
                self.machine_contents['cups'] -= 1
                self.machine_contents['money'] += 7
        elif choose == '3':
            if self.machine_contents['water'] < 200:
                print('Sorry, there is not enough water.')
            elif self.machine_contents['milk'] < 100:
                print('Sorry, there is not enough milk.')
            elif self.machine_contents['beans'] < 12:
                print('Sorry, there are not enough coffee beans.')
            elif self.machine_contents['cups'] < 1:
                print('Sorry, there are not enough disposable cups.')
            else:
                print('I have enough resources, making you a coffee!')
                self.machine_contents['water'] -= 200
                self.machine_contents['milk'] -= 100
                self.machine_contents['beans'] -= 12
                self.machine_contents['cups'] -= 1
                self.machine_contents['money'] += 6

    def fill(self):
        add_water = int(input('Write how many ml of water you want to add: \n'))
        add_milk = int(input('Write how many ml of milk you want to add: \n'))
        add_beans = int(input('Write how many grams of coffee beans you want to add: \n'))
        add_cups = int(input('Write how many disposable cups you want to add: \n'))
        self.machine_contents['water'] += add_water
        self.machine_contents['milk'] += add_milk
        self.machine_contents['beans'] += add_beans
        self.machine_contents['cups'] += add_cups

    def take(self):
        print(f'I gave you ${self.machine_contents["money"]}\n')
        self.machine_contents['money'] -= self.machine_contents['money']

    def take_action(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit): \n')
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.remaining()
            elif action == 'exit':
                break


make_coffee = CoffeeMachine()
make_coffee.take_action()
