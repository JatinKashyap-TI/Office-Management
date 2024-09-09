from odoo import models,fields ,api
from odoo.exceptions import ValidationError
class App_pay(models.Model):
    _name="office_pay"
    
    pay=fields.Float(string="Salary",required=True,default=0)
    app=fields.Float(string="Appraisal",required=True,default=1.04)
    emp_id=fields.Many2one("office_employee",string=" Employee Id",required=True);
    emp_name=fields.Char(related="emp_id.emp_name",string="Employee Name",readonly=True,store=True)

    @api.constrains('pay')
    def _check_app(self):
        for record in self:
            if record.app > 2:
                raise ValidationError("Error")
