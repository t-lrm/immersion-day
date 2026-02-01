import random

from EmuDev.custom_types import UShort, Byte, Stack
from EmuDev.memory import Memory
from EmuDev.screen import Display
from EmuDev.keypad import Keypad
from EmuDev.bits import Bits


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
        ...

    def handle_1(self, opcode):
        ...

    def handle_2(self, opcode):
        ...

    def handle_3(self, opcode):
        ...

    def handle_4(self, opcode):
        ...

    def handle_5(self, opcode):
        ...

    def handle_6(self, opcode):
        ...

    def handle_7(self, opcode):
        ...

    def handle_8(self, opcode):
        x = Bits.get_x(opcode)
        y = Bits.get_y(opcode)
        n = Bits.get_nibble(opcode, 3)

        match n:
            case 0x0:  # 8XY0
                ...
            case 0x1:  # 8XY1
                ...
            case 0x2:  # 8XY2
                ...
            case 0x3:  # 8XY3
                ...
            case 0x4:  # 8XY4
                ...
            case 0x5:  # 8XY5
                ...
            case 0x6:  # 8XY6
                ...
            case 0x7:  # 8XY7
                ...
            case 0xE:  # 8XYE
                ...
            case _:
                raise Exception("Invalid operation")

        self.done()

    def handle_9(self, opcode):
        ...

    def handle_A(self, opcode):
        ...

    def handle_B(self, opcode):
        ...

    def handle_C(self, opcode):
        ...

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
        ...

    def handle_F(self, opcode):
        x = Bits.get_x(opcode)
        nn = Bits.get_nn(opcode)

        match nn:
            case 0x07:  # FX07
                ...
            case 0x0A:  # FX0A
                ...
            case 0x15:  # FX15
                ...
            case 0x18:  # FX18
                ...
            case 0x1E:  # FX1E
                ...
            case 0x29:  # FX29
                ...
            case 0x33:  # FX33
                ...
            case 0x55:  # FX55
                ...
            case 0x65:  # FX65
                ...
            case _:
                raise Exception("Invalid instruction")

        self.done()
