from odoo import models,fields
class Team(models.Model):
    _name="office_team"
    _rec_name="team_id"
    team_name=fields.Char(string="Team Name",required=True);
    team_id=fields.Char(string="Team Id",required=True);
    team_role=fields.Selection([('odoo',"ODOO Dev Team"),('php','PHP Dev Team'),('system','System Admin team'),('management','Management Team')],string="Team Role",required=True)
    emp_id=fields.One2many("office_employee","team_id",string="Emp Id",required=True);
