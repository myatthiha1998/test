# -*- coding: utf-8 -*-


from odoo import api, fields, models, _

class Electricity(models.Model):
    _name = 'electricity.electricity'
    
    member = fields.Char(string='Member')
    monthly_cost =  fields.Char(string="Monthly Cost")
    daily_cost = fields.Char(string="Daily Cost")
    yearly_cost = fields.Char(string="Yearly Cost")
    
    

   