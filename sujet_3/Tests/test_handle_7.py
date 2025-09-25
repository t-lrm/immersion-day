from sujet_3.EmuDev.cpu import Cpu
from sujet_3.Moulinette.unit_test import AssertEqualAfterExecution, AssertEqual
from sujet_3.Moulinette.test_suite import TestSuite

cpu = Cpu()

test_handle_7 = TestSuite(cpu.handle_7)

cpu.memory.registers[0xA] = 0xFFFF

test_handle_7.add(AssertEqualAfterExecution([0x7010], lambda: cpu.PC, 0x202))
test_handle_7.add(AssertEqualAfterExecution([0x7035], lambda: cpu.PC, 0x204))
test_handle_7.add(AssertEqualAfterExecution([0x70A7], lambda: cpu.PC, 0x206))
test_handle_7.add(AssertEqual(lambda: cpu.memory.registers.__getitem__(0x0), 0xEC))

test_handle_7.add(AssertEqualAfterExecution([0x7A01], lambda: cpu.PC, 0x208))
test_handle_7.add(AssertEqual(lambda: cpu.memory.registers.__getitem__(0xA), 0x00))

if __name__ == "__main__":
    test_handle_7.run()
