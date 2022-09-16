from asyncore import write
from odoo import api, fields, models,_

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    nothing_toinvoice = fields.Boolean(string="No aplica factura", default = False)

    if nothing_toinvoice:
        write({
            'invoice_status':'no'
        })
