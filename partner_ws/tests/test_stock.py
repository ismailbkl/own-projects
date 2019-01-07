# -*- coding: utf-8 -*-
# (C) 2011 Smile (<http://www.smile.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from datetime import date

from odoo.tests.common import TransactionCase


class TestStock(TransactionCase):

    def setUp(self):
        super(TestStock, self).setUp()

    def test_00_check_stock_picking_of_partner_exist(self):
        """
            Test check_stock_picking_of_partner method
            We try to check if there is a sale order of this partner
            It returns a recordset
        """
        partner_id = self.env.ref('base.res_partner_2').id
        picking = self.env['stock.picking'].check_stock_picking_of_partner_existance(partner_id)
        self.assertNotIsInstance(picking, dict)

    def test_01_check_stock_picking_of_partner_not_exist(self):
        """
            Test check_stock_picking_of_partner method
            We try to check the method to return warning
            It returns a dict warning
        """
        partner_id = self.env.ref('base.res_partner_address_16').id
        picking = self.env['stock.picking'].check_stock_picking_of_partner_existance(partner_id)
        self.assertIn('warning', picking)

    def test_02_get_filtered_pickings(self):
        """
            Test get_purchase_order_infos method
            We try to check the method to return warning
            It returns a dict warning
        """
        partner_id = self.env.ref('base.res_partner_1').id
        picking = self.env['stock.picking'].get_filtered_pickings(partner_id, '2017-01-01', '2017-11-30',
                                                                  ['done'], ['outgoing'])
        self.assertIsInstance(picking, dict)

    def test_03_get_stock_picking_infos(self):
        """
            Test get_stock_picking_infos method
            We try to check the method to return all infos of sale
            It returns a list contains all sale infos
        """
        partner_id = self.env.ref('base.res_partner_1').id
        picking = self.env['stock.picking'].get_stock_picking_infos(partner_id, str(date.today().year)+'-01-01',
                                                                    str(date.today().year)+'-11-30')
        self.assertIsInstance(picking, list)

    def test_04_check_get_stock_picking_infos_with_states_not_exists(self):
        """
            Test get_stock_picking_infos method
            It returns a dict contains partner infos with warning_states_not_exists element
        """
        partner_id = self.env.ref('base.res_partner_1').id
        picking = self.env['stock.picking'].get_stock_picking_infos(partner_id, str(date.today().year)+'-01-01',
                                                                    str(date.today().year)+'-11-30', ['non_existent'])
        self.assertIn('warning_states_not_exists', picking[-1])
