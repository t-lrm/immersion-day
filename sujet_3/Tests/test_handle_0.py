from sujet_3.EmuDev.cpu import Cpu
from sujet_3.Moulinette.unit_test import AssertEqualAfterExecution, ThrowException
from sujet_3.Moulinette.moulinette import TestSuite

cpu = Cpu()

cpu.display._memory = [True] * 2048
display = [False] * 2048
cpu.stack.push(0xD)

test_handle_0 = TestSuite(cpu.handle_0)
test_handle_0.add(AssertEqualAfterExecution([0xE0], lambda: cpu.display._memory, display))
test_handle_0.add(AssertEqualAfterExecution([0xEE], lambda: cpu.PC, 0xF))
test_handle_0.add(ThrowException([0x00EE], IndexError))
test_handle_0.add(ThrowException([0xEEEE], Exception))

if __name__ == "__main__":
    test_handle_0.run()
