# VibeDeck-6Key i used KMK firmware 

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.macros import Macros, Delay, Press, Release, Tap
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()

# KMK macros and rotary encoder handlimg
macros = Macros()
encoder_handler = EncoderHandler()
keyboard.modules = [macros, encoder_handler]
keyboard.extensions.append(MediaKeys())



keyboard.matrix = KeysScanner(
    pins=(
        board.D10,  # SW1
        board.D9,   # SW2
        board.D8,   # SW3
        board.D3,   # SW4
        board.D4,   # SW5
        board.D5,   # SW6
    ),
    value_when_pressed=False,
    pull=True,
)


encoder_handler.pins = (
    (board.D0, board.D2, board.D1, False, 4),
)

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
]

OPEN_STARDANCE = KC.MACRO(
    Press(KC.LGUI),
    Tap(KC.R),
    Release(KC.LGUI),
    Delay(500),
    "https://stardance.hackclub.com",
    Tap(KC.ENTER),
)


keyboard.keymap = [
    [
        OPEN_STARDANCE,  # SW1 
        KC.B,            # SW2 
        KC.C,            # SW3 
        KC.D,            # SW4 
        KC.E,            # SW5 
        KC.F,            # SW6 
    ]
]

if __name__ == "__main__":
    keyboard.go()
