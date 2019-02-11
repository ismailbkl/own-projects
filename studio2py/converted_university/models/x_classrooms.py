# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# (C) 2019 Smile (<http://www.smile.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class Classrooms(models.Model):
    _name = "x_classrooms"
    _inherit = ['mail.thread']

    x_name = fields.Char(name='x_name', string='Name', domain=[], )
    x_studio_field_BEoj2 = fields.Char(
        name='x_studio_field_BEoj2', string='code classroom', domain=[], )
    x_studio_field_g2P2p = fields.Integer(
        name='x_studio_field_g2P2p', string='Level', domain=[], )
    x_studio_field_ZlV1X = fields.Integer(
        name='x_studio_field_ZlV1X', string='Number of students', domain=[], )
    x_studio_field_gKfHJ = fields.Many2one(
        on_delete='set null', name='x_studio_field_gKfHJ', string='Department', comodel_name='x_departments', domain=[], )
    x_studio_field_zcMMg = fields.Many2many(
        name='x_studio_field_zcMMg', string='proffessors', comodel_name='x_proffessors', domain=[], )
    x_studio_field_8S1e1 = fields.One2many(
        inverse_name='x_studio_field_i414y', name='x_studio_field_8S1e1', string='New One2many', comodel_name='x_students', domain=[], )
