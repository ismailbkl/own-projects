# -*- coding: utf-8 -*-
# (C) 2018 Smile (<http://www.smile.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api, _

class ResPartner(models.Model):
    _inherit = "res.partner"

    def check_partner_existance(self, partner_id):
        """
        Check if partner exists
        :param partner_id: int
        :return: partner recordset if exists, warning if not
        """
        if isinstance(partner_id, int):
            partner_id = self.search([('id', '=', partner_id)])
            if partner_id:
                return partner_id
            else:
                return {'warning': _("There is no partner with this ID, please put an other one!")}
        else:
            return {'warning': _("The partner id must be Integer!")}

    def check_partner_iscompany(self, partner_id):
        """
        Pull child contacts of partner, if partner is a company
        :param partner_id: int
        :return: dict contains list of child contacts
        """
        childs_list = []
        if partner_id.is_company:
            for contact in partner_id.child_ids:
                childs_list += [{"name:": contact.name, 'function': contact.function, "phone": contact.phone,
                                 "email": contact.email, "lang": contact.lang}]
        return {'contacts': childs_list}

    @api.model
    def get_partner_infos(self, partner_id, fields=['name', 'street', 'phone', 'mobile', 'email', 'website', 'lang']):
        """
        Pull all the informations of a specific partner
        :param partner_id: int that is the partner id
        :param fields: list that is the demanding fields
        :return: dict contains the informations of the partner
        """
        partner_infos = {}
        warning_list = []
        # Check partner
        partner_id = self.check_partner_existance(partner_id)
        if isinstance(partner_id, dict):
            return partner_id
        # Process
        if len(fields) == 0:
            return {"warning": "You must insert at least one field in the list, or remove it to get the defaults fields"}
        for field in fields:
            if field in self._fields:
                partner_infos.update({field: eval('partner_id.%s' %field)})
            else:
                warning_list.append(field)
        if warning_list:
            partner_infos.update({"Fields_Not_exists": warning_list})
        partner_infos.update(self.check_partner_iscompany(partner_id))
        return partner_infos
