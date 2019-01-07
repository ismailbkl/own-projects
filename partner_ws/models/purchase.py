# -*- coding: utf-8 -*-
# (C) 2018 Smile (<http://www.smile.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api, _
from .tools import check_all_states

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def check_purchase_order_of_partner_existance(self, partner_id):
        """
        Check if there is purchase orders for partner_id
        :param partner_id: int
        :return: warning if there is no purchase order for the partner_id
         """
        purchases_order_of_partner = self.search([('partner_id', '=', partner_id)])
        if purchases_order_of_partner:
            pass
        else:
            return {'warning': _('There is no purchase order for the partner')}

    def pull_purchase_orders(self):
        """
        Get all the infos we need of purchase orders
        :return: list contains all infos of stock pickings
        """
        purchase_order_list = []
        amount_total = 0
        for order in self:
            amount_total += order.amount_untaxed
            purchase_orders_infos = {
                'SO': order.name,
                'Date': order.create_date,
                'Amount_untaxed': order.amount_untaxed,
                'State': order.state,
            }
            purchase_order_list += [purchase_orders_infos]

        purchase_orders_infos_with_total = purchase_order_list + [{'Total_amount': amount_total}]
        return purchase_orders_infos_with_total

    def get_filtered_purchases(self, partner_id, start_date, end_date, states):
        """
        Pull the filtred informations of purchase orders of a partner
        :param partner_id: int
        :param start_date: date
        :param end_date: date
        :param states: list
        :return:
        """
        filter_domain = [('partner_id', '=', partner_id),
                         ('date_order', '>=', start_date),
                         ('date_order', '<=', end_date)]
        warning = {}
        states_list, warning_list = check_all_states(self, states, 'purchase.order', 'state')
        if warning_list:
            warning.update({"warning_states_not_exists": warning_list})
        if states_list:
            filter_domain.append(('state', 'in', states_list))
        orders = self.search(filter_domain)
        if not orders:
            return {"warning": _("There is no sale order for the partner in this period!")}
        datas = orders.pull_purchase_orders()
        if warning:
            datas.append(warning)
        return datas

    @api.model
    def get_purchase_order_infos(self, partner_id, start_date, end_date, states=['draft', 'done']):
        """
        Pull all the purchases orders of a specific partner
        :param partner_id: int
        :param start_date: string (format date yyyy-mm-dd)
        :param end_date: string (format date yyyy-mm-dd)
        :param states: list (must be in state selection field)
        :return: dict contains all principal infos for the purchase order of the
                partner in the period between start and end date
        """
        partner = self.env['res.partner'].check_partner_existance(partner_id)
        if isinstance(partner, dict):
            return partner
        purchases_order_of_partner = self.check_purchase_order_of_partner_existance(partner_id)
        if isinstance(purchases_order_of_partner, dict):
            return purchases_order_of_partner
        return self.get_filtered_purchases(partner_id, start_date, end_date, states)
