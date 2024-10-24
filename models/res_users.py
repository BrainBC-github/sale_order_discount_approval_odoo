# -*- coding: utf-8 -*-
 
from odoo import models, fields


class ResUsers(models.Model):
    """This is used to inherit 'res.users' to add new fields"""
    _inherit = 'res.users'

    is_discount_control = fields.Boolean(string='Discount Control',
                                         help='Which is used to identify isit '
                                              'for discount control')
    allow_discount = fields.Float(string='Allow Discount',
                                  help='Allowed discount percentage')
