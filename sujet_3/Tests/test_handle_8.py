from sujet_3.Skeleton.cpu import Cpu
from sujet_3.EmuDev.custom_types import Byte
from sujet_3.Moulinette.unit_test import AssertEqualAfterExecution, Execute, AssertEqual
from sujet_3.Moulinette.test_suite import TestSuite

cpu = Cpu()

test_handle_8 = TestSuite(cpu.handle_8)


def reg(x: int):
    return cpu.memory.registers[x]


def init_registers():
    cpu.memory.registers = [Byte(0)] * 16
    cpu.memory.registers[0x1] = Byte(0x12)
    cpu.memory.registers[0x2] = Byte(0xFF)
    cpu.memory.registers[0xB] = Byte(0x07)
    cpu.memory.registers[0xC] = Byte(0x10)
    cpu.memory.registers[0xF] = Byte(0x77)


# 0x8XY0
test_handle_8.add(Execute(init_registers))
test_handle_8.add(AssertEqualAfterExecution([0x8010], lambda: reg(0x0), 0x12))
test_handle_8.add(AssertEqualAfterExecution([0x8FF0], lambda: reg(0xF), 0x77))
test_handle_8.add(AssertEqualAfterExecution([0x8420], lambda: reg(0x4), 0xFF))

# 0x8XY1
test_handle_8.add(Execute(init_registers))
test_handle_8.add(AssertEqualAfterExecution([0x8121], lambda: reg(0x1), 0xFF))
test_handle_8.add(AssertEqualAfterExecution([0x8211], lambda: reg(0x2), 0xFF))
test_handle_8.add(AssertEqualAfterExecution([0x8BC1], lambda: reg(0xB), 0x17))
test_handle_8.add(AssertEqualAfterExecution([0x8BF1], lambda: reg(0xB), 0x77))

# 0x8XY2
test_handle_8.add(Execute(init_registers))
test_handle_8.add(AssertEqualAfterExecution([0x8122], lambda: reg(0x1), 0x12))
test_handle_8.add(AssertEqualAfterExecution([0x8B22], lambda: reg(0xB), 0x07))

# 0x8XY3
test_handle_8.add(Execute(init_registers))
test_handle_8.add(AssertEqualAfterExecution([0x8133], lambda: reg(0x1), 0x12))
test_handle_8.add(AssertEqualAfterExecution([0x8B33], lambda: reg(0xB), 0x07))
test_handle_8.add(AssertEqualAfterExecution([0x82F3], lambda: reg(0x2), 0x88))

# 0x8XY4
test_handle_8.add(Execute(init_registers))
test_handle_8.add(AssertEqualAfterExecution([0x81B4], lambda: reg(0x1), 0x19))
test_handle_8.add(AssertEqual(lambda: reg(0xF), 0x00))
test_handle_8.add(AssertEqualAfterExecution([0x8124], lambda: reg(0x1), 0x18))
test_handle_8.add(AssertEqual(lambda: reg(0xF), 0x01))

# 0x8XY5
test_handle_8.add(Execute(init_registers))
test_handle_8.add(AssertEqualAfterExecution([0x8125], lambda: reg(0x1), 0x13))
test_handle_8.add(AssertEqual(lambda: reg(0xF), 0x01))
test_handle_8.add(AssertEqualAfterExecution([0x8155], lambda: reg(0xF), 0x00))
test_handle_8.add(AssertEqual(lambda: reg(0xF), 0x00))
test_handle_8.add(AssertEqualAfterExecution([0x8C55], lambda: reg(0xC), 0x10))
test_handle_8.add(AssertEqual(lambda: reg(0xF), 0x00))

# 0x8XY6
test_handle_8.add(Execute(init_registers))
test_handle_8.add(AssertEqualAfterExecution([0x8106], lambda: reg(0x1), 0x09))
test_handle_8.add(AssertEqual(lambda: reg(0xF), 0))
test_handle_8.add(AssertEqualAfterExecution([0x8BF6], lambda: reg(0xB), 0x03))
test_handle_8.add(AssertEqual(lambda: reg(0xF), 0x01))

# 0x8XY7
test_handle_8.add(Execute(init_registers))
test_handle_8.add(AssertEqualAfterExecution([0x8217], lambda: reg(0x2), 0x13))
test_handle_8.add(AssertEqual(lambda: reg(0xF), 0x01))
test_handle_8.add(AssertEqualAfterExecution([0x8517], lambda: reg(0x5), 0x12))
test_handle_8.add(AssertEqual(lambda: reg(0xF), 0x00))
test_handle_8.add(AssertEqualAfterExecution([0x8C57], lambda: reg(0x5), 0x12))
test_handle_8.add(AssertEqual(lambda: reg(0xF), 0x00))

# 0x8XYE
test_handle_8.add(Execute(init_registers))
test_handle_8.add(AssertEqualAfterExecution([0x818E], lambda: reg(0x1), 0x24))
test_handle_8.add(AssertEqualAfterExecution([0x8C8E], lambda: reg(0xC), 0x20))

if __name__ == "__main__":
    test_handle_8.run()
