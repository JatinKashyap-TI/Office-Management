from odoo import models,fields
class Finance(models.Model):
    _name="office_finance"
    team_id=fields.Many2one("office_team",string="Team Id",required=True);
    team_name = fields.Char(string="Team Name", related="team_id.team_name", store=True, readonly=True)
    project=fields.Char(string="Project",required=True)
    budget=fields.Float(string="Budget",required=True,default=0)
    