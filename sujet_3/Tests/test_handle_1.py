from sujet_3.EmuDev.cpu import Cpu
from sujet_3.Moulinette.unit_test import AssertEqualAfterExecution
from sujet_3.Moulinette.moulinette import TestSuite

cpu = Cpu()

test_handle_1 = TestSuite(cpu.handle_1)
test_handle_1.add(AssertEqualAfterExecution([0x0], lambda: cpu.PC, 0x0))
test_handle_1.add(AssertEqualAfterExecution([0x1A], lambda: cpu.PC, 0x1A))
test_handle_1.add(AssertEqualAfterExecution([0x0FFF], lambda: cpu.PC, 0x0FFF))
test_handle_1.add(AssertEqualAfterExecution([0xFFFF], lambda: cpu.PC, 0x0FFF))

if __name__ == "__main__":
    test_handle_1.run()
