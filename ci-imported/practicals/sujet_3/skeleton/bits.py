from skeleton.custom_types import UShort, Byte


class Bits:

    @staticmethod
    def get_nibble(instruction: UShort, n: int) -> Byte:
        raise NotImplementedError

    @staticmethod
    def get_n(instruction: UShort) -> Byte:
        raise NotImplementedError

    @staticmethod
    def get_nn(instruction: UShort) -> Byte:
        raise NotImplementedError

    @staticmethod
    def get_nnn(instruction: UShort) -> UShort:
        raise NotImplementedError

    @staticmethod
    def get_x(instruction: UShort) -> Byte:
        raise NotImplementedError

    @staticmethod
    def get_y(instruction: UShort) -> Byte:
        raise NotImplementedError
