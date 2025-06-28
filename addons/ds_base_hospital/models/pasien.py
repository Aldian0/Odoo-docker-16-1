from odoo import models, fields, api


class DsPAsien(models.Model):
    _name = 'ds.pasien'
    _description = 'Ds Pasien'



    name = fields.Char(string='Nama Lengkap', required=True)
    age = fields.Integer(string='Umur')
    no_rm = fields.Char(string='No. Rekam Medis')
    nik = fields.Char(string='NIK', size=16)
    jenis_kelamin = fields.Selection([('male','Male'),('female','Female')], string='Jenis Kelamin')
    tanggal_lahir = fields.Date(string='Tanggal Lahir')
    gol_darah = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O')
    ], string='Golongan Darah')
    alamat = fields.Text(string='Alamat')
    status = fields.Selection([
        ('aktif', 'Aktif'),
        ('nonaktif', 'Nonaktif')
    ], string='Status', default='aktif')
    telepon = fields.Char(string='Nomor Telepon')
    email = fields.Text(string='Email')
