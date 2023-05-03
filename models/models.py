from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Car(models.Model):
    _name = "car.car"
    _description = 'car.car'

    name = fields.Char(string="Name")
    horse_power = fields.Integer(string="Horse Power (hp)")
    door_number = fields.Integer(string="Doors Number")
    driver_id = fields.Many2one('res.partner', string="Driver")
    parking_id = fields.Many2one('parking.parking', string="Parking")
    feature_ids = fields.Many2many('car.feature', string="Features")
    total_speed = fields.Integer(string='Speed Total  (hp)*50', compute='get_total_speed')
    random_massage = fields.Char(string='Massage', compute='say_hello')

    status = fields.Selection([('new','New'),('used','Used'),('pending','Pending'),('sold','Sold')], string='Status', default='new')
    car_sequence=fields.Char(string='Sequence')
    
    
    # _inherit='product.template'
    
    def set_car_to_used(self):
        self.status = 'used'
        
        
    def set_car_to_pending(self):
        print("================================================")
        print("Hello World")
        print("================================================")
        self.status = 'pending'
        
        
    def set_car_to_sold(self):
        self.status = 'sold'
    
    
    @api.model
    def create(self, vals):
        print('---------We are override method create-------')
        if vals['name'] == 'abcd':
            vals['name'] = 'bmw x seven'
            
        vals['car_sequence'] = self.env['ir.sequence'].next_by_code('car.sequence')
        result = super(Car, self).create(vals)
        return result
    
    
    def write(self, vals):
        
        if vals['horse_power'] == 10:
            raise ValidationError(_('The horse power can t be greater than 10'))
        print('---------We are override method write-------')
        result = super(Car, self).write(vals)
        return result
        
        
    def get_total_speed(self):
        # print('name',self.name)
        # print('horse_power',self.horse_power)
        self.total_speed = self.horse_power * 50


    def say_hello(self):
        # print('driver_id',self.driver_id)
        # print('driver_id.id',self.driver_id.id)
        # print('driver_id.name',self.driver_id.name)
        
        self.random_massage = "Hello " + self.driver_id.name
        

# access_my_first_module_my_first_module___car.form___model_car_car___base.group_user___1___1___1___1
# access_car_car___Access For Car___model_car_car___base.group_user___1___1___1___1

class Parking(models.Model):
    _name = "parking.parking"
    _description = "parking.parking"

    name = fields.Char(string="Name")
    car_ids = fields.One2many('car.car', 'parking_id', string="Cars")


class CarFeatures(models.Model):
    _name = "car.feature"
    _description = "car.feature"

    name = fields.Char(string="Name")
    # value = fields.Char(string="Value") [we add valu in car.xml as widget="many2many_tags"]


