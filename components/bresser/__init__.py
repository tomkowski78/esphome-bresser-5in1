import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome import pins
from esphome.const import (
    CONF_HUMIDITY,
    CONF_WIND_SPEED,
    CONF_WIND_DIRECTION_DEGREES,
    CONF_ID,
    CONF_TEMPERATURE,
    CONF_PIN,
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_WIND_SPEED,
    STATE_CLASS_MEASUREMENT,
    UNIT_CELSIUS,
    UNIT_PERCENT,
    UNIT_DEGREES,
    UNIT_MILLIMETER,
)

CONF_PIN_CS      = "PIN_CS"
CONF_PIN_GDO0    = "PIN_GDO0"
CONF_PIN_GDO2    = "PIN_GDO2"


PIN_CS   = 5
PIN_GDO0 = 27
PIN_GDO2 =  4


bresser_ns = cg.esphome_ns.namespace("bresser")
Bresser = bresser_ns.class_(
    "Bresser", cg.PollingComponent 
)



CONFIG_SCHEMA = cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(Bresser),
            
            cv.Required(CONF_PIN_CS): cv.All(pins.internal_gpio_input_pin_schema),
            cv.Required(CONF_PIN_GDO0): cv.All(pins.internal_gpio_input_pin_schema),
            cv.Required(CONF_PIN_GDO2): cv.All(pins.internal_gpio_input_pin_schema),
        }
    ).extend(cv.polling_component_schema("60s"))


async def to_code(config):
    var  = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    #await sensor.register_sensor(var, config) 
    #await sensor.my_to_code_sensor(var, config)
   
    pin = await cg.gpio_pin_expression(config[CONF_PIN_CS])
    cg.add(var.set_pin_cs(pin))
    
    pin = await cg.gpio_pin_expression(config[CONF_PIN_GDO0])
    cg.add(var.set_pin_gdo0(pin))
    
    pin = await cg.gpio_pin_expression(config[CONF_PIN_GDO2])
    cg.add(var.set_pin_gdo2(pin))
    
#    var_adv = cg.new_Pvariable(config[CONF_INFO_COMP_ID])
#    await cg.register_component(var_adv, {})

