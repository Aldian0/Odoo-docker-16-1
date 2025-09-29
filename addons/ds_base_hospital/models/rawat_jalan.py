from odoo import models, fields, api

class DsRawatJalan(models.Model):
    _name = 'ds.rawat.jalan'
    _description = 'Ds Rawat Jalan Pasien'

    no_kunjungan    = fields.Char(string='Nomor Kunjungan', required=True, copy=False, readonly=True, default='New')
    tanggal         = fields.Date(string='Tanggal Kunjungan', default=fields.Date.today)

    pasien_id       = fields.Many2one('ds.pasien', string='Pasien', required=True)
    poli_id         = fields.Many2one('ds.poli', string='Poli', required=True)
    dokter_id       = fields.Many2one('res.users', string='Dokter', domain="[('is_dokter','=',True)]", required=True)
    user_id         = fields.Many2one('res.users', string='User', required=True)
    rawat_inap_id   = fields.One2many('ds.rawat.inap', 'rawat_jalan_id', string="Rawat Inap")

    keluhan         = fields.Text(string='Keluhan')
    diagnosis_awal  = fields.Text(string='Diagnosis Awal')
    rujukan         = fields.Selection([
        ('lanjutan', 'Pemeriksaan Lanjutan'),
        ('rawat_inap', 'Rawat Inap'),
        ('tidak', 'Tidak Dirujuk')
    ], string='Rujukan', default='tidak')
    rujuk_rawat_inap = fields.Boolean(string="Rujuk ke Rawat Inap")
    tanggal_kunjungan = fields.Datetime(string='Tanggal Kunjungan', default=fields.Datetime.now)

    alergi_ids = fields.One2many(related='pasien_id.alergi_ids', string='Alergi Pasien', readonly=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('ds.rawat_jalan') or 'New'
        return super().create(vals)
