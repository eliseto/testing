# -*- coding: utf-8 -*-

from asyncore import write
from odoo import api, fields, models,_


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    show_line = fields.Boolean(string="Visible", default=True, store=True)
    
class SaleOrder(models.Model):
    _inherit='sale.order'
    invoice_status = fields.Selection([
        ('upselling', 'Upselling Opportunity'),
        ('invoiced', 'Fully Invoiced'),
        ('to invoice', 'To Invoice'),
        ('not apply invoice', 'No aplica factura'),
        ('no', 'Nothing to Invoice')
        ], string='Invoice Status', compute='_get_invoice_status', store=True)
    nothing_invoice = fields.Boolean(string="no facturar", default=False)
    def action_confirm(self):
        super().action_confirm()
        if self.nothing_invoice:
            return {'invoice_status':'not apply invoice'}