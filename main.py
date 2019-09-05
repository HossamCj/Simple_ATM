class ATM:

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []


    def bank_information(self):
        print('The bank name: ', self.bank_name)
        print('Your account balance: ', self.balance)


    def check_balance(self, request):

        if request > self.balance:
            print('Your request more than your account balance!')

        elif request < 0:
            print('Please input number more than zero!')


    def withdraw(self, request):


        if request <= self.balance:

            amounts_allowed = [100, 50, 10, 5]

            if request > 0:
                self.withdrawals_list.append(request)
                self.balance -= request

                for req in amounts_allowed:
                    while request >= req:
                        request -= req
                        print('give ', req)

            if request < 5:
                print('give ', request, 'coins xD')
                request -= request

        return self.balance

    def show_withdrawals_list(self):

        for withdrawals in self.withdrawals_list:
            print('This is your withdrawals: ', withdrawals)


balance = 300

atm = ATM(balance, 'Islam Bank')

atm.bank_information()

atm.withdraw(103)

atm.bank_information()

atm.show_withdrawals_list()