import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import UNIT_CELSIUS, DEVICE_CLASS_TEMPERATURE, STATE_CLASS_MEASUREMENT

DEPENDENCIES = []

my_sensor_ns = cg.esphome_ns.namespace('my_sensor')
MySensor = my_sensor_ns.class_('MySensor', sensor.Sensor, cg.PollingComponent)

CONFIG_SCHEMA = sensor.sensor_schema(
    MySensor,
    unit_of_measurement=UNIT_CELSIUS,
    device_class=DEVICE_CLASS_TEMPERATURE,
    state_class=STATE_CLASS_MEASUREMENT
).extend({})

async def to_code(config):
    var = cg.new_Pvariable(config)
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
    cg.add(var.set_update_interval(1000))