from datetime import datetime, timedelta
from odoo import SUPERUSER_ID
from odoo import api, fields, models, _
from odoo.http import request

class marca(models.Model):
    _name = "golemme.marca"

    name = fields.Char(string='Valore')
    products_ids = fields.One2many('product.template', 'marca', string="Prodotti")

class modello(models.Model):
    _name = "golemme.modello"

    name = fields.Char(string='Valore')
    products_ids = fields.One2many('product.template', 'modello', string="Prodotti")

class tipologia(models.Model):
    _name = "golemme.tipologia"

    name = fields.Char(string='Valore')
    products_ids = fields.One2many('product.template', 'tipologia', string="Prodotti")

class alimentazione(models.Model):
    _name = "golemme.alimentazione"

    name = fields.Char(string='Valore')
    products_ids = fields.One2many('product.template', 'alimentazione', string="Prodotti")

class classe(models.Model):
    _name = "golemme.classe"

    name = fields.Char(string='Valore')
    products_ids = fields.One2many('product.template', 'classe', string="Prodotti")

class telecomando(models.Model):
    _name = "golemme.telecomando"

    name = fields.Char(string='Valore')
    products_ids = fields.One2many('product.template', 'telecomando', string="Prodotti")

class tecnologia(models.Model):
    _name = "golemme.tecnologia"

    name = fields.Char(string='Valore')
    products_ids = fields.One2many('product.template', 'tecnologia', string="Prodotti")
	
class unita(models.Model):
    _name = "golemme.unita"

    name = fields.Char(string='Valore')
    products_ids = fields.One2many('product.template', 'unita', string="Prodotti")
	
class wifi(models.Model):
    _name = "golemme.wifi"

    name = fields.Char(string='Valore')
    products_ids = fields.One2many('product.template', 'wifi', string="Prodotti")
    
class garanzia(models.Model):
    _name = "golemme.garanzia"

    name = fields.Char(string='Valore')
    products_ids = fields.One2many('product.template', 'garanzia', string="Prodotti")
	
class colore(models.Model):
    _name = "golemme.colore"

    name = fields.Char(string='Valore')
    products_ids = fields.One2many('product.template', 'colore', string="Prodotti")

class tipologia_installazione(models.Model):
    _name = "golemme.tipologia_installazione"
    name = fields.Char(string='Valore')
    
    products_ids = fields.One2many('product.template', 'tipologia_installazione', string="Prodotti")



	


	




