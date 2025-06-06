# -*- coding: utf-8 -*-
# from odoo import http


# class DsBaseHospital(http.Controller):
#     @http.route('/ds_base_hospital/ds_base_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ds_base_hospital/ds_base_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ds_base_hospital.listing', {
#             'root': '/ds_base_hospital/ds_base_hospital',
#             'objects': http.request.env['ds_base_hospital.ds_base_hospital'].search([]),
#         })

#     @http.route('/ds_base_hospital/ds_base_hospital/objects/<model("ds_base_hospital.ds_base_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ds_base_hospital.object', {
#             'object': obj
#         })
