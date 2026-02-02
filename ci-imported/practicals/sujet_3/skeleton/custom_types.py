import operator


class FixedSizeInteger:
    def __init__(self, size: int, value: int | object) -> None:
        """
        Initializes a new Type object that simulates a fixed-size type in C#.

        :param size: The number of bits used to store the value.
        :param value: The value to be stored, which will be confined to the specified size.
        """
        self.max = 2**size
        self._size = size
        self.value = 0

        if isinstance(value, int):
            self._value = value
        elif isinstance(value, FixedSizeInteger):
            self._value = value.value
        else:
            raise TypeError(f"The type {type(value)} is not supported expected.")

    @property
    def size(self):
        """Gets number of bits used to store the value."""
        return self._size

    @property
    def max_value(self):
        """Gets the value stored in the type."""
        return 2**self._size - 1

    @property
    def value(self):
        """Gets the value stored in the type."""
        return self._value % (2**self._size)

    @value.setter
    def value(self, new_value):
        """Sets the value, modulo the maximum allowed value for the size."""
        self._value = new_value % (2**self._size)

    def binary(self):
        return format(self.value, f"0{self.size}b")

    def _operation(self, other, operation):
        if isinstance(other, int):
            output = FixedSizeInteger(self._size, 0)
            output._value = operation(self._value, other)
            return output

        if not isinstance(other, FixedSizeInteger):
            raise ValueError(f"Cannot do operations between {type(self)} and {type(other)}")

        if self._size != other._size:
            raise ValueError("You're trying to do an operation between two numbers of different size")

        output = FixedSizeInteger(self._size, self.value)
        output._value = operation(self._value, other.value)
        return output

    def _comparison(self, other, comparison):
        if isinstance(other, int):
            return comparison(self.value, other)

        if not isinstance(other, FixedSizeInteger):
            raise ValueError(f"Cannot do comparisons between {type(self)} and {type(other)}")

        if self._size != other._size:
            raise ValueError("You're trying to do an comparison between two numbers of different size")

        return comparison(self.value, other.value)

    def __repr__(self):
        return str(self.value)

    def __add__(self, other):  # obj + other
        return self._operation(other, operator.add)

    def __radd__(self, other):  # other + obj
        return self._operation(other, operator.add)

    def __sub__(self, other):  # obj - other
        return self._operation(other, operator.sub)

    def __rsub__(self, other):  # other - obj
        return self._operation(other, operator.sub)

    def __mul__(self, other):  # obj * other
        return self._operation(other, operator.mul)

    def __rmul__(self, other):  # other * obj
        return self._operation(other, operator.mul)

    def __floordiv__(self, other):  # obj // other
        return self._operation(other, operator.floordiv)

    def __rfloordiv__(self, other):  # other // obj
        return self._operation(other, operator.floordiv)

    def __mod__(self, other):  # obj % other
        return self._operation(other, operator.mod)

    def __rmod__(self, other):  # other % mod
        return self._operation(other, operator.mod)

    def __lshift__(self, other):  # obj << other (bitwise left shift)
        return self._operation(other, operator.lshift)

    def __rlshift__(self, other):  # other  << obj(bitwise left shift)
        return self._operation(other, operator.lshift)

    def __rshift__(self, other):  # obj >> other (bitwise right shift)
        return self._operation(other, operator.rshift)

    def __rrshift__(self, other):  # other >> obj (bitwise right shift)
        return self._operation(other, operator.rshift)

    def __and__(self, other):  # obj & other (bitwise AND)
        return self._operation(other, operator.and_)

    def __rand__(self, other):  # other & obj (bitwise AND)
        return self._operation(other, operator.and_)

    def __or__(self, other):  # obj | other (bitwise OR)
        return self._operation(other, operator.or_)

    def __ror__(self, other):  # other | obj (bitwise OR)
        return self._operation(other, operator.or_)

    def __xor__(self, other):  # obj ^ other (bitwise XOR)
        return self._operation(other, operator.xor)

    def __rxor__(self, other):  # other ^ obj (bitwise XOR)
        return self._operation(other, operator.xor)

    def __invert__(self):  # ~obj (bitwise NOT)
        return FixedSizeInteger(self._size, operator.invert(self.value))

    def __eq__(self, other):  # obj == other
        return self._comparison(other, operator.eq)

    def __ne__(self, other):  # obj != other
        return self._comparison(other, operator.ne)

    def __lt__(self, other):  # obj < other
        return self._comparison(other, operator.lt)

    def __gt__(self, other):  # obj > other
        return self._comparison(other, operator.gt)

    def __le__(self, other):  # obj <= other
        return self._comparison(other, operator.le)

    def __ge__(self, other):  # obj >= other
        return self._comparison(other, operator.ge)

    def __str__(self):
        return str(self.value)

    def __index__(self):
        # Return an integer representation of the object
        return int(self.value)


class Byte(FixedSizeInteger):
    def __init__(self, value):
        super().__init__(8, value)


class UShort(FixedSizeInteger):
    def __init__(self, value):
        super().__init__(16, value)


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def count(self):
        return len(self.stack)

    def clear(self):
        self.stack.clear()
