from sujet_3.Skeleton.cpu import Cpu
from sujet_3.Moulinette.unit_test import AssertEqualAfterExecution, Execute
from sujet_3.Moulinette.test_suite import TestSuite

cpu = Cpu()

test_handle_3 = TestSuite(cpu.handle_3)

for i in range(16):  # 0x3000, 0x3100 , 0x3200 , ..., 0x3F00
    test_handle_3.add(AssertEqualAfterExecution([0x3000 + i * 16 ** 2], lambda: cpu.PC, 0x200 + (i + 1) * 4))

# 'cpu.memory.registers.__setitem__(0x0, 0xFF)' is equivalent to 'cpu.memory.registers.[0x0] = 0xFF'
test_handle_3.add(Execute(lambda: cpu.memory.registers.__setitem__(0x0, 0xFF)))
test_handle_3.add(Execute(lambda: cpu.memory.registers.__setitem__(0x7, 0x99)))
test_handle_3.add(Execute(lambda: cpu.memory.registers.__setitem__(0xF, 0xAB)))

test_handle_3.add(AssertEqualAfterExecution([0x30FF], lambda: cpu.PC, 0x244))
test_handle_3.add(AssertEqualAfterExecution([0x3799], lambda: cpu.PC, 0x248))
test_handle_3.add(AssertEqualAfterExecution([0x3FAB], lambda: cpu.PC, 0x24C))
test_handle_3.add(AssertEqualAfterExecution([0x3042], lambda: cpu.PC, 0x24E))
test_handle_3.add(AssertEqualAfterExecution([0x32FF], lambda: cpu.PC, 0x250))

if __name__ == "__main__":
    test_handle_3.run()
