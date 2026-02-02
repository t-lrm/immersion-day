import random

from skeleton.custom_types import UShort, Byte, Stack
from skeleton.memory import Memory
from skeleton.screen import Display
from skeleton.keypad import Keypad
from skeleton.bits import Bits


class Cpu:
    def __init__(self, rng=None):

        self.memory = Memory()
        self.display = Display()
        self.stack = Stack()

        self.I: UShort = UShort(0)
        self.PC: UShort = UShort(0x200)
        self.delay_timer: Byte = Byte(0)
        self.sound_timer: Byte = Byte(0)
        self.rng = rng if rng else random.Random()

    def done(self):
        self.PC += 2

    def skip_if(self, condition):
        if condition:
            self.PC += 4
        else:
            self.PC += 2

    def handle_0(self, opcode):
        raise NotImplementedError

    def handle_1(self, opcode):
        raise NotImplementedError

    def handle_2(self, opcode):
        raise NotImplementedError

    def handle_3(self, opcode):
        raise NotImplementedError

    def handle_4(self, opcode):
        raise NotImplementedError

    def handle_5(self, opcode):
        raise NotImplementedError

    def handle_6(self, opcode):
        raise NotImplementedError

    def handle_7(self, opcode):
        raise NotImplementedError

    def handle_8(self, opcode):
        x = Bits.get_x(opcode)
        y = Bits.get_y(opcode)
        n = Bits.get_nibble(opcode, 3)

        match n:
            case 0x0:  # 8XY0
                raise NotImplementedError
            case 0x1:  # 8XY1
                raise NotImplementedError
            case 0x2:  # 8XY2
                raise NotImplementedError
            case 0x3:  # 8XY3
                raise NotImplementedError
            case 0x4:  # 8XY4
                raise NotImplementedError
            case 0x5:  # 8XY5
                raise NotImplementedError
            case 0x6:  # 8XY6
                raise NotImplementedError
            case 0x7:  # 8XY7
                raise NotImplementedError
            case 0xE:  # 8XYE
                raise NotImplementedError
            case _:
                raise Exception("Invalid operation")

        self.done()

    def handle_9(self, opcode):
        raise NotImplementedError

    def handle_A(self, opcode):
        raise NotImplementedError

    def handle_B(self, opcode):
        raise NotImplementedError

    def handle_C(self, opcode):
        raise NotImplementedError

    def handle_D(self, opcode):
        x = self.memory.registers[Bits.get_x(opcode)]
        y = self.memory.registers[Bits.get_y(opcode)]
        height = Bits.get_n(opcode)

        drawn = False
        c = 0
        for i in range(32 * 64):
            if self.display[i]:
                c += 1
        for line_idx in range(height):
            line = self.memory.ram[self.I + line_idx]
            for i in range(8):
                index = (x.value + i + (y.value + line_idx) * 64) % 2048
                bit = (line & 0x80) == 0x80
                line <<= 1
                if bit and self.display[index]:
                    drawn = True
                self.display[index] ^= bit

        self.memory.registers[0xF] = 1 if drawn else 0

        self.done()

    def handle_E(self, opcode):
        raise NotImplementedError

    def handle_F(self, opcode):
        x = Bits.get_x(opcode)
        nn = Bits.get_nn(opcode)

        match nn:
            case 0x07:  # FX07
                raise NotImplementedError
            case 0x0A:  # FX0A
                raise NotImplementedError
            case 0x15:  # FX15
                raise NotImplementedError
            case 0x18:  # FX18
                raise NotImplementedError
            case 0x1E:  # FX1E
                raise NotImplementedError
            case 0x29:  # FX29
                raise NotImplementedError
            case 0x33:  # FX33
                raise NotImplementedError
            case 0x55:  # FX55
                raise NotImplementedError
            case 0x65:  # FX65
                raise NotImplementedError
            case _:
                raise Exception("Invalid instruction")

        self.done()
