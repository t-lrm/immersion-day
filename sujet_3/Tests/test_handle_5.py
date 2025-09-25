from sujet_3.EmuDev.cpu import Cpu
from sujet_3.Moulinette.unit_test import AssertEqualAfterExecution
from sujet_3.Moulinette.test_suite import TestSuite

cpu = Cpu()

test_handle_5 = TestSuite(cpu.handle_5)

cpu.memory.registers[0x0] = 0x12
cpu.memory.registers[0x1] = 0x12
cpu.memory.registers[0xF] = 0x88
cpu.memory.registers[0xA] = 0x88

test_handle_5.add(AssertEqualAfterExecution([0x5010], lambda: cpu.PC, 0x204))
test_handle_5.add(AssertEqualAfterExecution([0x5100], lambda: cpu.PC, 0x208))
test_handle_5.add(AssertEqualAfterExecution([0x5FA0], lambda: cpu.PC, 0x20C))
test_handle_5.add(AssertEqualAfterExecution([0x5FA0], lambda: cpu.PC, 0x210))
test_handle_5.add(AssertEqualAfterExecution([0x55B0], lambda: cpu.PC, 0x214))
test_handle_5.add(AssertEqualAfterExecution([0x50F0], lambda: cpu.PC, 0x216))
test_handle_5.add(AssertEqualAfterExecution([0x5F00], lambda: cpu.PC, 0x218))
test_handle_5.add(AssertEqualAfterExecution([0x5F70], lambda: cpu.PC, 0x21A))

if __name__ == "__main__":
    test_handle_5.run()
