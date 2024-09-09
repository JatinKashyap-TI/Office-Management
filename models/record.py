from odoo import models,fields,api
from datetime import date

class Record(models.Model):
    _name="office_record"
    emp_id=fields.Many2one("office_employee",string="Id" ,required=True)
    emp_name=fields.Char(related="emp_id.emp_name",string="Name")
    dept=fields.Char(related="emp_id.dept_id.dept_name",string="Dept Name")
    emp_cno=fields.Integer(string="Co. Number",required=True);
    emp_mail=fields.Char(string="Email",required=True);
    emp_add=fields.Char(string="Address",required=True);
    emp_aad_id=fields.Char(string="Aadhar Number",required=True);
    emp_bank=fields.Integer(string="Bank account ",required=True);
    emp_photo=fields.Image(string="Image",required=True);
    emp_doc1=fields.Binary(string="Employee's Document (Doc is required to get verified)");
    emp_dob=fields.Date(string="DOB",required=True);
    age = fields.Char(string='Age', compute='_compute_time', store=True)
    doc_available = fields.Boolean(string="Verified", compute='_compute_doc_available')
    

    @api.depends('emp_dob')
    def _compute_time(self):    
        for record in self:
            if record.emp_dob:
                today = date.today()
                temp_age= fields.Date.from_string(record.emp_dob)
                new_age = today.year - temp_age.year - ((today.month, today.day) < (temp_age.month, temp_age.day))
                record.age= " %s years" % new_age
                    
            else:
                record.age = " %s years" % 0
    @api.depends('emp_doc1')
    def _compute_doc_available(self):
        for record in self:
            record.doc_available = bool(record.emp_doc1)
