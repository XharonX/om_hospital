# from odoo import fields, models, api
import datetime, re

#
# class Department(models.Model):
#     _name = 'hospital.department'
#     _description = 'Hospital Department'
#
#     name = fields.Char('Department', required=True)
#     ward_ids = fields.One2many('hospital.ward', 'department_id', 'Ward')
#     # doctor_ids = fields.One2many('hospital.doctor', string="Doctor")
#
#
# class Ward(models.Model):
#     _name = "hospital.ward"
#     _description = "Hospital Ward"
#
#     name = fields.Char(string="Room NO: ")
#     type = fields.Selection([
#         ('A1', 'A1'),
#         ('B1', 'B1'),
#         ('C', 'C'),
#         ('G', 'G'),
#     ])
#     meal_allowance = fields.Boolean(default=False)
#
#     department_id = fields.Many2one('hospital.department', string='Department')
#     patient_ids = fields.Many2many('hospital.patient', string="Patients", related=True)


class CreditCard:
    def __init__(self,credit_limit, opening_balance=0.0):
        self.opening_balance = opening_balance
        self.statement_date = None
        self.balance = 0.0
        self.withdrawal_amount = 0.0
        self.credit_limit = credit_limit
        self.minimum_payment = 0.0
        self.current_balance = 0.0
        self.due_date = None
        self.monthly_interest = 1.08
        self.monthly_penalty_fee = 1
        self.late_fee = 2
        self.withdrawal_date = None
        self.recharge_date = None

    def withdrawal(self, amount, date:str):
        '''

        :param amount: int or float
        :param date: 1/2/1989
        :return:
        '''

        if (amount > self.credit_limit) and (self.credit_limit > 0) and (amount > 0):
            raise ValueError("You are reach over limit balance")
        else:
            self.current_balance += amount
            self.statement_date = self.get_datetime(date)
            self.minimum_pay()
            self.get_due_date()

    def minimum_pay(self):
        self.minimum_payment = self.current_balance / 1.5

    def recharges_payment(self, amount, date=None):
        self.recharge_date = self.get_datetime(date)
        if self.due_date < self.recharge_date:
            if (amount > 0) and (amount < self.minimum_payment):
                self.current_balance -= amount
                if self.current_balance < 0.0:
                    raise ValueError("self.current_balance is reach less than 0.")
                else:
                    self.current_balance *= self.monthly_interest
                    self.current_balance += self.current_balance*((self.late_fee + self.monthly_penalty_fee)/100)
        else:
            if (amount > 0) and (amount < self.minimum_payment):
                self.current_balance -= amount
                if self.current_balance < 0.0:
                    raise ValueError("self.current_balance is reach less than 0.")
                else:
                    self.current_balance *= self.monthly_interest
                    self.current_balance += self.current_balance * ((self.late_fee + self.monthly_penalty_fee) / 100)

    @staticmethod
    def get_datetime(date=None):
        if date is None:
            return datetime.datetime.now()
        res = list(map(int, re.split('[/,.]', date)))
        return datetime.datetime(res[2],res[1],res[0])

    def get_due_date(self, due_amount=20):
        self.due_date = self.statement_date + datetime.timedelta(days=due_amount)