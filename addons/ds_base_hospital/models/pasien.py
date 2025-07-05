from odoo import models, fields, api
from odoo.exceptions import ValidationError

class DsPAsien(models.Model):
    _name = 'ds.pasien'
    _description = 'Ds Pasien'



    name = fields.Char(string='Rumah Sakit', required=True)
    name_id = fields.Char(string='Nama Lengkap', required=True)
    image = fields.Image("Foto Pasien")
    age = fields.Integer(string='Umur')
    no_rm = fields.Char(string='No. Rekam Medis', readonly=True, copy=False, default='New')
    nik = fields.Char(string='NIK', size=16)
    jenis_kelamin = fields.Selection([('male','Laki-Laki'),('female','Perempuan')], string='Jenis Kelamin')
    tanggal_lahir = fields.Date(string='Tanggal Lahir')
    gol_darah = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O')
    ], string='Golongan Darah')
    status_perkawinan = fields.Selection([
        ('single', 'Belum Menikah'),
        ('married', 'Menikah'),
        ('divorce', 'Cerai'),
    ], string="Status Pernikahan")
    tempat_lahir = fields.Char(string="Tempat Lahir")
    alamat = fields.Text(string='Alamat')
    status = fields.Selection([
        ('aktif', 'Aktif'),
        ('nonaktif', 'Nonaktif')
    ], string='Status', default='aktif')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Terkonfirmasi'),
        ('proses', 'Diproses'),
        ('done', 'Selesai'),
    ], default='draft', string="Status")

    kota_id = fields.Char(string="Kota")
    kabupaten_id = fields.Char(string="Kabupaten")
    kecamatan_id = fields.Char(string="Kecamatan")
    desa_id = fields.Char(string="Desa")

    telepon = fields.Char(string='Nomor Telepon')
    email = fields.Char(string='Email')
    alamat = fields.Text(string='Alamat')
    kota = fields.Char(string='Kota')
    provinsi = fields.Char(string='Provinsi')
    kode_pos = fields.Char(string='Kode Pos')

    kontak_darurat_nama = fields.Char(string='Nama Kontak Darurat')
    kontak_darurat_telepon = fields.Char("Telepon Darurat")
    kontak_darurat_hubungan = fields.Char("Hubungan")

    penyedia_asuransi = fields.Char("Asuransi")
    nomor_asuransi = fields.Char("Nomor Asuransi")
    tanggal_registrasi = fields.Date("Tanggal Registrasi", default=fields.Date.today)
    catatan = fields.Text("Catatan")

    @api.model
    def create(self, vals):
        if vals.get('no_rm', 'New') == 'New':
            vals['no_rm'] = self.env['ir.sequence'].next_by_code('ds.pasien') or 'RM/00001'
        return super().create(vals)
    
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_progress(self):
        for rec in self:
            rec.state = 'proses'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

# class DsWilayah (models.Models):
#     _name = 'wilayah.kota'
#     _description = 'Kota'

#     kota_id = fields.Many2one('wilayah.kota', string="Kota")
#     kabupaten_id = fields.Many2one('wilayah.kabupaten', string="Kabupaten")
#     kecamatan_id = fields.Many2one('wilayah.kecamatan', string="Kecamatan")
#     desa_id = fields.Many2one('wilayah.desa', string="Desa")
