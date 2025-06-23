from odoo import models, fields, api
# from odoo.exceptions import ValidationError

class DsPAsien(models.Model):
    _name = 'ds.pasien'
    _description = 'Ds Pasien'



    name = fields.Char(string='Nama Lengkap', required=True)
    age = fields.Integer(string='Umur')
    nik = fields.Char(string='NIK', size=16)
    gender = fields.Selection([('male','Male'),('female','Female')], string='Jenis Kelamin')
    birth_date = fields.Date(string='Tanggal Lahir')
    phone = fields.Char(string='Nomor Telepon')
    address = fields.Text(string='Alamat')
