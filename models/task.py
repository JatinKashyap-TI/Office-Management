from odoo import models,fields
class Task(models.Model):
    _name="office_task"
    team_id=fields.Many2one("office_team",string="Team Id",required=True);
    project=fields.Char(string="Project",required=True)
    start_dt=fields.Date(string="Start date",required=True,default=fields.Date.context_today)    