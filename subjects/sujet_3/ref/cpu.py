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
        nnn = Bits.get_nnn(opcode)

        if nnn == 0xE0:
            for i in range(2048):
                self.display[i] = False
        elif nnn == 0xEE:
            if self.stack.count() == 0:
                raise IndexError("The stack is empty.")
            self.PC = self.stack.pop()
        else:
            raise Exception("Unhandled 0NNN: " + str(opcode.value))

        self.done()

    def handle_1(self, opcode):
        self.PC = Bits.get_nnn(opcode)

    def handle_2(self, opcode):
        self.stack.push(self.PC)
        self.PC = Bits.get_nnn(opcode)

    def handle_3(self, opcode):
        self.skip_if(self.memory.registers[Bits.get_x(opcode)] == Byte(Bits.get_nn(opcode)))

    def handle_4(self, opcode):
        self.skip_if(self.memory.registers[Bits.get_x(opcode)] != Byte(Bits.get_nn(opcode)))

    def handle_5(self, opcode):
        self.skip_if(self.memory.registers[Bits.get_x(opcode)] == self.memory.registers[Bits.get_y(opcode)])

    def handle_6(self, opcode):
        self.memory.registers[Bits.get_x(opcode)] = Byte(Bits.get_nn(opcode))
        self.done()

    def handle_7(self, opcode):
        self.memory.registers[Bits.get_x(opcode)] += Byte(Bits.get_nn(opcode))
        self.done()

    def handle_8(self, opcode):
        x = Bits.get_x(opcode)
        y = Bits.get_y(opcode)
        n = Bits.get_nibble(opcode, 3)

        match n:
            case 0x0:
                self.memory.registers[x] = self.memory.registers[y]
            case 0x1:
                self.memory.registers[x] |= self.memory.registers[y]
            case 0x2:
                self.memory.registers[x] &= self.memory.registers[y]
            case 0x3:
                self.memory.registers[x] ^= self.memory.registers[y]
            case 0x4:
                overflow = self.memory.registers[x].value + self.memory.registers[y].value > 0xFF
                sum_val = self.memory.registers[x] + self.memory.registers[y]
                self.memory.registers[0xF] = Byte(1) if overflow else Byte(0)
                self.memory.registers[x] = sum_val
            case 0x5:
                overflow = self.memory.registers[x].value - self.memory.registers[y].value < 0
                diff_val = self.memory.registers[x] - self.memory.registers[y]
                self.memory.registers[0xF] = Byte(0) if overflow else Byte(1)
                self.memory.registers[x] = diff_val
            case 0x6:
                self.memory.registers[0xF] = self.memory.registers[x] & 0x1
                self.memory.registers[x] >>= 1
            case 0x7:
                overflow = self.memory.registers[y].value - self.memory.registers[x].value < 0
                diff_val = self.memory.registers[y] - self.memory.registers[x]
                self.memory.registers[0xF] = Byte(1) if overflow else Byte(0)
                self.memory.registers[x] = diff_val
            case 0xE:
                self.memory.registers[0xF] = 1 if (self.memory.registers[x] & 0x80) == 0x80 else 0
                self.memory.registers[x] <<= 1
            case _:
                raise Exception("Invalid operation")

        self.done()

    def handle_9(self, opcode):
        self.skip_if(self.memory.registers[Bits.get_x(opcode)] != self.memory.registers[Bits.get_y(opcode)])

    def handle_A(self, opcode):
        self.I = Bits.get_nnn(opcode)
        self.done()

    def handle_B(self, opcode):
        self.PC = Bits.get_nnn(opcode) + UShort(self.memory.registers[0])

    def handle_C(self, opcode):
        self.memory.registers[Bits.get_x(opcode)] = Bits.get_nn(opcode) & self.rng.randint(0, 255)
        self.done()

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
        key = self.memory.registers[Bits.get_x(opcode)]
        pressed = Keypad.is_pressed(key)
        cond = pressed if Bits.get_nn(opcode) == 0x9E else not pressed
        self.skip_if(cond)

    def handle_F(self, opcode):
        x = Bits.get_x(opcode)
        nn = Bits.get_nn(opcode)

        match nn:
            case 0x07:
                self.memory.registers[x] = self.delay_timer
            case 0x0A:
                index = -1
                for i in range(16):
                    if not Keypad.is_pressed(i):
                        continue
                    index = i
                    break
                if index != -1:
                    self.memory.registers[x] = Byte(index)
            case 0x15:
                self.delay_timer = self.memory.registers[x]
            case 0x18:
                self.sound_timer = self.memory.registers[x]
            case 0x1E:
                self.I += UShort(self.memory.registers[x])
            case 0x29:
                self.I = 5 * UShort(self.memory.registers[x])
            case 0x33:
                self.memory.ram[self.I] = Byte(self.memory.registers[x] // 100)
                self.memory.ram[self.I + 1] = Byte((self.memory.registers[x] // 10) % 10)
                self.memory.ram[self.I + 2] = Byte(self.memory.registers[x] % 10)
            case 0x55:
                for i in range(x + 1):
                    self.memory.ram[self.I + i] = self.memory.registers[i]
            case 0x65:
                for i in range(x + 1):
                    self.memory.registers[i] = self.memory.ram[self.I + i]
            case _:
                raise Exception("Invalid instruction")

        self.done()
