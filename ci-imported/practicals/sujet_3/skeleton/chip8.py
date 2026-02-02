import time

from skeleton.bits import Bits
from skeleton.cpu import Cpu

class Chip8(Cpu):
    def __init__(self, random):
        super().__init__(random)

    def execute_op(self):
        instruction = self.memory.read_short(self.PC)
        op = Bits.get_nibble(instruction, 0)
        # print(str(op.value) + " " + str(instruction.value))

        # Dictionary of operation handlers
        op_handlers = {
            0x0: self.handle_0, 0x1: self.handle_1, 0x2: self.handle_2, 0x3: self.handle_3,
            0x4: self.handle_4, 0x5: self.handle_5, 0x6: self.handle_6, 0x7: self.handle_7,
            0x8: self.handle_8, 0x9: self.handle_9, 0xA: self.handle_A, 0xB: self.handle_B,
            0xC: self.handle_C, 0xD: self.handle_D, 0xE: self.handle_E, 0xF: self.handle_F
        }

        # Get the operation handler based on the opcode
        exec_handler = op_handlers.get(op.value, None)

        if exec_handler is None:
            raise ValueError("Operation doesn't exist")

        # Handle infinite loop case
        if op == 0x1 and Bits.get_nnn(instruction) == self.PC:
            return False

        exec_handler(instruction)
        # print("RegF: " + str(self.memory.registers[0xf]))
        # print("I: " + str(self.I.value))
        return True

    def run_program(self):
        while self.execute_op():
            if self.delay_timer > 0:
                self.delay_timer -= 1
            if self.sound_timer > 0:
                self.sound_timer -= 1
            self.display.draw()
            self.display.update()
            time.sleep(.001)
