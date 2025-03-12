# esphome-bresser

## YAML definition examples

```yaml

libraries:
    - jgromes/RadioLib

esp8266:
  board: d1_mini_lite

spi:

external_components:
  source:
    type: git
    url: https://github.com/olekdata/esphome-bresser
    ref: main

bresser:
  PIN_CS:   2
  PIN_GDO0: 4
  PIN_GDO2: 5


sensor:
  - platform: bresser
    temperature:
      name: "Temperatura"
    humidity:
      name: "Wilgotność"
    wind_speed:
      name: "Prędkość wiatru"
    wind_direction_degrees:
      name: "Kierunek wiatru"
    rain:
      name: "Deszcz"
    update_interval: 10s
```
## Connection example

```yaml

#  ***********************  Podłączenie fizyczne modułów ****************************************
#
#                                    +-----------------+| 
#                                    |    |  |  |  |    |
#                              [RST] |o                o| [TX ] [GPIO1]
#                     [ ADC1 ] [ A0] |o                o| [RX ] [GPIO3]
#                     [GPIO16] [ D0] |o   W E M O S    o| [D1 ] [GPIO5]   6 zielony
#  4 fiolet    [ SCK] [GPIO14] [ D5] |o                o| [D2 ] [GPIO4]   7 żółty
#  5 niebie    [MISO] [GPIO12] [ D6] |o   D1 MINI      o| [D3 ] [GPIO0]
#  3 biały     [MOSI] [GPIO13] [ D7] |o                o| [D4 ] [GPIO2]   8 pomar
#              [ SS ] [GPIO15] [ D8] |o                o| [GND]           2 szary
#  1 czarny                    [3v3] |o                o| [5V ]
#                                      |                |
#                                      |----|usb|-------|
#
#
#                                    +---------------------+
#  1 czarny                  [ VCC]  |o                    |                 
#  2 szary                   [ GND]  |o                    |                 
#  3 biały                   [MOSI]  |o                   o| [GND]
#  4 fiolet                  [SCLK]  |o     CC1101        o| [ATN] /\/\/\/\/               
#  5 niebie                  [MISO]  |o                   o| [GND]                
#  6 zielony                 [GDO2]  |o                    |                 
#  7 żółty                   [GDO0]  |o                    |                 
#  8 pomar                   [ CSN]  |o                    |                 
#                                    +---------------------+
#
#  mosi_pin: GPIO13
#  miso_pin: GPIO12
#  clk_pin:  GPIO14
#  cs_pin:   GPIO2
#  gdo0_pin: GPIO4
#  gdo2_pin: GPIO5

# https://esphome.io/components/sensor/custom.html
#
# instalacja poprzez VSC wiecej 
# https://olekdata.pl/blog/2024/01/14/stacja-pogodowa-bresser5in1-wspolpraca-z-home-assistant/
#
```
