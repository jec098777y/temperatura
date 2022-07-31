I2C_LCD1602.LcdInit(63)
basic.forever(function on_forever() {
    I2C_LCD1602.ShowString("czas", 0, 0)
    pause(500)
    
})
