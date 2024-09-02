from odoo import models,fields
class Employee(models.Model):
    _name="office_employee"
    emp_name=fields.Char(string="Employee Name",required=True);
    emp_id=fields.Char(string="Employee Id",required=True);
    dept_id=fields.Many2one("office_department",string="Department_id" ,required=True)
    team_id=fields.Many2one("office_team",string="Team_id" ,required=True)


    