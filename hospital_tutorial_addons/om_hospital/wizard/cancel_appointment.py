from odoo import fields, models, api


class CancelAppointment(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = "Cancel Appointment Wizard"

    appointment_id = fields.Many2one('hospital.appointment')
    reason = fields.Text()

    def action_cancel(self):
        for ap in self:
            ap.appointment_id.state = 'cancel'
            # need to redirect to list view of appointments

    def cron_add_appointment(self):
        ap = self.env['hospital.appointment'].sudo().search([])