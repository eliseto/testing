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
        ('notinvoice', 'No aplica factura'),
        ('no', 'Nothing to Invoice')
        ], string='Invoice Status', compute='_get_invoice_status', store=True, compute= 'compute_fields_nothing')
    nothing_invoice = fields.Boolean(string="No Facturar", default=False)

    @api.depends('nothing_invoice')
    def compute_fields_nothing(self):
        for rec in self:
            if rec.nothing_invoice:
                rec.invoice_status =('notinvoice')
            else:
                pass

    #def action_confirm(self):
    #    super().action_confirm()
    #    if self.nothing_invoice:
    #        self.write ({'invoice_status':'notinvoice'})
    #    else:
    #        pass