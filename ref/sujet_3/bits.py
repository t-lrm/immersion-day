from EmuDev.custom_types import UShort, Byte


class Bits:

    @staticmethod
    def get_nibble(instruction: UShort, n: int) -> Byte:
        return Byte((instruction >> (12 - n * 4)) & 0xF)

    @staticmethod
    def get_n(instruction: UShort) -> Byte:
        return Byte(instruction & 0xF)

    @staticmethod
    def get_nn(instruction: UShort) -> Byte:
        return Byte(instruction & 0xFF)

    @staticmethod
    def get_nnn(instruction: UShort) -> UShort:
        return UShort(instruction & 0xFFF)

    @staticmethod
    def get_x(instruction: UShort) -> Byte:
        return Byte((instruction >> 8) & 0xF)

    @staticmethod
    def get_y(instruction: UShort) -> Byte:
        return Byte((instruction >> 4) & 0xF)
