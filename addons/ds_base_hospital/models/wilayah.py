from odoo import models, fields, api, _

class WilayahPropinsi(models.Model):
    _name = 'wilayah.propinsi'
    _description = 'Propinsi'

    name = fields.Char(string="Nama Propinsi", required=True)

class WilayahKota(models.Model):
    _name = 'wilayah.kota'
    _description = 'Kota/Kabupaten'

    name = fields.Char(string="Nama Kota", required=True)
    propinsi_id = fields.Many2one('wilayah.propinsi', string="Propinsi", required=True)

class WilayahKabupaten(models.Model):
    _name = 'wilayah.kabupaten'
    _description = 'Kabupaten'

    name = fields.Char(string="Nama Kabupaten", required=True)
    kota_id = fields.Many2one('wilayah.kota', string="Kota", required=True)

class WilayahKecamatan(models.Model):
    _name = 'wilayah.kecamatan'
    _description = 'Kecamatan'

    name = fields.Char(string="Nama Kecamatan", required=True)
    kabupaten_id = fields.Many2one('wilayah.kabupaten', string="Kabupaten", required=True)

class WilayahDesa(models.Model):
    _name = 'wilayah.desa'
    _description = 'Desa'

    name = fields.Char(string="Nama Desa", required=True)
    kecamatan_id = fields.Many2one('wilayah.kecamatan', string="Kecamatan", required=True)


