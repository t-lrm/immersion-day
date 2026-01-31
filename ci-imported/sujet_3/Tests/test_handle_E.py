from sujet_3.Skeleton.cpu import Cpu
from sujet_3.EmuDev.keypad import Keypad
from sujet_3.EmuDev.custom_types import Byte
from sujet_3.Moulinette.unit_test import AssertEqualAfterExecution
from sujet_3.Moulinette.test_suite import TestSuite


def is_pressed(keycode: Byte):
    return {
        0x1: True, 0x2: False, 0x3: False, 0xc: False,
        0x4: False, 0x5: False, 0x6: False, 0xd: False,
        0x7: False, 0x8: False, 0x9: True, 0xe: False,
        0xa: False, 0x0: False, 0xb: False, 0xf: True
    }[int(keycode)]


cpu = Cpu()
cpu.memory.registers[0x1] = Byte(0x1)
cpu.memory.registers[0x6] = Byte(0x9)
cpu.memory.registers[0xB] = Byte(0xF)
cpu.memory.registers[0xC] = Byte(0x8)
Keypad.is_pressed = is_pressed

test_handle_E = TestSuite(cpu.handle_E)

# 0xEX9E
test_handle_E.add(AssertEqualAfterExecution([0xE19E], lambda: cpu.PC, 0x204))
test_handle_E.add(AssertEqualAfterExecution([0xE69E], lambda: cpu.PC, 0x208))
test_handle_E.add(AssertEqualAfterExecution([0xEB9E], lambda: cpu.PC, 0x20C))
test_handle_E.add(AssertEqualAfterExecution([0xE49E], lambda: cpu.PC, 0x20E))
test_handle_E.add(AssertEqualAfterExecution([0xEC9E], lambda: cpu.PC, 0x210))

# 0xEXA1
test_handle_E.add(AssertEqualAfterExecution([0xE1A1], lambda: cpu.PC, 0x212))
test_handle_E.add(AssertEqualAfterExecution([0xE6A1], lambda: cpu.PC, 0x214))
test_handle_E.add(AssertEqualAfterExecution([0xEBA1], lambda: cpu.PC, 0x216))
test_handle_E.add(AssertEqualAfterExecution([0xE4A1], lambda: cpu.PC, 0x21A))
test_handle_E.add(AssertEqualAfterExecution([0xECA1], lambda: cpu.PC, 0x21E))

if __name__ == "__main__":
    test_handle_E.run()
