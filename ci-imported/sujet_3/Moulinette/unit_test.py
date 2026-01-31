class UnitTest:
    """
    Base class for unit tests.
    """
    type = "UnitTest"


class AssertOutput(UnitTest):
    type = "AssertOutput"

    def __init__(self, args: list, expected):
        """
        This class is used to assert the output of a function.
        :param args: Arguments to pass to the function (in order).
        :param expected: Expected output of the function.
        """
        self.args = args
        self.expected = expected


class AssertEqualAfterExecution(UnitTest):
    type = "AssertEqualAfterExecution"

    def __init__(self, args: list, variable, expected):
        """
        This class is used to assert the value of a variable after the execution of a function.
        :param args: Arguments to pass to the function (in order).
        :param variable: Lambda expression returning the variable to compare.
        :param expected: Expected value of the mutable variable.
        """
        self.args = args
        self.variable = variable
        self.expected = expected


class AssertEqual(UnitTest):
    type = "AssertEqual"

    def __init__(self, variable, expected):
        """
        This class is used to assert the value of a variable (it's independent of the execution of the function).
        :param variable: Lambda expression returning the variable to compare.
        :param expected: Expected value of the mutable variable.
        """
        self.variable = variable
        self.expected = expected


class AssertNotEqual(UnitTest):
    type = "AssertNotEqual"

    def __init__(self, variable, forbidden: list):
        """
        Assert that the value of the variable is not one of the forbidden values.
        :param variable: Lambda expression returning the variable to compare.
        :param forbidden: A sequence of values that the test value must not equal.
        """
        self.variable = variable
        self.forbidden = forbidden


class ThrowException(UnitTest):
    type = "ThrowException"

    def __init__(self, args: list, exception: Exception, error_message: str = ""):
        """
        This class is used to assert the exception raised by a function.
        :param args: Arguments to pass to the function (in order).
        :param exception: Type of exception to raise.
        :param error_message: Error message to display if the exception is not raised.
        """
        self.args = args
        self.exception = exception
        self.error_message = error_message


class Execute(UnitTest):
    type = "Execute"

    def __init__(self, function, args: list = None):
        """
        Execute a function.
        :param function: Function to execute.
        :param args: Arguments passed into the function.
        """
        self.function = function
        self.args = args
