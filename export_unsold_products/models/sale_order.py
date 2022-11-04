import csv

from odoo import models


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    """
    Inherit sale order model to get all those product variants which has not been sold yet. 
    """

    def export_unsold_products(self):
        ordered_products = [o.product_id.id for o in self.env['sale.order.line'].sudo().search([], order='id ASC')]
        product_variant_ids = [product for product in self.env['product.product'].sudo().search([], order='id ASC')]
        product_list = []

        for product in product_variant_ids:
            if product.id not in ordered_products:
                external_id = self.env['ir.model.data'].sudo().search(
                    [('model', '=', 'product.product'), ('res_id', '=', product.id)])
                external_id_name = str(external_id.module) + '.' + external_id.name
                product_list.append(
                    [external_id_name, product.name, product.default_code if product.default_code else ''])

        header = ['External id', 'Name', 'Internal Reference']

        with open('unsold_product.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(product_list)
