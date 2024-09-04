from odoo import models,fields,api
from datetime import date
from odoo.exceptions import ValidationError
from datetime import datetime
class Task(models.Model):
    _name="office_task"
    team_id=fields.Many2one("office_team",string="Team Id",required=True);
    project=fields.Char(string="Project",required=True)
    start_dt=fields.Date(string="Start date",required=True,default=fields.Date.context_today)    
    time = fields.Char(string='Time (in years)', compute='_compute_time', store=True)
    status=fields.Selection([('just_initiated',' Just Initiated'),('Finished','Finished'),('under process','Under Process')],string="Status",required=True)
    emp_id=fields.Many2many("office_employee",string="Employees Involved",required=True)
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
    @api.constrains('start_dt')
    def _check_date(self):
        for record in self:
            if record.start_dt < datetime(2020, 1, 1).date():
                raise ValidationError("The date cannot be earlier than 01/01/2020.")