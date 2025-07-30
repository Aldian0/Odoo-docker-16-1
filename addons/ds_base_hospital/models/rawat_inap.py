from odoo import models, fields, api

class DsRawatInap(models.Model):
    _name = 'ds.rawat.inap'
    _description = 'Ds Rawat Inap'

    pasien_id       = fields.Many2one('ds.pasien', string="Pasien", required=True)
    kamar_id        = fields.Many2one('ds.kamar', string="Kamar", required=True)
    tempat_tidur    = fields.Char(string="Tempat Tidur", required=True)
    tanggal_masuk   = fields.Datetime(string="Tanggal Masuk", default=fields.Datetime.now)
    tanggal_keluar  = fields.Datetime(string="Tanggal Keluar")
    kondisi_pasien  = fields.Text(string="Monitoring Kondisi Pasien")
    tindakan_ids    = fields.One2many('ds.tindakan.medis', 'rawat_inap_id', string="Tindakan Medis")
    catatan_dokter  = fields.Text(string="Catatan Dokter")
    catatan_perawat = fields.Text(string="Catatan Perawat")


class DsTindakanMedis(models.Model):
    _name = 'ds.tindakan.medis'
    _description = 'Ds Tindakan Medis'

    rawat_inap_id   = fields.Many2one('ds.rawat.inap', string="Rawat Inap", required=True, ondelete='cascade')
    tanggal         = fields.Datetime(string="Tanggal", default=fields.Datetime.now)
    tindakan        = fields.Text(string="Tindakan")
    dokter_id       = fields.Many2one('ds.dokter', string="Dokter")
    perawat_id      = fields.Many2one('res.users', string="Perawat")