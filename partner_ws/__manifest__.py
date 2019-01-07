# -*- coding: utf-8 -*-
# (C) 2018 Smile (<http://www.smile.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Partner WS",

    'summary': """
       Partner Web Service
                """,

    'description': """
            Partner Web Service  
                    """,

    'author': "Smile SA",
    'website': "http://www.smile.eu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase',
                'sale_management',
                'base',
                'account',
                'stock',
                'common',
                'contacts'],
}