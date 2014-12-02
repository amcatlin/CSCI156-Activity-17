__author__ = 'Alicia'
from ss import *


class Employee:
    def __init__(self, first=None, last=None, start=None, pay_rate=None, social=None):
        if first is None:
            self.first = input("Please enter employees first name: ").strip().lower()
            self.last = input("Please enter employees last name: ").strip().lower()
            self.start = input("Please enter employees starting date: ").strip()
            self.pay_rate = format(float(input("Please enter the employees hourly pay rate: ").strip()), ".2f")
            self.social = SS()
        else:
            self.last = last
            self.first = first
            self.start = start
            self.pay_rate = format(float(pay_rate), ".2f")
            self.social = SS(social)

    def __str__(self):
        return "Employee " + self.first.capitalize() + " " + self.last.capitalize() + " with social security number " +\
               str(self.social.ss) + " started in " + self.start + " and makes $" + str(self.pay_rate) + " an hour."