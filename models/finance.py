from odoo import models,fields
class Finance(models.Model):
    _name="office_finance"
    team_id=fields.Many2one("office_team",string="Team Id",required=True);
    project=fields.Char(string="Project",required=True)
    budget=fields.Float(string="Budget",required=True,default='0')
    