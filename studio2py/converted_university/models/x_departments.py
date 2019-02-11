# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# (C) 2019 Smile (<http://www.smile.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class Departments(models.Model):
    _name = "x_departments"
    _inherit = ['mail.thread']

    x_name = fields.Char(name='x_name', string='Name', domain=[], )
    x_studio_field_C3DCI = fields.Char(
        name='x_studio_field_C3DCI', string='code department', domain=[], )
    x_studio_field_anKSn = fields.Integer(
        name='x_studio_field_anKSn', string='Number of proffessors', domain=[], )
    x_studio_field_WCOgl = fields.Integer(
        name='x_studio_field_WCOgl', string='Number of subjects', domain=[], )
    x_studio_field_Q8ZEc = fields.Selection(name='x_studio_field_Q8ZEc', string='New Priority', selection=[
                                            ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], domain=[], )
    x_studio_field_y3ybp = fields.One2many(inverse_name='x_studio_field_m2OZR', name='x_studio_field_y3ybp',
                                           string='New One2many', comodel_name='x_proffessors', domain=[], )
    x_studio_field_T31dO = fields.One2many(
        inverse_name='x_studio_field_tgCMc', name='x_studio_field_T31dO', string='New One2many', comodel_name='x_subjects', domain=[], )
