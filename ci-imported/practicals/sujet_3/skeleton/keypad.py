import keyboard
from EmuDev.custom_types import UShort


class Keypad:

    @staticmethod
    def is_pressed(keycode: UShort):
        key_mapping = {
            0x1: '1', 0x2: '2', 0x3: '3', 0xc: '4',
            0x4: 'q', 0x5: 'w', 0x6: 'e', 0xd: 'r',
            0x7: 'a', 0x8: 's', 0x9: 'd', 0xe: 'f',
            0xa: 'z', 0x0: 'x', 0xb: 'c', 0xf: 'v'
        }

        char = key_mapping.get(int(keycode))
        return bool(char and keyboard.is_pressed(char))
