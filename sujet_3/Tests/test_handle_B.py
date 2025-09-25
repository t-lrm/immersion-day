from EmuDev.cpu import Cpu
from Moulinette.unit_test import AssertEqualAfterExecution, Execute
from Moulinette.test_suite import TestSuite

cpu = Cpu()

test_handle_B = TestSuite(cpu.handle_B)


def set_reg0(x: int):
    cpu.memory.registers[0] = x


test_handle_B.add(AssertEqualAfterExecution([0xB000], lambda: cpu.PC, 0x0000))
test_handle_B.add(Execute(lambda: set_reg0(0xFF)))
test_handle_B.add(AssertEqualAfterExecution([0xB000], lambda: cpu.PC, 0x00FF))
test_handle_B.add(AssertEqualAfterExecution([0xBFFF], lambda: cpu.PC, 0x10FE))
test_handle_B.add(AssertEqualAfterExecution([0xB001], lambda: cpu.PC, 0x0100))
test_handle_B.add(Execute(lambda: set_reg0(0xBC)))
test_handle_B.add(AssertEqualAfterExecution([0xB000], lambda: cpu.PC, 0x00BC))
test_handle_B.add(AssertEqualAfterExecution([0xB09D], lambda: cpu.PC, 0x0159))
test_handle_B.add(AssertEqualAfterExecution([0xB001], lambda: cpu.PC, 0x00BD))

if __name__ == "__main__":
    test_handle_B.run()
