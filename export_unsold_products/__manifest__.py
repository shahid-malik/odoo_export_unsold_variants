# -*- coding: utf-8 -*-
{
    'name': "Product variants cleaning module",

    'summary': """
        Export List off product variants that are not sold yet on a single button click.

        
        """,

    'description': """
        This module is developed for client specially and does not work for all sceanrios. Requirements were very specific.

        This module is meant to clean unused product variants. To remove product variant is a 5 way process.
                
        Step 1: Export all variants of a Product that are not sold yet and have no reference in sale order.
        Step 2: Add any internal reference i.e 'need to be deleted' which can differentiate it from other product variants.
        Step 3: Import back to odoo
        Step 4: Search by internal referenced i.e 'Need to be deleted'
        step 5: Manually delete the product variants from search results
    """,

    'author': "Mediod Consulting",
    'website': "http://www.mediodconsulting.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'views/sale_order.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}