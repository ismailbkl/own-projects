# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# (C) 2019 Smile (<http://www.smile.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class Proffessors(models.Model):
    _name = "x_proffessors"
    _inherit = ['mail.thread']

    x_name = fields.Char(name='x_name', string='Name', domain=[], )
    x_studio_field_vPm32 = fields.Binary(
        name='x_studio_field_vPm32', string='New Image', domain=[], )
    x_studio_field_w2XeZ = fields.Date(
        name='x_studio_field_w2XeZ', string='Birth Date', domain=[], )
    x_studio_field_fTRVz = fields.Datetime(
        name='x_studio_field_fTRVz', string='Start Date ', domain=[], )
    x_studio_field_CA5cQ = fields.Many2one(
        on_delete='set null', name='x_studio_field_CA5cQ', string='Subject', comodel_name='x_subjects', domain=[], )
    x_studio_field_m2OZR = fields.Many2one(
        on_delete='set null', name='x_studio_field_m2OZR', string='Department', comodel_name='x_departments', domain=[], )
    x_studio_field_SNDxF = fields.Many2many(
        name='x_studio_field_SNDxF', string='classrooms', comodel_name='x_classrooms', domain=[], )
    x_studio_field_0WZBi = fields.Many2many(
        name='x_studio_field_0WZBi', string='Classroom', comodel_name='x_classrooms', domain=[], )
    x_studio_field_OIu8d = fields.Selection(name='x_studio_field_OIu8d', string='Sexe', selection=[
                                            ('Male', 'Male'), ('Female', 'Female')], domain=[], )
