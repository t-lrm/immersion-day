from sujet_3.Skeleton.cpu import Cpu
from sujet_3.Moulinette.unit_test import AssertEqualAfterExecution, Execute
from sujet_3.Moulinette.test_suite import TestSuite

cpu = Cpu()

test_handle_4 = TestSuite(cpu.handle_4)

for i in range(16):  # 0x4000, 0x4100 , 0x4200 , ..., 0x4F00
    test_handle_4.add(AssertEqualAfterExecution([0x4000 + i * 16 ** 2], lambda: cpu.PC, 0x200 + (i + 1) * 2))

# 'cpu.memory.registers.__setitem__(0x0, 0xFF)' is equivalent to 'cpu.memory.registers.[0x0] = 0xFF'
test_handle_4.add(Execute(lambda: cpu.memory.registers.__setitem__(0x0, 0xFF)))
test_handle_4.add(Execute(lambda: cpu.memory.registers.__setitem__(0x7, 0x99)))
test_handle_4.add(Execute(lambda: cpu.memory.registers.__setitem__(0xF, 0xAB)))

test_handle_4.add(AssertEqualAfterExecution([0x40FF], lambda: cpu.PC, 0x222))
test_handle_4.add(AssertEqualAfterExecution([0x4799], lambda: cpu.PC, 0x224))
test_handle_4.add(AssertEqualAfterExecution([0x4FAB], lambda: cpu.PC, 0x226))
test_handle_4.add(AssertEqualAfterExecution([0x4042], lambda: cpu.PC, 0x22A))
test_handle_4.add(AssertEqualAfterExecution([0x42FF], lambda: cpu.PC, 0x22E))

if __name__ == "__main__":
    test_handle_4.run()
