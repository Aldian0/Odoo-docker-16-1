from odoo import models, fields, api



class DsPAsien(models.Model):
    _name = 'ds.pasien'
    _description = 'Ds Pasien'
    # _inherit     = ['mail.thread', 'mail.activity.mixin']

    READONLY_STATES         = {'proses': [('readonly', True)], 'done': [('readonly', True)]}
    STATE = [
        ('draft', 'Draft'),
        ('proses', 'Proses'),
        ('done', 'Done'),
    ]




    name                    = fields.Char(string='Rumah Sakit', required=True)
    name_id                 = fields.Char(string='Nama Lengkap', required=True)
    tempat_lahir            = fields.Char(string="Tempat Lahir")
    email                   = fields.Char(string='Email')

    kontak_darurat_nama     = fields.Char(string='Nama Kontak Darurat')
    kontak_darurat_telepon  = fields.Char(string="Telepon Darurat")
    kontak_darurat_hubungan = fields.Char(string="Hubungan")
    nomor_asuransi          = fields.Char(string="Nomor Asuransi")

    propinsi_id             = fields.Many2one('wilayah.propinsi', string="Provinsi", store=True)
    kota_id                 = fields.Many2one('wilayah.kota', string="Kota", store=True)
    kabupaten_id            = fields.Many2one('wilayah.kabupaten', string="Kabupaten", store=True)
    kecamatan_id            = fields.Many2one('wilayah.kecamatan', string="Kecamatan", store=True)
    desa_id                 = fields.Many2one('wilayah.desa', string="Desa", store=True)

    alamat                  = fields.Text(string='Alamat', store=True)

    age                     = fields.Integer(string='Umur')
    no_rm                   = fields.Char(string='No. Rekam Medis', readonly=True, copy=False, default='New')
    nik                     = fields.Char(string='NIK', size=16)
    kode_pos                = fields.Char(string='Kode Pos')
    telepon                 = fields.Char(string='Nomor Telepon')

    tanggal_registrasi      = fields.Date(string="Tanggal Registrasi", default=fields.Date.today)
    catatan                 = fields.Text(string="Catatan")

    jenis_kelamin = fields.Selection([
        ('male','Laki-Laki'),
        ('female','Perempuan')
        ], string='Jenis Kelamin')
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
    status = fields.Selection([
        ('aktif', 'Aktif'),
        ('nonaktif', 'Nonaktif')
    ], string='Status', default='aktif')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Dikonfirmasi'),
        ('proses', 'Diproses'),
        ('done', 'Selesai'),
    ], default='draft', string="Status")
    penyedia_asuransi = fields.Selection([
        ('allianz', 'Allianz'),
        ('prudential', 'Prudential'),
        ('aia', 'AIA'),
        ('manulife', 'Manulife'),
        ('axa mandiri', 'AXA Mandiri'),
        ('sinarmas msig life', 'Sinarmas MSIG Life'),
        ('bri life', 'BRI Life'),
        ('bps kesehatan', 'BPJS Kesehatan'),
    ], string="Asuransi")

    @api.onchange('propinsi_id')
    def _onchange_propinsi(self):
        self.kota_id = False
        self.kabupaten_id = False
        self.kecamatan_id = False
        self.desa_id = False


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

class DsDataPasien(models.Model):
    _name = 'ds.data.pasien'
    _description = 'Ds Data Pasien'

    name_id                 = fields.Char(string='Nama Lengkap', required=True)
    no_rm                   = fields.Char(string='No. Rekam Medis')
    nik                     = fields.Char(string='NIK', size=16)
    jenis_kelamin = fields.Selection([
        ('male','Laki-Laki'),
        ('female','Perempuan')
        ], string='Jenis Kelamin')
    tempat_lahir            = fields.Char(string='Tempat Lahir')
    tanggal_lahir           = fields.Date(string='Tanggal Lahir')
    alamat                  = fields.Text(string='Alamat')
    telepon                 = fields.Char(string='Nomor Telepon')
    email                   = fields.Char(string='Email')
    status = fields.Selection([
        ('aktif', 'Aktif'),
        ('nonaktif', 'Nonaktif')
    ], string='Status', default='aktif')

class DsAlergiPasien(models.Model):
    _name = 'ds.alergi.pasien'
    _description = 'Ds Alergi Pasien'

    name = fields.Char(string='Nama Alergi', required=True)
    deskripsi = fields.Text(string='Deskripsi')
    pasien_id = fields.Many2one('ds.pasien', string='Pasien', required=True)

class DsKunjungan(models.Model):
    _name = 'ds.kunjungan'
    _description = 'Ds Kunjungan'

    pasien_id       = fields.Many2one('ds.pasien', string='Pasien', required=True)
    tanggal         = fields.Date(string='Tanggal Kunjungan', required=True)
    poli_id         = fields.Many2one('ds.poli', string='Poli Tujuan')
    dokter_id       = fields.Many2one('res.users', string='Dokter')
    keluhan         = fields.Text(string='Keluhan')
    diagnosis_awal  = fields.Text(string='Diagnosis Awal')
    rujukan         = fields.Selection([
        ('lanjutan', 'Pemeriksaan Lanjutan'),
        ('rawat_inap', 'Rawat Inap'),
        ('selesai', 'Selesai')
    ], string='Rujukan') 
    upload_hasil_riwayat_kunjungan  = fields.Binary(string='Upload Hasil Gambar')
    keterangan                      = fields.Text(string='Keterangan',  compute='_compute_peringatan')
    

    data_hasil_riwayat_kunjungan_ids    = fields.One2many('ds.kunjungan', 'pasien_id', string='Upload Hasil Riwayat Kunjungan')

class DsPoli(models.Model):
    _name = 'ds.poli'
    _description = 'Data Poli Rumah Sakit'

    pasien_id = fields.Many2one('ds.pasien', string='Pasien', required=True)
    nama_poli = fields.Selection([
        ('Umum', 'Poli Umum'),
        ('Gigi', 'Poli Gigi'),
        ('Anak', 'Poli Anak'),
        ('Kandungan', 'Poli Kandungan'),
        ('Penyakit Dalam', 'Poli Penyakit Dalam'),
        ('Bedah', 'Poli Bedah'),
        ('THT', 'Poli THT'),
        ('Mata', 'Poli Mata'),
        ('Saraf', 'Poli Saraf'),
        ('Kulit dan Kelamin', 'Poli Kulit dan Kelamin')
    ], string='Nama Poli')
    keterangan = fields.Text(string='Keterangan')


# class DsWilayah (models.Models):
#     _name = 'wilayah.kota'
#     _description = 'Kota'

#     kota_id = fields.Many2one('wilayah.kota', string="Kota")
#     kabupaten_id = fields.Many2one('wilayah.kabupaten', string="Kabupaten")
#     kecamatan_id = fields.Many2one('wilayah.kecamatan', string="Kecamatan")
#     desa_id = fields.Many2one('wilayah.desa', string="Desa")
