from sujet_3.EmuDev.cpu import Cpu
from sujet_3.Moulinette.unit_test import AssertEqualAfterExecution
from sujet_3.Moulinette.test_suite import TestSuite

cpu = Cpu()

test_handle_9 = TestSuite(cpu.handle_9)

cpu.memory.registers[0x0] = 0x12
cpu.memory.registers[0x2] = 0x12
cpu.memory.registers[0xF] = 0x88

test_handle_9.add(AssertEqualAfterExecution([0x9010], lambda: cpu.PC, 0x204))
test_handle_9.add(AssertEqualAfterExecution([0x9100], lambda: cpu.PC, 0x208))
test_handle_9.add(AssertEqualAfterExecution([0x9FA0], lambda: cpu.PC, 0x20C))
test_handle_9.add(AssertEqualAfterExecution([0x9AF0], lambda: cpu.PC, 0x210))
test_handle_9.add(AssertEqualAfterExecution([0x9020], lambda: cpu.PC, 0x212))
test_handle_9.add(AssertEqualAfterExecution([0x9200], lambda: cpu.PC, 0x214))
test_handle_9.add(AssertEqualAfterExecution([0x9AB0], lambda: cpu.PC, 0x216))

if __name__ == "__main__":
    test_handle_9.run()
