from odoo import models,fields
class Department(models.Model):
    _name="office_department"
    dept_name=fields.Char(string="Department Name",required=True);
    emp_id=fields.One2many("office_employee","dept_id",string="Employee Id",required=True);
    