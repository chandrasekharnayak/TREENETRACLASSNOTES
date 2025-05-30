
from datetime import datetime,timedelta

class BankAccount:
    def __init__(self,account_holder,inital_amount = 100):
        self.account_holder = account_holder
        self.balance  = inital_amount

    def credit(self,amount):
        self.balance += amount
        print(f'account_ holder:- {self.account_holder}, Credit :- {amount}, New Balance :- {self.balance}')

    def debit(self,amount):
        if amount <= self.balance:
            self.balance-=amount
            print(f'account_ holder:- {self.account_holder}, Debit :- {amount}, New Balance :- {self.balance}')
        else:
            print('Insufficent fund')


    def calculate_interest(self,transation_date):
        today = datetime.now().date()
        print(today,type(today))
        delta_days = (today-transation_date).days

        if delta_days>150:
            inteset_rate = 0.25
            interset = self.balance*inteset_rate
            self.balance+=interset
            print(f"Intrest of 25% {interset} applied after {delta_days} days, Current balance:- {self.balance}")

ob1 = BankAccount('202413077898',1000)
ob1.credit(100)
ob1.debit(500)
ob1.credit(1000)
ob1.debit(1700)

#int man
old_date = datetime.now().date()-timedelta(days=160)
ob1.calculate_interest(old_date)


#90days-- elif
#else --- mention



'''
Bus Name:-Dolphin --
Source :- Rourkela
Destination :- BBSR
cost is :- 15,000


seat -- 60
seat price - 1000
cancelation - 25% -- 750

Monday Morning :- 15 seats booked
Monday eveng :- 10 seats booked  and 7 seats cancelled


Tuesdya Morning :- 20 seats booked and 5 seats cancelled
Tuesdya eveng :- 20 seats booked  and 2 seats cancelled

total bus booking amount :- 
monday eod :- total amount, book seat and avl seat
tuesdya eod :- total amount,book seat and avl seat

check the process is profitable or not, if it is profitable how much percent of amount profit , if it is loss amount of percent in loss.

'''






















