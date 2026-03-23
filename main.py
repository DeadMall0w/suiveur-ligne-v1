maqueenPlusV2.i2c_init()
basic.show_leds("""
    # . . . #
    . . . # .
    . # # . #
    . # . # #
    . . # # .
    """)

def on_forever():
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        255)
    basic.show_leds("""
        # . # . #
        . . . . .
        . . # . .
        . . . . .
        . . # . .
        """)
basic.forever(on_forever)
