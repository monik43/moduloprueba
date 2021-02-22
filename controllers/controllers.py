# -*- coding: utf-8 -*-
from odoo import http

# class Moduloprueba(http.Controller):
#     @http.route('/moduloprueba/moduloprueba/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/moduloprueba/moduloprueba/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('moduloprueba.listing', {
#             'root': '/moduloprueba/moduloprueba',
#             'objects': http.request.env['moduloprueba.moduloprueba'].search([]),
#         })

#     @http.route('/moduloprueba/moduloprueba/objects/<model("moduloprueba.moduloprueba"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('moduloprueba.object', {
#             'object': obj
#         })