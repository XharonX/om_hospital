from odoo import fields, models, api


class PatientTags(models.Model):
    _name = 'patient.tag'
    _description = "Patient RFID Tag"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    color = fields.Integer("Color Picker")



