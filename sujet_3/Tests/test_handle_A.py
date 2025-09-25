from sujet_3.EmuDev.cpu import Cpu
from sujet_3.Moulinette.unit_test import AssertEqualAfterExecution
from sujet_3.Moulinette.test_suite import TestSuite

cpu = Cpu()

test_handle_A = TestSuite(cpu.handle_A)

test_handle_A.add(AssertEqualAfterExecution([0xA000], lambda: cpu.I, 0x000))
test_handle_A.add(AssertEqualAfterExecution([0xAFFF], lambda: cpu.I, 0xFFF))
test_handle_A.add(AssertEqualAfterExecution([0xACDC], lambda: cpu.I, 0xCDC))
test_handle_A.add(AssertEqualAfterExecution([0xA7B5], lambda: cpu.I, 0x7B5))



if __name__ == "__main__":
    test_handle_A.run()
