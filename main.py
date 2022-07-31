I2C_LCD1602.lcd_init(63)


def on_forever():
    
    I2C_LCD1602.show_string("czas", 0, 0)
            
    pause(500)
    pass
basic.forever(on_forever)
