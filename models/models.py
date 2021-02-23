# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tareasPen(models.Model):
    _name = 'tareas.pend'
    _description = 'Lista tareas'
    name = fields.Char('Descripción', required=True)
    is_done = fields.Boolean('Está hecha?')
    active = fields.Boolean('Activa?', default=True)

    @api.multi
    def do_toggle_fet(self):
        for tarea in self:
            tarea.is_done = not tarea.is_done
        return True

    @api.multi
    def do_clear_fet(self):
        fets = self.search([('is_done', '=', True)])
        fets.write({'active': False})
        return True
