# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# (C) 2019 Smile (<http://www.smile.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class Students(models.Model):
    _name = "x_students"
    _inherit = ['mail.thread']

    x_name = fields.Char(name='x_name', string='Name', domain=[], )
    x_studio_field_5pROc = fields.Binary(
        name='x_studio_field_5pROc', string='Image', domain=[], )
    x_studio_field_q7jZ8 = fields.Date(
        name='x_studio_field_q7jZ8', string='Birth Date', domain=[], )
    x_studio_field_3QFQW = fields.Char(
        name='x_studio_field_3QFQW', string='Address', domain=[], )
    x_studio_field_AyhsB = fields.Datetime(
        name='x_studio_field_AyhsB', string='Inscription date', domain=[], )
    x_studio_field_IKyoq = fields.Selection(name='x_studio_field_IKyoq', string='Sexe', selection=[
                                            ('Male', 'Male'), ('Female', 'Female')], domain=[], )
    x_studio_field_jlUcP = fields.Integer(
        name='x_studio_field_jlUcP', string='Age', domain=[], )
    x_studio_field_i414y = fields.Many2one(
        on_delete='set null', name='x_studio_field_i414y', string='Classroom', comodel_name='x_classrooms', domain=[], )
    x_studio_field_9CyA7 = fields.Many2many(
        name='x_studio_field_9CyA7', string='proffessors', comodel_name='x_proffessors', domain=[], )
