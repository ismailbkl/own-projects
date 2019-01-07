# -*- coding: utf-8 -*-
# (C) 2018 Smile (<http://www.smile.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

def check_all_states(self, states, model='sale.order', field='state'):
    """
    Check the states entred by user to determine if it should be add to filter domain or to a warning
    :param self: object we search in
    :param states: list
    :param model: model
    :param field: string then type is selection
    :return: Two lists: one contains warning of fileds that not exists, other contains a list of fields exists
    """
    warning_list = []
    states_list = []
    for state in states:
        if state in dict(self.env[model]._fields[field].selection):
            states_list.append(state)
        else:
            warning_list.append(state)
    return states_list, warning_list


