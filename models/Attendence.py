from odoo import models, fields,api,_
from datetime import datetime , timedelta
from odoo.exceptions import ValidationError
 
class Attend(models.Model):
    _name="office_attendence"
    _order = 'chck_out desc'

    # check_in=fields.Selection([('chck','check in'),('waiting','waiting')],default='waiting')
    chck_in=fields.Datetime(string="Check in Time",readonly=True)
    # check_out=fields.Selection([('chck_out','check out'),('waiting','waiting')],default='waiting')
    chck_out=fields.Datetime(string="Check out Time",readonly=True)
    present=fields.Integer(string="Number of Hours",readonly=True,compute="_compute_present",store=True)
    attend=fields.Char(string="Status",readonly=True,compute="_compute_attend",inverse="_inverse_attend",store=True)
    emp_atnd=fields.Many2one('office_employee',string="Emp Id")
    check_in_date=fields.Datetime(string="Check in Time",readonly=True)

    def action_do_something(self):
        for record in self:
            existing_record = self.search([
                ('emp_atnd', '=', record.emp_atnd.id),
                ('check_in_date', '=', datetime.now().date()),
            ])
            if existing_record:
                raise ValidationError(_("Already Checked in"))
            else:
                record.chck_in = datetime.now()
                record.check_in_date=datetime.now().date();
        return True

    def action_do_something_check_out(self):
        for record in self:
            existing_record = self.search([
                ('emp_atnd', '=', record.emp_atnd.id),
                ('check_in_date', '=', datetime.now().date()),
                ('chck_out', '=', False)
            ])
            if not existing_record:
                raise ValidationError(_("No matching check-in record found to check out."))
            
            record.chck_in=existing_record.chck_in; 
            existing_record.unlink()  
            record.chck_out = datetime.now()
        return True
    
    # @api.depends('check_in')
    # def _compute_chkin(self):
    #     for record in self:
    #         if record.check_in == 'chck':
    #             record.chck_in=datetime.now()

                
    # @api.depends('check_out')
    # def _compute_chkout(self):
    #     for record in self:
    #         if record.check_out == 'chck_out':
    #             record.chck_out=datetime.now()

    @api.depends('chck_out')
    def _compute_present(self):
        for record in self:
            if record.chck_in and record.chck_out:
                check_in_time = fields.Datetime.from_string(record.chck_in)
                check_out_time = fields.Datetime.from_string(record.chck_out)
                duration = (check_out_time - check_in_time).total_seconds() / 3600
                record.present = duration
            else:
                record.present = 0
    @api.depends('present')
    def _compute_attend(self):
        for record in self: 
            if record.present >= 8 and record.present < 24:
                record.attend="Present"
            elif 4 <= record.present and record.present < 8:
                record.attend="Half Day"
            else:
                record.attend="Absent"
    def _inverse_attend(self):
        for record in self:
            if record.attend=="Absent":
                if record.present > 24:
                    record.chck_out=record.chck_in + timedelta(hours=8)


    
                
    