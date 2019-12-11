# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Series(models.Model):
    _name = 'facturacion.series'
    _description = 'Series de documentos'

    name = fields.Char(string='Nombre de la Serie')
    prefix = fields.Char(string='Prefijo de la Serie')
    document_type = fields.Selection([('01','Factura'),
    ('03','Boleta'),
    ('07','Nota de Crédito'),
    ('08','Nota de Debito')
    ])
    active = fields.Boolean(string='Estado de la Serie',default= True)