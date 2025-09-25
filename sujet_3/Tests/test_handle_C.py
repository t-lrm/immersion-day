import random
from EmuDev.cpu import Cpu
from Moulinette.unit_test import AssertEqualAfterExecution, AssertEqual
from Moulinette.test_suite import TestSuite

# When running 'rng.randint(0, 255)' the values will be 0x39, 0x0C, 0x8C, 0x7D, 0x72, 0x47, 0x34
cpu = Cpu(random.Random(42))

test_handle_C = TestSuite(cpu.handle_C)


def reg(x: int):
    return cpu.memory.registers[x]


test_handle_C.add(AssertEqualAfterExecution([0xC000], lambda: reg(0x0), 0x00))
test_handle_C.add(AssertEqualAfterExecution([0xC004], lambda: reg(0x0), 0x04))
test_handle_C.add(AssertEqualAfterExecution([0xC0A7], lambda: reg(0x0), 0x84))

test_handle_C.add(AssertEqual(lambda: cpu.PC, 0x206))

if __name__ == "__main__":
    test_handle_C.run()
