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

    # 🔗 Related fields dari ds.pasien
    no_rekam_medis  = fields.Char(related='pasien_id.no_rm', string="No Rekam Medis", store=True, readonly=True)
    nama_pasien     = fields.Char(related='pasien_id.name', string="Nama Pasien", store=True, readonly=True)
    tanggal_lahir   = fields.Date(related='pasien_id.tanggal_lahir', string="Tanggal Lahir", store=True, readonly=True)
    jenis_kelamin   = fields.Selection(related='pasien_id.jenis_kelamin', string="Jenis Kelamin", store=True, readonly=True)
    golongan_darah  = fields.Selection(related='pasien_id.gol_darah', string="Golongan Darah", store=True, readonly=True)
    no_telp         = fields.Char(related='pasien_id.telepon', string="No. Telepon", store=True, readonly=True)
    email           = fields.Char(related='pasien_id.email', string="Email", store=True, readonly=True)
    alamat          = fields.Text(related='pasien_id.alamat', string="Alamat", store=True, readonly=True)

    tindakan_medis_ids = fields.One2many('ds.tindakan.medis', 'rawat_inap_id', string='Tindakan Medis')
    # alergi_ids = fields.One2many(related='pasien_id.alergi_ids', string='Alergi Pasien', readonly=True, store=True)
    alergi_ids = fields.Many2many(
    'ds.alergi.pasien',
    'ds_rawat_inap_alergi_rel',     # nama tabel relasi
    'rawat_inap_id',                # kolom di tabel relasi yang mengacu ke ds.rawat.inap
    'alergi_id',                    # kolom di tabel relasi yang mengacu ke ds.alergi.pasien
    string='Alergi Pasien',
    readonly=True
)
    
@api.depends('pasien_id')
def _compute_alergi_ids(self):
        for rec in self:
            rec.alergi_ids = rec.pasien_id.alergi_ids if rec.pasien_id else False



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

class DsAlergiPasien(models.Model):
    _name = 'ds.alergi.pasien'
    _description = 'Ds Alergi Pasien'
    _rec_name = 'name_alergi'

    pasien_id = fields.Many2one('ds.pasien', string="Pasien", required=True, ondelete='cascade')
    name_alergi = fields.Char(string="Nama Alergi",required=True)
    tingkat_keparahan = fields.Selection([
        ('ringan', 'Ringan'),
        ('sedang', 'Sedang'),
        ('berat', 'Berat'),
        ('fatal', 'Fatal'),
    ], string="Tingkat Keparahan", default='ringan')
    reaksi = fields.Text(string="Reaksi")
    catatan = fields.Text(string="Catatan")