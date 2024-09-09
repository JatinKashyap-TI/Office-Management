from odoo import models, fields, _, api
from odoo.exceptions import ValidationError
from datetime import datetime

class Accounting(models.Model):
    _name = "office_accounting"
    
    internal = fields.Integer(string="Money", default=100000, readonly=True )
    emp_id = fields.Many2many('office_pay', string="Employee Details")
    time = fields.Datetime(string="Time of payment", readonly=True)
    payment = fields.Integer(readonly=True)

    def action_pay_salary(self):
        total_payout = 0  
        for employee in self.emp_id:
            if employee.pay < 0:
                raise ValidationError(_("Employee {} has invalid salary: {}").format(employee.emp_name, employee.pay))

            total_payout += employee.pay

        if self.internal < total_payout:
            raise ValidationError(_("Not enough money to pay employees"))

        self.payment = total_payout
        self.time = datetime.now()

        

        

