I2C_LCD1602.lcd_init(63)
radio.set_transmit_power(7)
radio.set_group(2)
def on_forever():
    temperatura = dstemp.celsius(DigitalPin.P7)
    
    radio.send_string(str(temperatura))
    I2C_LCD1602.show_string(str(temperatura), 0, 0)
    pause(500)
    pass
basic.forever(on_forever)
