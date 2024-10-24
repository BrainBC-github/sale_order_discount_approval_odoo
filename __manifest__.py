# -*- coding: utf-8 -*-
 
{
    'name': 'Sale Order Discount Approval',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Sale Order Discount Approval based on the Allowed discount values',
    'description': """Module for discount approval of sales orders if 
     discount limit exceeded of allowed discount of user.""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': [
        'sale_management',
    ],
    'data': [
        'security/sale_order_discount_approval_odoo_groups.xml',
        'view/res_users_views.xml',
        'view/sale_order_views.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
