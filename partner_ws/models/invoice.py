# -*- coding: utf-8 -*-
# (C) 2018 Smile (<http://www.smile.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api, _
from .tools import check_all_states

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    def check_account_invoices_of_partner_existance(self, partner_id):
        """
        Check if there is purchase orders of partner_id
        :param partner_id: int
        :return: warning if there is no purchase order for the partner_id
         """
        account_invoice_of_partner = self.search([('partner_id', '=', partner_id)])
        if account_invoice_of_partner:
            pass
        else:
            return {'warning': _('There is no account invoice for the partner')}

    def pull_account_invoices(self):
        """
        Get all the infos we need of account invoices
        :return: list contains all infos of stock pickings
        """
        account_invoice_list = []
        amount_total = 0
        for order in self:
            amount_total += order.amount_untaxed
            account_invoices_infos = {
                'INV': order.name,
                'date': order.create_date,
                'amount_untaxed': order.amount_untaxed,
                'state': order.state,
            }
            account_invoice_list += [account_invoices_infos]

        account_invoices_infos_with_total = account_invoice_list + [{'Total_amount': amount_total}]
        return account_invoices_infos_with_total

    def get_filtered_invoices(self, partner_id, start_date, end_date, states):
        """
        Pull the filtred informations of account invoices of a partner
        :param partner_id: int
        :param start_date: date
        :param end_date: date
        :param states: list
        :return:
        """
        filter_domain = [('partner_id', '=', partner_id),
                         ('date_invoice', '>=', start_date),
                         ('date_invoice', '<=', end_date)]
        warning = {}
        states_list, warning_list = check_all_states(self, states, 'account.invoice', 'state')
        if warning_list:
            warning.update({"warning_states_not_exists": warning_list})
        if states_list:
            filter_domain.append(('state', 'in', states_list))
        orders = self.search(filter_domain)
        if not orders:
            return {"warning": _("There is no sale order for the partner in this period!")}
        datas = orders.pull_account_invoices()
        if warning:
            datas.append(warning)
        return datas

    @api.model
    def get_account_invoice_infos(self, partner_id, start_date, end_date, states=['paid', 'open']):
        """
        Pull all the account invoices of a specific partner
        :param partner_id: int
        :param start_date: string (format date yyyy-mm-dd)
        :param end_date: string (format date yyyy-mm-dd)
        :param states: list (must be in state selection field)
        :return: dict contains all principal infos for the account invoive of the
                partner in the period between start and end date
        """
        partner = self.env['res.partner'].check_partner_existance(partner_id)
        if isinstance(partner, dict):
            return partner
        account_invoice_of_partner = self.check_account_invoices_of_partner_existance(partner_id)
        if isinstance(account_invoice_of_partner, dict):
            return account_invoice_of_partner
        return self.get_filtered_invoices(partner_id, start_date, end_date, states)
