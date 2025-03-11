/*
* na podstaw https://github.com/matthias-bs/Bresser_Weather_Sensor_CC1101_MQTT
* dodatek (inccule) do ESPHome
* odbioru danych z staji pogodowej Bresser
* 
*/

#pragma once
#include "esphome.h"
#include "RadioLib.h"
#include "esphome/core/gpio.h"


#if defined(ESP32)
    #define PIN_CC1101_CS   5
    #define PIN_CC1101_GDO0 27
    #define PIN_CC1101_GDO2 4
#elif defined(ESP8266)
    #define PIN_CC1101_CS   2
    #define PIN_CC1101_GDO0 4
    #define PIN_CC1101_GDO2 5
#endif

namespace esphome {
namespace bresser {

	enum DecodeStatus {
        DECODE_OK, DECODE_PAR_ERR, DECODE_CHK_ERR, DECODE_DIG_ERR
    };

    struct WeatherData_S {
        uint8_t  s_type;               // only 6-in1
        uint32_t sensor_id;            // 5-in-1: 1 byte / 6-in-1: 4 bytes
        uint8_t  chan;                 // only 6-in-1
        bool     temp_ok;              // only 6-in-1
        float    temp_c;
        int      humidity;
        bool     uv_ok;                // only 6-in-1
        float    uv;                   // only 6-in-1
        bool     wind_ok;              // only 6-in-1
        float    wind_direction_deg;
        float    wind_gust_meter_sec;
        float    wind_avg_meter_sec;
        bool     rain_ok;              // only 6-in-1
        float    rain_mm;
        bool     battery_ok;
        bool     moisture_ok;          // only 6-in-1
        int      moisture;             // only 6-in-1
    };

    typedef struct WeatherData_S WeatherData_t;


class Bresser : public PollingComponent  {
  public:	
  

    void setup() override; 
    void loop() override; 
    void update() override;

	void set_temperature_sensor(sensor::Sensor *temperature_sensor) { temperature_sensor_ = temperature_sensor; }
    void set_humidity_sensor(sensor::Sensor *humidity_sensor) { humidity_sensor_ = humidity_sensor; }
	void set_wind_speed_sensor(sensor::Sensor *wind_speed_sensor) { wind_speed_sensor_ = wind_speed_sensor; }
	void set_wind_direction_sensor(sensor::Sensor *wind_direction_sensor) { wind_direction_sensor_ = wind_direction_sensor; }
	void set_rain_sensor(sensor::Sensor *rain_sensor) { rain_sensor_ = rain_sensor; }
	
	void set_pin_cs(InternalGPIOPin *pin) { this->pin_CS_ = pin; }
	void set_pin_gdo0(InternalGPIOPin *pin) { this->pin_GDO0_ = pin; }
	void set_pin_gdo2(InternalGPIOPin *pin) { this->pin_GDO2_ = pin; }
	
  protected:
  
	CC1101 *radio;// = new Module(PIN_CC1101_CS, PIN_CC1101_GDO0, RADIOLIB_NC, PIN_CC1101_GDO2);

	InternalGPIOPin  *pin_CS_{nullptr};
	InternalGPIOPin  *pin_GDO0_{nullptr};
	InternalGPIOPin  *pin_GDO2_{nullptr};

  
	sensor::Sensor *temperature_sensor_{nullptr};
	sensor::Sensor *humidity_sensor_{nullptr};
	sensor::Sensor *wind_speed_sensor_{nullptr};
	sensor::Sensor *wind_direction_sensor_{nullptr};
	sensor::Sensor *rain_sensor_{nullptr};
	
    // Weather data object
    WeatherData_t weatherData;

	
    void genData(WeatherData_t *pOut);
	uint16_t lfsr_digest16(uint8_t const message[], unsigned bytes, uint16_t gen, uint16_t key);
	int add_bytes(uint8_t const message[], unsigned num_bytes);
    DecodeStatus decodeBresser5In1Payload(uint8_t *msg, uint8_t msgSize, WeatherData_t *pOut);
    DecodeStatus decodeBresser6In1Payload(uint8_t *msg, uint8_t msgSize, WeatherData_t *pOut);
    uint8_t windspeed_ms_to_bft(float ms);
    bool getWeatherdata(void);
    void printRawdata(uint8_t *msg, uint8_t msgSize);
       	
  	
};

} //namesp
} //namesp