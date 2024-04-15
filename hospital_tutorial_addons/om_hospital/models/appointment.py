from odoo import fields, models, api


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'

    patient_id = fields.Many2one('hospital.patient', string="Patient", default=fields.Datetime.now)
    gender = fields.Selection((
        ['male', 'Male'],
        ['Female', 'Female'],
    ), related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment time:', default=fields.Date.context_today)
    booking_date = fields.Date(string='Booking')

    def __str__(self):
        print(self)
        return f"{self.patient_id.name}'s appointment"
