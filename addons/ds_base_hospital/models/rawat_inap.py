from odoo import models, fields, api

class DsRawatInap(models.Model):
    _name = 'ds.rawat.inap'
    _description = 'Ds Rawat Inap'

    pasien_id       = fields.Many2one('ds.pasien', string="Pasien", required=True)
    kamar_id        = fields.Many2one('ds.kamar', string="Kamar", required=True)
    rawat_jalan_id  = fields.Many2one('ds.rawat.jalan', string="Asal Rawat Jalan")
    tempat_tidur    = fields.Char(string="Tempat Tidur", required=True)
    tanggal_masuk   = fields.Datetime(string="Tanggal Masuk", default=fields.Datetime.now)
    tanggal_keluar  = fields.Datetime(string="Tanggal Keluar")
    tindakan_ids    = fields.One2many('ds.tindakan.medis', 'rawat_inap_id', string="Tindakan Medis")
    catatan_dokter  = fields.Text(string="Catatan Dokter")
    catatan_perawat = fields.Text(string="Catatan Perawat")
    keluhan         = fields.Text(string='Keluhan')
    diagnosis_awal  = fields.Text(string='Diagnosis Awal')
    rujukan         = fields.Selection([
        ('lanjutan', 'Pemeriksaan Lanjutan'),
        ('rawat_inap', 'Rawat Inap'),
        ('tidak', 'Tidak Dirujuk')
    ], string='Rujukan', default='tidak')
    kondisi_pasien = fields.Selection([
    ('stabil', 'Stabil'),
    ('kritis', 'Kritis'),
    ('meningkat', 'Meningkat'),
    ('menurun', 'Menurun'),
    ], string="Kondisi Pasien", default='stabil')

    tindakan_medis_ids = fields.One2many('ds.tindakan.medis', 'rawat_inap_id', string='Tindakan Medis')
    alergi_ids = fields.One2many(related='pasien_id.alergi_ids', string='Alergi Pasien', readonly=True)


class DsTindakanMedis(models.Model):
    _name = 'ds.tindakan.medis'
    _description = 'Ds Tindakan Medis'

    pasien_id       = fields.Many2one('ds.pasien', string="Pasien", required=True)
    dokter_id       = fields.Many2one('ds.dokter', string="Dokter")
    perawat_id      = fields.Many2one('res.users', string="Perawat")
    rawat_inap_id   = fields.Many2one('ds.rawat.inap', string="Rawat Inap", required=True, ondelete='cascade')
    tanggal         = fields.Datetime(string="Tanggal", default=fields.Datetime.now)
    tindakan        = fields.Text(string="Tindakan")
    deskripsi       = fields.Text(string="Catatan")