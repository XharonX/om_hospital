from odoo import models, fields, api


class Doctor(models.Model):
    # _name = 'hospital.doctor'
    _description = 'Hospital Doctor'
    _inherit = 'res.users'

    name = fields.Char('Doctor', required=True)
    specialty_ids = fields.Many2many('hospital.specialty')
    experience_years = fields.Integer('Years of Experience')
    qualifications = fields.Text()


class Specialty(models.Model):
    _name = 'hospital.specialty'

    name = fields.Char()
    description = fields.Text()