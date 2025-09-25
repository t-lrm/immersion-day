from sujet_3.EmuDev.cpu import Cpu
from sujet_3.Moulinette.unit_test import AssertEqualAfterExecution, AssertEqual
from sujet_3.Moulinette.moulinette import TestSuite

cpu = Cpu()

test_handle_2 = TestSuite(cpu.handle_2)
test_handle_2.add(AssertEqual(lambda: cpu.PC, 0x200))
test_handle_2.add(AssertEqualAfterExecution([0x0], lambda: cpu.PC, 0x0))
test_handle_2.add(AssertEqual(cpu.stack.peek, 0x200))
test_handle_2.add(AssertEqualAfterExecution([0xFFF], lambda: cpu.PC, 0x0FFF))
test_handle_2.add(AssertEqual(cpu.stack.peek, 0x0))

if __name__ == "__main__":
    test_handle_2.run()
