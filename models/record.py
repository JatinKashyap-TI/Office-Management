from odoo import models,fields
class Record(models.Model):
    _name="office_record"
    emp_id=fields.Many2one("office_employee",string="Employee id" ,required=True)
    emp_cno=fields.Integer(string="Employee Contact Number",required=True,size=10);
    emp_mail=fields.Char(string="Employee Email",required=True);
    emp_add=fields.Char(string="Employee Address",required=True);
    emp_aad_id=fields.Char(string="Aadhar Number",required=True);
    emp_bank=fields.Integer(string="Bank account number",required=True,max_width=1920, max_height=1920);
    emp_photo=fields.Image(string="Employee's photo",required=True);
    emp_doc1=fields.Binary(string="Employee's Document (if any)");