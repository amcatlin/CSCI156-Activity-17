__author__ = 'Alicia'
from ss import *


class Employee:
    def __init__(self, last=None, first=None, start=None, pay_rate=None, social=None):
        if (first is None):
            self.last = input("Please enter employees last name: ").strip().lower()
            self.first = input("Please enter employees first name: ").strip().lower()
            self.start = input("Please enter employees starting starting date: ").strip()
            self.pay_rate = float(input("Please enter the employees pay rate: ").strip())
            self.social = SS(input("Please enter employees social security number: ").strip())
        else:
            self.last = last
            self.first = first
            self.start = start
            self.pay_rate = float(pay_rate)
            self.social = SS(social)

    def __str__(self):
        return "Employee " + self.first.capitalize() + " " + self.last.capitalize() + " with social security number " \
               + str(self.social) + " started in " + self.start + " and makes $" + str(self.pay_rate) +" an hour."