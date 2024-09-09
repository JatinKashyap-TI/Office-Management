from odoo import models,fields
from datetime import datetime , timedelta

class Employee(models.Model):
    _name="office_employee"
    _rec_name="emp_id"
    emp_name=fields.Char(string="Employee Name",required=True);
    emp_id=fields.Char(string="Employee Id",required=True);
    dept_id=fields.Many2one(comodel_name="office_department",string="Department id" ,required=True)
    team_id=fields.Many2one("office_team",string="Team id" ,required=True)
    dept_name = fields.Char(string="Department Name", related="dept_id.dept_name",  readonly=True)
    team_name = fields.Char(string="Team Name", related="team_id.team_name",  readonly=True)
    atnd=fields.One2many('office_attendence','emp_atnd',string="Attendence",readonly=True)
  