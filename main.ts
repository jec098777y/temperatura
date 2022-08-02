I2C_LCD1602.LcdInit(63)
radio.setTransmitPower(7)
radio.setGroup(2)
basic.forever(function on_forever() {
    let temperatura = dstemp.celsius(DigitalPin.P7)
    radio.sendString("" + temperatura)
    I2C_LCD1602.ShowString("" + temperatura, 0, 0)
    pause(500)
    
})
