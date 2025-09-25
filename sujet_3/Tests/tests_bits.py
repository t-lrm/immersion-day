from sujet_3.Skeleton import bits
from sujet_3.Moulinette.unit_test import AssertOutput
from sujet_3.Moulinette.moulinette import Moulinette, TestSuite

moulinette = Moulinette()

test_get_nibble = TestSuite(bits.Bits.get_nibble)
test_get_nibble.add(AssertOutput([0xABCD, 0], 0xA))
test_get_nibble.add(AssertOutput([0xABCD, 1], 0xB))
test_get_nibble.add(AssertOutput([0xABCD, 2], 0xC))
test_get_nibble.add(AssertOutput([0xABCD, 3], 0xD))
test_get_nibble.add(AssertOutput([0x000F, 0], 0x0))
test_get_nibble.add(AssertOutput([0x00FF, 1], 0x0))
test_get_nibble.add(AssertOutput([0x0FFF, 2], 0xF))
test_get_nibble.add(AssertOutput([0xFFFF, 3], 0xF))

test_get_n = TestSuite(bits.Bits.get_n)
test_get_n.add(AssertOutput([0xABCD], 0xD))
test_get_n.add(AssertOutput([0x0], 0x0))
test_get_n.add(AssertOutput([0x1], 0x1))
test_get_n.add(AssertOutput([0xFFF0], 0x0))
test_get_n.add(AssertOutput([0x2584], 0x4))
test_get_n.add(AssertOutput([0x7F], 0xF))

test_get_nn = TestSuite(bits.Bits.get_nn)
test_get_nn.add(AssertOutput([0xABCD], 0xCD))
test_get_nn.add(AssertOutput([0x00F0], 0xF0))
test_get_nn.add(AssertOutput([0x0010], 0x10))
test_get_nn.add(AssertOutput([0x0001], 0x01))
test_get_nn.add(AssertOutput([0x2584], 0x84))
test_get_nn.add(AssertOutput([0x007F], 0x7F))

test_get_nnn = TestSuite(bits.Bits.get_nnn)
test_get_nnn.add(AssertOutput([0xABCD], 0xBCD))
test_get_nnn.add(AssertOutput([0x0F00], 0xF00))
test_get_nnn.add(AssertOutput([0x0100], 0x100))
test_get_nnn.add(AssertOutput([0x000F], 0x00F))
test_get_nnn.add(AssertOutput([0x2584], 0x584))

test_get_x = TestSuite(bits.Bits.get_x)
test_get_x.add(AssertOutput([0xABCD], 0xB))
test_get_x.add(AssertOutput([0x00F0], 0x0))
test_get_x.add(AssertOutput([0x1234], 0x2))
test_get_x.add(AssertOutput([0x8AF2], 0xA))

test_get_y = TestSuite(bits.Bits.get_y)
test_get_y.add(AssertOutput([0xABCD], 0xC))
test_get_y.add(AssertOutput([0x00F0], 0xF))
test_get_y.add(AssertOutput([0x0010], 0x1))
test_get_y.add(AssertOutput([0x0001], 0x0))
test_get_y.add(AssertOutput([0x2584], 0x8))
test_get_y.add(AssertOutput([0x007F], 0x7))

moulinette.add_test(test_get_nibble)
moulinette.add_test(test_get_n)
moulinette.add_test(test_get_nn)
moulinette.add_test(test_get_nnn)
moulinette.add_test(test_get_x)
moulinette.add_test(test_get_y)

if __name__ == "__main__":
    moulinette.run_all()
