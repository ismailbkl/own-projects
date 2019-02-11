# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# (C) 2019 Smile (<http://www.smile.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class Subjects(models.Model):
    _name = "x_subjects"
    _inherit = ['mail.thread']

    x_name = fields.Char(name='x_name', string='Name', domain=[], )
    x_studio_field_5frFt = fields.Char(
        name='x_studio_field_5frFt', string='code subject', domain=[], )
    x_studio_field_jbQGX = fields.Integer(
        name='x_studio_field_jbQGX', string='Number of proffessors', domain=[], depends='x_studio_field_jbQGX', )
    x_studio_field_10MGz = fields.Integer(
        name='x_studio_field_10MGz', string=' umber', domain=[], )
    x_studio_field_tgCMc = fields.Many2one(
        on_delete='set null', name='x_studio_field_tgCMc', string='Department', comodel_name='x_departments', domain=[], )
    x_studio_field_3TRcW = fields.One2many(inverse_name='x_studio_field_CA5cQ', name='x_studio_field_3TRcW',
                                           string='New One2many', comodel_name='x_proffessors', domain=[], )
    x_studio_field_QrHjn = fields.Many2many(
        name='x_studio_field_QrHjn', string='classrooms', comodel_name='x_classrooms', domain=[], )
