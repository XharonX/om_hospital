from odoo import fields, models, api


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'
    _rec_name = 'ref'
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    gender = fields.Selection(related='patient_id.gender', readonly=False)
    ref = fields.Char('Reference', required=True, tracking=True)
    appointment_time = fields.Datetime(string='Appointment time:', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking', default=fields.Date.context_today)
    prescription = fields.Html(string="Prescription")
    doctor_id = fields.Many2one('res.users', string='Doctor')
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', 'Pharmacy')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority", tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Canceled')], string="Status", tracking=True)

    def __str__(self):
        print(self)
        return f"{self.patient_id.name}'s appointment"

    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_do_cancel(self):
        self.write({'state': 'cancel'})

    def action_do_done(self):
        self.write({'state': 'done'})

    def action_do_consultation(self):
        return self.write({'state': 'in_consultation'})


class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacy Line"

    product_id = fields.Many2one('product.product', string="Product", required=True)
    qty = fields.Integer('Quantity', default=1)
    unit_price = fields.Float(string='Price', related='product_id.list_price', readonly=False)
    appointment_id = fields.Many2one('hospital.appointment')
    total_price = fields.Float(compute="_get_total_price")

    @api.depends('unit_price', 'qty')
    def _get_total_price(self):
        for appointment in self:
            appointment.total_price = appointment.unit_price * appointment.qty
