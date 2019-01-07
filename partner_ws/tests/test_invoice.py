# -*- coding: utf-8 -*-
# (C) 2011 Smile (<http://www.smile.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from datetime import date

from odoo.tests.common import TransactionCase

class TestInvoice(TransactionCase):

    def setUp(self):
        super(TestInvoice, self).setUp()

    def test_00_check_account_invoice_of_partner_exist(self):
        """
            Test check_account_invoice_of_partner method
            We try to check if there is a sale order of this partner
            It returns a recordset
        """
        partner_id = self.env.ref('base.res_partner_2').id
        invoice = self.env['account.invoice'].check_account_invoices_of_partner_existance(partner_id)
        self.assertNotIsInstance(invoice, dict)

    def test_01_check_account_invoice_of_partner_not_exist(self):
        """
            Test check_account_invoice_of_partner method
            We try to check the method to return warning
            It returns a dict warning
        """
        partner_id = self.env.ref('base.res_partner_address_16').id
        invoice = self.env['account.invoice'].check_account_invoices_of_partner_existance(partner_id)
        self.assertIn('warning', invoice)

    def test_02_get_filtered_invoices(self):
        """
            Test get_account_invoice_infos method
            We try to check the method to return all infos of sale
            It returns a list contains all invoice infos
        """
        partner_id = self.env.ref('base.res_partner_address_25').id
        invoice = self.env['account.invoice'].get_filtered_invoices(partner_id, str(date.today().year)+'-01-01',
                                                                    str(date.today().year)+'-11-30',
                                                                    ['open', 'paid'])
        self.assertIsInstance(invoice, list)

    def test_03_get_account_invoice_infos(self):
        """
            Test get_account_invoice_infos method
            We try to check the method to return all infos of sale
            It returns a list contains all sale infos
        """
        partner_id = self.env.ref('base.res_partner_2').id
        invoice = self.env['account.invoice'].get_account_invoice_infos(partner_id, str(date.today().year)+'-01-01',
                                                                        str(date.today().year)+'-11-30')

        self.assertIsInstance(invoice, list)

    def test_04_check_get_account_invoice_infos_with_states_not_exists(self):
        """
            Test get_account_invoice method
            It returns a dict contains partner infos with warning_states_not_exists element
        """
        partner_id = self.env.ref('base.res_partner_2').id
        partner_infos = self.env['account.invoice'].get_account_invoice_infos(partner_id, str(date.today().year)+'-01-01'
                                                                              , str(date.today().year)+'-11-30',
                                                                              ['non_existent'])
        self.assertIn('warning_states_not_exists', partner_infos[-1])
