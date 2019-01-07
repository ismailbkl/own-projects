# -*- coding: utf-8 -*-
# (C) 2011 Smile (<http://www.smile.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestPartner(TransactionCase):

    def setUp(self):
        super(TestPartner, self).setUp()

    def test_00_check_partner_id_exist(self):
        """
            Test check_partner_existance method
            We try to check if user exists
            It returns a recordset
        """
        partner_id = self.env.ref('base.res_partner_3').id
        partner = self.env['res.partner'].check_partner_existance(partner_id)
        self.assertNotIsInstance(partner, dict)

    def test_01_check_partner_id_not_exist(self):
        """
            Test check_partner_existance method
            We try to check if user exists
            It returns a warning in dict
        """
        # partner_id exist not : 800000
        partner = self.env['res.partner'].check_partner_existance(800000)
        self.assertIn('warning', partner)

    def test_02_check_partner_is_company(self):
        """
            Test check_partner_iscompany method
            We try to check if partner as a company
            It returns a racordset
        """
        # partner_id : 9
        partner_id = self.env.ref('base.res_partner_2')
        company = self.env['res.partner'].check_partner_iscompany(partner_id)
        self.assertNotEquals(len(company['contacts']), 0)

    def test_03_check_partner_is_not_company(self):
        """
            Test check_partner_iscompany method
            We try to check if partner as a person
            It returns a warning in dict
        """
        # partner_id : 15
        partner_id = self.env.ref('base.res_partner_address_1')
        company = self.env['res.partner'].check_partner_iscompany(partner_id)
        self.assertEquals(len(company['contacts']), 0)

    def test_04_check_partner_infos_without_params(self):
        """
            Test get_partner_infos method
            We try to check the return of partner with the default fields
            It returns a dict contains partner infos
        """
        # partner_id : 15
        partner_id = self.env.ref('base.res_partner_address_1').id
        partner_infos = self.env['res.partner'].get_partner_infos(partner_id)
        self.assertEquals(len(partner_infos), 8)

    def test_05_check_partner_infos_with_params(self):
        """
            Test get_partner_infos method
            We try to check the return of partner with the specifics fields
            It returns a dict contains partner infos
        """
        # partner_id : 15
        partner_id = self.env.ref('base.res_partner_address_1').id
        partner_infos = self.env['res.partner'].get_partner_infos(partner_id, ['name', 'email', 'phone'])
        self.assertEquals(len(partner_infos), 4)

    def test_06_check_partner_infos_with_fields_not_exists(self):
        """
            Test get_partner_infos method
            It returns a dict contains partner infos with Fields_Not_exists element
        """
        # partner_id : 15
        partner_id = self.env.ref('base.res_partner_address_1').id
        partner_infos = self.env['res.partner'].get_partner_infos(partner_id, ['jhvjkvk', 'name', 'email', 'phone',
                                                                               'non_existent_1', 'non_existent_2'])
        self.assertIn('Fields_Not_exists', partner_infos)
