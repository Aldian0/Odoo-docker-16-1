from odoo import models, fields, api



class DsPAsien(models.Model):
    _name = 'ds.pasien'
    _description = 'Ds Pasien'
    

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

    rawat_jalan_ids     = fields.One2many('ds.rawat.jalan', 'pasien_id', string="Rawat Jalan")
    rawat_inap_ids      = fields.One2many('ds.rawat.inap', 'pasien_id', string="Rawat Inap")
    kunjungan_ids       = fields.One2many('ds.kunjungan', 'pasien_id', string="Riwayat Kunjungan")
    alergi_ids          = fields.One2many('ds.alergi.pasien', 'pasien_id', string="Alergi Pasien")
    tindakan_medis_ids  = fields.One2many('ds.tindakan.medis', 'pasien_id', string="Tindakan Medis")

    @api.onchange('propinsi_id')
    def _onchange_propinsi(self):
      if not self.propinsi_id or not self.propinsi_id.exists():
        self.kota_id = False
        self.kabupaten_id = False
        self.kecamatan_id = False
        self.desa_id = False
    
    @api.onchange('kota_id')
    def _onchange_kota(self):
      if not self.kota_id or not self.kota_id.exists():
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


    

class DsAlergiPasien(models.Model):
    _name = 'ds.alergi.pasien'
    _description = 'Ds Alergi Pasien'

    name_alergi = fields.Char(string='Jenis Alergi', required=True)
    tingkat_keparahan = fields.Selection([
        ('ringan', 'Ringan'),
        ('sedang', 'Sedang'),
        ('berat', 'Berat')
    ], string='Tingkat Keparahan', required=True)
    reaksi = fields.Text(string='Reaksi yang Terjadi')
    catatan = fields.Text(string='Catatan Tambahan')
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

    # pasien_id = fields.Many2one('ds.pasien', string='Pasien', required=True)
    name = fields.Char(string='Nama Poli', required=True)
    kode_poli = fields.Char(string='Kode Poli', required=True)
    spesialisasi = fields.Selection([
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
    ], string='Spesialisai Dokter')
    deskripsi = fields.Text(string='Deskripsi')
    aktif = fields.Boolean(string='Aktif', default=True)
    dokter_ids = fields.One2many('ds.dokter', 'poli_id', string='Dokter')
    jadwal_praktek = fields.Selection([
        ('Senin - Jumat', '08:00 - 14:00'),
        ('Sabtu & Minggu', '10:00 - 12:00'),
        ('Setiap Hari', '24 Jam (UGD)')
    ], string='Jadwal Praktek')

class DsDokter(models.Model):
    _name = 'ds.dokter'
    _description = 'Dokter Rumah Sakit'

    name = fields.Char(string='Nama Dokter', required=True)
    spesialisasi = fields.Selection([
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
    ], string='Spesialisai Dokter')
    poli_id = fields.Many2one('ds.poli', string='Poli')
    jadwal_praktek = fields.Selection([
        ('Senin - Jumat', '08:00 - 14:00'),
        ('Sabtu & Minggu', '10:00 - 12:00'),
        ('Setiap Hari', '24 Jam (UGD)')
    ], string='Jadwal Praktek')




