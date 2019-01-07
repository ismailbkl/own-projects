# -*- coding: utf-8 -*-
# (C) 2018 Smile (<http://www.smile.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api, _
from .tools import check_all_states

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def check_sale_order_of_partner_existance(self, partner_id):
        """
        Check if there is sale orders for partner_id
        :param partner_id: int
        :return: warning if there is no sale orders for the partner_id
        """
        sales_order_of_partner = self.search([('partner_id', '=', partner_id)])
        if sales_order_of_partner:
            pass
        else:
            return {'warning': _('There is no sale order for the partner')}

    @api.multi
    def pull_sale_orders(self):
        """
        Get orders and total amount
        :return: dict contains all infos of sale orders
        """
        orders = []
        amount_total = 0
        for order in self:
            amount_total += order.amount_untaxed
            values = {
                'Ref': order.name,
                'date': order.create_date,
                'amount_untaxed': order.amount_untaxed,
                'state': order.state,
            }
            orders.append(values)
        return {'sales': orders, 'total_amount': amount_total}

    def get_filtered_sales(self, partner_id, start_date, end_date, states):
        """
        Pull the filtred informations of sales order of a partner
        :param partner_id: int
        :param start_date: string (format date yyyy-mm-dd)
        :param end_date: string (format date yyyy-mm-dd)
        :param states: list (must be in state selection field)
        :return: dict contain all infos or a warning
        """
        filter_domain = [('partner_id', '=', partner_id),
                         ('confirmation_date', '>=', start_date),
                         ('confirmation_date', '<=', end_date)]
        warning = {}
        states_list, warning_list = check_all_states(self, states, 'sale.order', 'state')
        if warning_list:
            warning.update({"warning_states_not_exists": warning_list})
        if states_list:
            filter_domain.append(('state', 'in', states_list))
        orders = self.search(filter_domain)
        if not orders:
            return {"warning": _("There is no sale order for the partner in this period!")}
        datas = orders.pull_sale_orders()
        if warning:
            datas.update(warning)
        return datas

    @api.model
    def get_sale_order_infos(self, partner_id, start_date, end_date, states=['done', 'sale']):
        """
        Pull all the sales orders of a specific partner
        :param partner_id: int
        :param start_date: string (format date yyyy-mm-dd)
        :param end_date: string (format date yyyy-mm-dd)
        :param states: list (must be in state selection field)
        :return: dict contains all principal infos for the sale order of the
                partner in the period between start and end date
        """
        partner = self.env['res.partner'].check_partner_existance(partner_id)
        if isinstance(partner, dict):
            return partner
        sales_order_of_partner = self.check_sale_order_of_partner_existance(partner_id)
        if isinstance(sales_order_of_partner, dict):
            return sales_order_of_partner
        return self.get_filtered_sales(partner_id, start_date, end_date, states)
