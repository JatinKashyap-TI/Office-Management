from odoo import models, fields,api
from datetime import datetime
 
 
class Attend(models.Model):
    _name="office_attendence"

    check_in=fields.Selection([('chck','check in'),('waiting','waiting')],default='waiting')
    chck_in=fields.Datetime(string="Check in Time",readonly=True,compute="_compute_chkin",store=True)
    check_out=fields.Selection([('chck_out','check out'),('waiting','waiting')],default='waiting')
    chck_out=fields.Datetime(string="Check out Time",readonly=True,compute="_compute_chkout",store=True)
    present=fields.Integer(readonly=True)
    @api.depends('check_in')
    def _compute_chkin(self):
        for record in self:
            if record.check_in == 'chck':
                record.chck_in=datetime.now()

                
    @api.depends('check_out')
    def _compute_chkout(self):
        for record in self:
            if record.check_out == 'chck_out':
                record.chck_out=datetime.now();
                # date_format = "%m/%d/%Y %H:%M:%S"
                # date1 = datetime.strptime(str(record.chck_in), date_format)
                # date2 = datetime.strptime(str(record.chck_out), date_format)
                # time_difference = date2 - date1
                # hours_difference = time_difference.total_seconds() / 3600
                # record.present=int(hours_difference);
    