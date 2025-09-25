from sujet_3.EmuDev.custom_types import UShort, Byte


class Bits:

    @staticmethod
    def get_nibble(instruction: UShort, n: int) -> Byte:
        ...

    @staticmethod
    def get_n(instruction: UShort) -> Byte:
        ...

    @staticmethod
    def get_nn(instruction: UShort) -> Byte:
        ...

    @staticmethod
    def get_nnn(instruction: UShort) -> UShort:
        ...

    @staticmethod
    def get_x(instruction: UShort) -> Byte:
        ...

    @staticmethod
    def get_y(instruction: UShort) -> Byte:
        ...
