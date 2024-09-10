from odoo import models, fields, _, api
from odoo.exceptions import ValidationError
from datetime import datetime

class Accounting(models.Model):
    _name = "office_accounting"
    
    internal = fields.Integer(string="Money", readonly=True , default=lambda self:self.get_initial_value() ) 
    emp_id = fields.Many2many('office_pay', string="Employee Details")
    time = fields.Datetime(string="Time of payment", readonly=True)
    payment = fields.Integer(readonly=True)

    # @api.model
    # def create(self, vals):
    #     last_record = self.search([], order='id desc', limit=1)
    #     if last_record:
    #         vals['internal'] = last_record.internal
    #     else:
    #         vals['internal'] = 100000
    #     return super(Accounting, self).create(vals)
    def get_initial_value(self):
        last_record = self.search([], order='id desc', limit=1)
        if last_record: 
            if last_record.internal == 0:
                return 100000;
            else:
                return last_record.internal
        else:
            return 100000

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
        self.internal = self.internal - self.payment  
        self.write({'internal': self.internal})  