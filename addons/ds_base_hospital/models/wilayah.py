from odoo import models, fields, api, _

class WilayahPropinsi(models.Model):
    _name = 'wilayah.propinsi'
    _description = 'Propinsi'

    name = fields.Char(string="Nama", required=True)

    # kota_ids = fields.One2many(comodel_name='wilayah.propinsi', inverse_name='propinsi_id', string='Daftar Kota')    

class WilayahKota(models.Model):
    _name = 'wilayah.kota'
    _description = 'Kota'

    name = fields.Char(string="Nama Kota", required=True)

    propinsi_id = fields.Many2one(comodel_name='wilayah.propinsi', string="Propinsi", required=True)
    # kecamatan_ids = fields.One2many(comodel_name='wilayah.kecamatan', inverse_name='kota_id', string='Daftar Kecamatan')

class WilayahKecamatan(models.Model):
    _name = 'wilayah.kecamatan'
    _description = 'Kecamatan'

    name = fields.Char(string="Nama Kecamatan", required=True)

    kota_id = fields.Many2one(comodel_name='wilayah.kota', string="Kota", required=True)
    # desa_ids = fields.One2many(comodel_name='wilayah.desa', inverse_name='kecamatan_id', string='Daftar Desa')

class WilayahDesa(models.Model):
    _name = 'wilayah.desa'
    _description = 'Desa'

    name = fields.Char(string="Nama Desa", required=True)

    kecamatan_id = fields.Many2one(comodel_name='wilayah.kecamatan', string="Kecamatan", required=True)


