# -*- coding: utf-8 -*-
# (C) 2011 Smile (<http://www.smile.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from datetime import date

from odoo.tests.common import TransactionCase


class TestPurchase(TransactionCase):

    def setUp(self):
        super(TestPurchase, self).setUp()

    def test_00_check_purchase_order_of_partner_exist(self):
        """
            Test check_purchase_order_of_partner method
            We try to check if there is a purchase order of this partner
            It returns a recordset
        """
        partner_id = self.env.ref('base.res_partner_3').id
        purchase = self.env['purchase.order'].check_purchase_order_of_partner_existance(partner_id)
        self.assertNotIsInstance(purchase, dict)

    def test_01_check_purchase_order_of_partner_not_exist(self):
        """
            Test check_purchase_order_of_partner method
            We try to check the method to return warning
            It returns a dict warning
        """
        partner_id = self.env.ref('base.res_partner_address_16').id
        purchase = self.env['purchase.order'].check_purchase_order_of_partner_existance(partner_id)
        self.assertIn('warning', purchase)

    def test_02_get_filtered_purchases(self):
        """
            Test get_purchase_order_infos method
            We try to check the method to return warning
            It returns a dict warning
        """
        partner_id = self.env.ref('base.res_partner_3').id
        purchase = self.env['purchase.order'].get_filtered_purchases(partner_id, str(date.today().year)+'-01-01',
                                                                     str(date.today().year)+'-11-30', ['draft', 'done'])
        self.assertIsInstance(purchase, list)

    def test_03_get_purchase_order_infos(self):
        """
            Test get_purchase_order_infos method
            We try to check the method to return list
            It returns a list contains sale orders infos
        """
        partner_id = self.env.ref('base.res_partner_3').id
        purchase = self.env['purchase.order'].get_purchase_order_infos(partner_id, str(date.today().year)+'-01-01',
                                                                       str(date.today().year)+'-11-30')
        self.assertIsInstance(purchase, list)

    def test_04_check_get_purchase_order_infos_with_states_not_exists(self):
        """
            Test get_purchase_order_infos method
            It returns a dict contains partner infos with warning_states_not_exists element
        """
        partner_id = self.env.ref('base.res_partner_3').id
        purchase = self.env['purchase.order'].get_purchase_order_infos(partner_id, str(date.today().year)+'-01-01',
                                                                       str(date.today().year)+'-11-30', ['non_existent'])
        self.assertIn('warning_states_not_exists', purchase[-1])