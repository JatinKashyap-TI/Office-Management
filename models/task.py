from odoo import models,fields,api
from datetime import date
class Task(models.Model):
    _name="office_task"
    team_id=fields.Many2one("office_team",string="Team Id",required=True);
    project=fields.Char(string="Project",required=True)
    start_dt=fields.Date(string="Start date",required=True,default=fields.Date.context_today)    
    time = fields.Char(string='Time (in years)', compute='_compute_time', store=True)
    status=fields.Selection([('just_initiated',' Just Initiated'),('Finished','Finished'),('under process','Under Process')],string="Status",required=True)
    @api.depends('start_dt')
    def _compute_time(self):
        for record in self:
            if record.start_dt:
                today = date.today()
                start_time= fields.Date.from_string(record.start_dt)
                new_time = today.year - start_time.year - ((today.month, today.day) < (start_time.month, start_time.day))
                record.time= "%s years" %new_time

            else:
                record.time = "%s years"% 0