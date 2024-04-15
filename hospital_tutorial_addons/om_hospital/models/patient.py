from odoo import fields, models, api
from datetime import datetime


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name', required=True)
    active = fields.Boolean('Active', default=True)
    ref = fields.Char('Reference', required=True, tracking=True)
    age = fields.Integer(compute='_get_age')
    bod = fields.Date(string='Birth of Date: ', required=True)
    gender = fields.Selection([('male', 'male'), ('female', 'female')], string='Gender', required=True)
    address = fields.Char()
    phone_number = fields.Char()
    blood = fields.Selection([
        ('O+', 'O+'), ('O-', 'O-'),
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
    ], required=True)
    conditions = fields.Char("Medical Condition", tracking=True)
    description = fields.Text("Description")

    def __str__(self):
        return f"{self.name} + ({self.ref})"

    @api.depends('bod')
    def _get_age(self):
        td = datetime.now()
        for patient in self:
            birthdate = patient.bod
            if birthdate:
                birthdate = datetime(birthdate.year, birthdate.month, birthdate.day)
                age = (td - birthdate).days // 356
                patient.age = age
            else:
                patient.age = 1
