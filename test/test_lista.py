# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase

class TestLista(TransactionCase):

    def test_create(self):
        "Crear tarea simple"
        Lista = self.env['tareas.pend']
        tarea = Lista.create({'name': 'Test1'})
        self.assertEqual(tarea.is_done,False)

        #cambia estado test

        tarea.do_toggle_fet()
        self.assertTrue(tarea.is_done)

        #limpiar tareas hechas

        Lista.do_clear_fet()
        self.assertFalse(tarea.active)