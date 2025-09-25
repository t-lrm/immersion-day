from sujet_3.EmuDev.cpu import Cpu
from sujet_3.EmuDev.keypad import Keypad
from sujet_3.EmuDev.custom_types import Byte
from sujet_3.Moulinette.unit_test import AssertEqualAfterExecution, Execute, ThrowException
from sujet_3.Moulinette.test_suite import TestSuite

cpu = Cpu()

test_handle_F = TestSuite(cpu.handle_F)

keys = {
    0x1: True, 0x2: False, 0x3: False, 0xc: False,
    0x4: False, 0x5: False, 0x6: False, 0xd: False,
    0x7: False, 0x8: False, 0x9: True, 0xe: False,
    0xa: False, 0x0: False, 0xb: False, 0xf: True
}


def set_key(keycode: Byte, value: bool):
    keys[keycode] = value


def is_pressed(keycode: Byte):
    return keys[int(keycode)]


Keypad.is_pressed = is_pressed


def reg(opcode: int):
    return cpu.memory.registers[opcode]


def set_reg(opcode: int, value: int):
    cpu.memory.registers[opcode] = value


def set_ram(opcode: int, value: int):
    cpu.memory.ram[opcode] = value


def set_I(value: int):
    cpu.I = value


def init_reg():
    reset_cpu()
    cpu.memory.registers[0x1] = Byte(0x12)
    cpu.memory.registers[0x2] = Byte(0xFF)
    cpu.memory.registers[0xB] = Byte(0x07)
    cpu.memory.registers[0xC] = Byte(0x10)
    cpu.memory.registers[0xF] = Byte(0x77)


def init_ram():
    reset_cpu()
    cpu.memory.ram[0x120] = Byte(0x8F)
    cpu.memory.ram[0x123] = Byte(0x47)
    cpu.memory.ram[0x12A] = Byte(0x11)
    cpu.memory.ram[0x12C] = Byte(0xB1)
    cpu.memory.ram[0x12F] = Byte(0x80)


def reset_cpu():
    cpu.memory.registers = [Byte(0x00)] * 16
    cpu.memory.ram = [Byte(0x00)] * 4096


def set_delay_timer(opcode):
    cpu.delay_timer = Byte(opcode)


# 0xFX07
test_handle_F.add(Execute(init_reg))
test_handle_F.add(AssertEqualAfterExecution([0xF007], lambda: reg(0x0), 0x0))
test_handle_F.add(Execute(lambda: set_delay_timer(0x7B)))
test_handle_F.add(AssertEqualAfterExecution([0xFB07], lambda: reg(0xB), 0x7B))
test_handle_F.add(Execute(lambda: set_delay_timer(0xFF)))
test_handle_F.add(AssertEqualAfterExecution([0xFB07], lambda: reg(0xB), 0xFF))

# 0xFX0A
test_handle_F.add(Execute(init_reg))
test_handle_F.add(AssertEqualAfterExecution([0xF00A], lambda: reg(0x0), 0x1))
test_handle_F.add(Execute(lambda: set_key(0x1, False)))
test_handle_F.add(AssertEqualAfterExecution([0xF40A], lambda: reg(0x4), 0x9))
test_handle_F.add(Execute(lambda: set_key(0x9, False)))
test_handle_F.add(AssertEqualAfterExecution([0xFF0A], lambda: reg(0xF), 0xF))

# 0xFX15
test_handle_F.add(Execute(init_reg))
test_handle_F.add(AssertEqualAfterExecution([0xF015], lambda: cpu.delay_timer, 0x0))
test_handle_F.add(AssertEqualAfterExecution([0xF115], lambda: cpu.delay_timer, 0x12))
test_handle_F.add(AssertEqualAfterExecution([0xFF15], lambda: cpu.delay_timer, 0x77))

# 0xFX18
test_handle_F.add(Execute(init_reg))
test_handle_F.add(AssertEqualAfterExecution([0xF018], lambda: cpu.sound_timer, 0x0))
test_handle_F.add(AssertEqualAfterExecution([0xF118], lambda: cpu.sound_timer, 0x12))
test_handle_F.add(AssertEqualAfterExecution([0xFF18], lambda: cpu.sound_timer, 0x77))

# 0xFX1E
test_handle_F.add(Execute(init_reg))
test_handle_F.add(AssertEqualAfterExecution([0xF01E], lambda: cpu.I, 0x0))
test_handle_F.add(AssertEqualAfterExecution([0xF11E], lambda: cpu.I, 0x12))
test_handle_F.add(AssertEqualAfterExecution([0xFF1E], lambda: cpu.I, 0x89))

# 0xFX29
test_handle_F.add(Execute(init_reg))
test_handle_F.add(AssertEqualAfterExecution([0xF029], lambda: cpu.I, 0x0))
test_handle_F.add(AssertEqualAfterExecution([0xF129], lambda: cpu.I, 0x5A))
test_handle_F.add(AssertEqualAfterExecution([0xFF29], lambda: cpu.I, 0x253))

# 0xFX33
test_handle_F.add(Execute(init_reg))
test_handle_F.add(Execute(lambda: set_I(0x123)))
test_handle_F.add(AssertEqualAfterExecution([0xF033], lambda: cpu.memory.ram[cpu.I:cpu.I + 3], [0x00, 0x00, 0x00]))
test_handle_F.add(AssertEqualAfterExecution([0xFF33], lambda: cpu.memory.ram[cpu.I:cpu.I + 3], [0x01, 0x01, 0x09]))
test_handle_F.add(Execute(lambda: set_I(0x000)))
test_handle_F.add(AssertEqualAfterExecution([0xFC33], lambda: cpu.memory.ram[cpu.I:cpu.I + 3], [0x00, 0x01, 0x06]))
test_handle_F.add(AssertEqualAfterExecution([0xF233], lambda: cpu.memory.ram[cpu.I:cpu.I + 3], [0x02, 0x05, 0x05]))

# 0xFX55
test_handle_F.add(Execute(init_reg))
test_handle_F.add(AssertEqualAfterExecution(
    [0xFF55],
    lambda: cpu.memory.ram[cpu.I:cpu.I + 16],
    [0x00, 0x12, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x10, 0x00, 0x00, 0x77]
))
test_handle_F.add(Execute(lambda: set_I(0x123)))
test_handle_F.add(AssertEqualAfterExecution(
    [0xFF55],
    lambda: cpu.memory.ram[cpu.I:cpu.I + 16],
    [0x00, 0x12, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x10, 0x00, 0x00, 0x77]
))
test_handle_F.add(Execute(lambda: set_reg(0x0, 0xFF)))
test_handle_F.add(Execute(lambda: set_reg(0x1, 0xA8)))
test_handle_F.add(Execute(lambda: set_reg(0x4, 0x69)))
test_handle_F.add(Execute(lambda: set_reg(0x7, 0x01)))
test_handle_F.add(Execute(lambda: set_reg(0x8, 0x54)))
test_handle_F.add(Execute(lambda: set_reg(0xF, 0x00)))
test_handle_F.add(AssertEqualAfterExecution(
    [0xF755],
    lambda: cpu.memory.ram[cpu.I:cpu.I + 16],
    [0xFF, 0xA8, 0xFF, 0x00, 0x69, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x07, 0x10, 0x00, 0x00, 0x77]
))

# 0xFX65
test_handle_F.add(Execute(init_ram))
test_handle_F.add(Execute(lambda: set_I(0x120)))
test_handle_F.add(AssertEqualAfterExecution(
    [0xFF65],
    lambda: cpu.memory.registers,
    [0x8F, 0x00, 0x00, 0x47, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x11, 0x00, 0xB1, 0x00, 0x00, 0x80]
))
test_handle_F.add(Execute(lambda: set_I(0x467)))
test_handle_F.add(Execute(lambda: set_ram(0x467, 0x67)))
test_handle_F.add(Execute(lambda: set_ram(0x468, 0x01)))
test_handle_F.add(Execute(lambda: set_ram(0x469, 0xBA)))
test_handle_F.add(AssertEqualAfterExecution(
    [0xF265],
    lambda: cpu.memory.registers,
    [0x67, 0x01, 0xBA, 0x47, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x11, 0x00, 0xB1, 0x00, 0x00, 0x80]
))

# Undefined cases
test_handle_F.add(ThrowException([0xF000], Exception))
test_handle_F.add(ThrowException([0xF123], Exception))
test_handle_F.add(ThrowException([0xFF31], Exception))

if __name__ == "__main__":
    test_handle_F.run()
