from EmuDev.cpu import Cpu
from Moulinette.unit_test import AssertEqualAfterExecution, AssertEqual
from Moulinette.test_suite import TestSuite

cpu = Cpu()

test_handle_6 = TestSuite(cpu.handle_6)

test_handle_6.add(AssertEqualAfterExecution([0x6010], lambda: cpu.PC, 0x202))
test_handle_6.add(AssertEqual(lambda: cpu.memory.registers.__getitem__(0x0), 0x10))
test_handle_6.add(AssertEqualAfterExecution([0x6BFF], lambda: cpu.PC, 0x204))
test_handle_6.add(AssertEqual(lambda: cpu.memory.registers.__getitem__(0xB), 0xFF))
test_handle_6.add(AssertEqualAfterExecution([0x6ABC], lambda: cpu.PC, 0x206))
test_handle_6.add(AssertEqual(lambda: cpu.memory.registers.__getitem__(0xA), 0xBC))

# TODO: maybe add some tests to ensure the rest of the register are intact

if __name__ == "__main__":
    test_handle_6.run()
