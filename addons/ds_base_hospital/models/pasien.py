from odoo import models, fields, api


# Data pasien tambahan, extend res.partner (data pasien (NIK, nama, tanggal lahir, no. RM, dll.)


class DsPAsien(models.Model):
    _name = 'ds.pasien'
    _description = 'Ds Pasien'

# class DsPasien(models.Model):
#     _name = 'ds.Pasien'
#     _description = 'Ds Pasien'

    name = fields.Char(string='Nama Lengkap', required=True)
    nik = fields.Char(string='NIK', size=16)
    gender = fields.Selection([('male','Male'),('female','Female')], string='Jenis Kelamin')
    birth_date = fields.Date(string='Birth Date')
    phone = fields.Char(string='Nomor Telepon')
    address = fields.Text(string='Alamat')
