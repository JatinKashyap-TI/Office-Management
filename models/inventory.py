from odoo import models,fields
class Inventory(models.Model):
    _name="office_inventory"
    prod_name=fields.Char(string="Product Name",required=True);
    prod_id=fields.Char(string="Product Id",required=True);
    warranty_status=fields.Selection([('undewarranty',"Under Warranty"),('out','Out of Warranty')],string="Warranty status",required=True)
    emp_id=fields.Many2one("office_employee",string="Emp Id",required=True);
    # emp_name=fields.Char(related="emp_id.emp_name",readonly=True,store=True)
    emp_name = fields.Char(string="Emp Name", related="emp_id.emp_name", store=True, readonly=True)
