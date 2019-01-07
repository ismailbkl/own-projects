# -*- coding: utf-8 -*-
# (C) 2018 Smile (<http://www.smile.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api, _
from .tools import check_all_states

class StockPicking(models.Model):
    _inherit = "stock.picking"

    def check_stock_picking_of_partner_existance(self, partner_id):
        """
        Check if there is stock pickings for partner_id
        :param partner_id: int
        :return: warning if there is no stock pickings for the partner_id
        """
        stock_picking_of_partner = self.search([('partner_id', '=', partner_id)])
        if stock_picking_of_partner:
            pass
        else:
            return {'warning': _('There is no stock picking for the partner')}

    def pull_stock_picking(self):
        """
        Get all the infos we need of stock picking
        :return: list contains all infos of stock pickings
        """
        stock_picking_list = []
        for picking in self:
            move_lines = []
            for move in picking:
               move_lines.append({
                    'Product_id': move.move_lines.product_id.name,
                    'Product_uom_qty': move.move_lines.product_uom_qty,
                    'Quantity_done': move.move_lines.quantity_done,
                })
            stock_pickings_infos = {
                'WH': picking.name,
                'Date': picking.create_date,
                'move_lines': move_lines,
                'state': picking.state,
                'type': picking.picking_type_id.code,
            }
            stock_picking_list += [stock_pickings_infos]
        return stock_picking_list

    def get_filtered_pickings(self, partner_id, start_date, end_date, states, type):
        """
        Pull the filtred informations of stock picking of a partner
        :param partner_id: int
        :param start_date: date
        :param end_date: date
        :param states: list
        :param type: list
        :return: list contain all infos or a warning
        """
        filter_domain = [('partner_id', '=', partner_id),
                         ('scheduled_date', '>=', start_date),
                         ('scheduled_date', '<=', end_date),
                         ('picking_type_id.code', 'in', type)]
        warning = {}
        states_list, warning_list = check_all_states(self, states, 'stock.picking', 'state')
        if warning_list:
            warning.update({"warning_states_not_exists": warning_list})
        if states_list:
            filter_domain.append(('state', 'in', states_list))
        orders = self.search(filter_domain)
        if not orders:
            return {"warning": _("There is no sale order for the partner in this period!")}
        datas = orders.pull_stock_picking()
        if warning:
            datas.append(warning)
        return datas

    @api.model
    def get_stock_picking_infos(self,  partner_id, start_date, end_date, states=['done'], type=['outgoing']):
        """
        pull all the stock pickings of a specific partner
        :param partner_id: int
        :param start_date: string (format date yyyy-mm-dd)
        :param end_date: string (format date yyyy-mm-dd)
        :param states: list (must be in state selection field)
        :param type: list (must be in picking_type_id.code selection field)
        :return: dict contains all principal infos for the stock picking of the
                partner in the period between start and end date
        """
        partner = self.env['res.partner'].check_partner_existance(partner_id)
        if isinstance(partner, dict):
            return partner
        stock_picking_of_partner = self.check_stock_picking_of_partner_existance(partner_id)
        if isinstance(stock_picking_of_partner, dict):
            return stock_picking_of_partner
        return self.get_filtered_pickings(partner_id, start_date, end_date, states, type)
