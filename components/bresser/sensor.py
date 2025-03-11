
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

bresser_ns = cg.esphome_ns.namespace("bresser")
Bresser = bresser_ns.class_(
    "Bresser", cg.PollingComponent 
)

CONFIG_SCHEMA = cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(Bresser),
            
            cv.Optional(CONF_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_HUMIDITY): sensor.sensor_schema(
                unit_of_measurement=UNIT_PERCENT,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_HUMIDITY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_WIND_SPEED): sensor.sensor_schema(
                unit_of_measurement="m/s",
                accuracy_decimals=1,
                #device_class=DEVICE_CLASS_WIND_SPEED,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_WIND_DIRECTION_DEGREES): sensor.sensor_schema(
                unit_of_measurement=UNIT_DEGREES,
                accuracy_decimals=0,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional('rain'): sensor.sensor_schema(
                unit_of_measurement=UNIT_MILLIMETER,
                accuracy_decimals=1,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional('rain'): sensor.sensor_schema(
                unit_of_measurement=UNIT_MILLIMETER,
                accuracy_decimals=1,
                state_class=STATE_CLASS_MEASUREMENT,
            ),

        }
    ).extend(cv.polling_component_schema("60s"))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    if temperature_config := config.get(CONF_TEMPERATURE):
        sens = await sensor.new_sensor(temperature_config)
        cg.add(var.set_temperature_sensor(sens))
        
    if humidity_config := config.get(CONF_HUMIDITY):
        sens = await sensor.new_sensor(humidity_config)
        cg.add(var.set_humidity_sensor(sens))
        
    if wind_speed_config := config.get(CONF_WIND_SPEED):
        sens = await sensor.new_sensor(wind_speed_config)
        cg.add(var.set_wind_speed_sensor(sens))        
        
    if wind_direction_degrees_config := config.get(CONF_WIND_DIRECTION_DEGREES):
        sens = await sensor.new_sensor(wind_direction_degrees_config)
        cg.add(var.set_wind_direction_sensor(sens))                
        
    if rain_config := config.get('rain'):
        sens = await sensor.new_sensor(rain_config)
        cg.add(var.set_rain_sensor(sens))                        
        