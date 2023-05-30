import random


class PartyBillSplitter:
    def __init__(self):
        self.friends = {}
        self.number_of_friends = None
        self.total_bill = None
        self.random_lucky = None

    def get_number_of_friends(self):
        try:
            self.number_of_friends = int(input('Enter the number of friends joining (including you): \n'))
            if self.number_of_friends <= 0:
                raise ValueError
            else:
                self.get_friends_names()
        except ValueError:
            print('No one is joining for the party')

    def get_friends_names(self):
        print('Enter the name of every friend (including you), each on a new line: \n')
        for n in range(int(self.number_of_friends)):
            name = input()
            if name.strip():
                self.friends[name] = 0
        self.get_total_bill()

    def choose_lucky(self):
        lucky_one = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: \n')
        if lucky_one == 'Yes':
            self.random_lucky = random.choice(list(self.friends))
            print(f'{self.random_lucky} is the lucky one!')
            self.recalculate_bill()
        else:
            print('No one is going to be lucky')
            self.split_bill()

    def get_total_bill(self):
        self.total_bill = int(input('Enter the total bill value: \n'))
        self.choose_lucky()

    def split_bill(self):
        for name in self.friends:
            self.friends[name] = round(self.total_bill / self.number_of_friends, 2)
        print(self.friends)

    def recalculate_bill(self):
        n = len(self.friends)
        new_number = n - 1
        new_split_value = round(self.total_bill / new_number, 2)
        for name in self.friends:
            if name == self.random_lucky:
                self.friends[name] = 0
            else:
                self.friends[name] = new_split_value
        print(self.friends)

party = PartyBillSplitter()
party.get_number_of_friends()
