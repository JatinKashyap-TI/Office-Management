from odoo import models,fields
class App_pay(models.Model):
    _name="office_pay"
    
    pay=fields.Float(string="Salary",required=True,default='0')
    app=fields.Float(string="Appraisal",required=True,default='1.04')
    emp_id=fields.Many2one("office_employee",string=" Employee Id",required=True);
    