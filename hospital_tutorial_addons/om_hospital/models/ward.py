# from odoo import fields, models, api
#
#
# class Department(models.Model):
#     _name = 'hospital.department'
#     _description = 'Hospital Department'
#
#     name = fields.Char('Department', required=True)
#     ward_ids = fields.One2many('hospital.ward', 'department_id', 'Ward')
#     # doctor_ids = fields.One2many('hospital.doctor', string="Doctor")
#
#
# class Ward(models.Model):
#     _name = "hospital.ward"
#     _description = "Hospital Ward"
#
#     name = fields.Char(string="Room NO: ")
#     type = fields.Selection([
#         ('A1', 'A1'),
#         ('B1', 'B1'),
#         ('C', 'C'),
#         ('G', 'G'),
#     ])
#     meal_allowance = fields.Boolean(default=False)
#
#     department_id = fields.Many2one('hospital.department', string='Department')
#     patient_ids = fields.Many2many('hospital.patient', string="Patients", related=True)
