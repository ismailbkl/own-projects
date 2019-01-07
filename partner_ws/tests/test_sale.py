# -*- coding: utf-8 -*-
# (C) 2011 Smile (<http://www.smile.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from datetime import date

from odoo.tests.common import TransactionCase


class TestSale(TransactionCase):

    def setUp(self):
        super(TestSale, self).setUp()

    def test_00_check_sale_order_of_partner_exist(self):
        """
            Test check_sale_order_of_partner method
            We try to check if there is a sale order of this partner
            It returns a recordset
        """
        partner_id = self.env.ref('base.res_partner_3').id
        sale = self.env['sale.order'].check_sale_order_of_partner_existance(partner_id)
        self.assertNotIsInstance(sale, dict)

    def test_01_check_sale_order_of_partner_not_exist(self):
        """
            Test check_sale_order_of_partner method
            We try to check the method to return warning
            It returns a dict warning
        """
        partner_id = self.env.ref('base.res_partner_address_16').id
        sale = self.env['sale.order'].check_sale_order_of_partner_existance(partner_id)
        self.assertIn('warning', sale)

    def test_02_get_filtered_sales(self):
        """
            Test get_filtered_sales method
            We try to check the method to return dict
            It returns a dict dict contains sale orders infos
        """
        partner_id = self.env.ref('base.res_partner_3').id
        sale = self.env['sale.order'].get_filtered_sales(partner_id, str(date.today().year)+'-01-01',
                                                         str(date.today().year)+'-11-30', ['done', 'sale'])
        self.assertIsInstance(sale, dict)

    def test_03_get_sale_order_infos(self):
        """
            Test get_sale_order_infos method
            We try to check the method to return all infos of sale
            It returns a dict contains all sale infos
        """
        partner_id = self.env.ref('base.res_partner_3').id
        sale = self.env['sale.order'].get_sale_order_infos(partner_id, str(date.today().year)+'-01-01',
                                                           str(date.today().year)+'-11-30')
        self.assertIsInstance(sale, dict)

    def test_04_check_get_sale_order_infos_with_states_not_exists(self):
        """
            Test get_sale_order_infos method
            It returns a dict contains partner infos with warning_states_not_exists element
        """
        partner_id = self.env.ref('base.res_partner_3').id
        sale = self.env['sale.order'].get_sale_order_infos(partner_id, str(date.today().year)+'-01-01',
                                                           str(date.today().year)+'-11-30', ['non_existent'])
        self.assertIn('warning_states_not_exists', sale)
