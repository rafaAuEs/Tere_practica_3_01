# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lista_tareas(models.Model):
    # El _name define el nombre de la tabla en la DB (odoo la llamará lista_tareas_lista_tareas)
    _name = 'lista_tareas.lista_tareas'
    _description = 'Modelo de la Lista de Tareas'

    # --- CAMPOS BÁSICOS ---
    tarea = fields.Char(string='Tarea', required=True)
    prioridad = fields.Integer(string='Prioridad', default=10)
    urgente = fields.Boolean(string='¿Es Urgente?', compute="_value_urgente", store=True)
    realizada = fields.Boolean(string='Completada')

    fecha_limite = fields.Date(string='Fecha Límite')
    descripcion = fields.Html(string='Descripción Detallada')
    
    # Campo de estado
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('en_progreso', 'En Progreso'),
        ('finalizado', 'Finalizado'),
    ], string='Estado', default='borrador')

    # Lógica del campo calculado
    @api.depends('prioridad')
    def _value_urgente(self):
        for record in self:
            # Si la prioridad es mayor a 10, marcamos como urgente
            if record.prioridad > 10:
                record.urgente = True
            else:
                record.urgente = False