# MFRC522 test

MFRC522 NFC module test

## Connected Pins
```
VCC  - 3V3
RST  - GP22
GND  - GND
IRQ  - x
MISO - GP4 (SPI0 RX)
MOSI - GP7 (SPI0 TX)
SCK  - GP6
SDA  - GP5
```

## Copy adafrui library
Please upload below lib files to `CIRCUITPY/lib` folder 
* [./lib/mfrc522.py](./lib/mfrc522.py)
* [./lib/decode_ndef.py](./lib/decode_ndef.py)
* [./lib/decode_TLV.py](./lib/decode_TLV.py)


# References
* https://github.com/domdfcoding/circuitpython-mfrc522
* https://github.com/zemyblue/pico_micropython_test/tree/main/tests/mfrc522
