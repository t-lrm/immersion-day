import traceback
import os
import ast, inspect, textwrap
import io
import sys

from Moulinette.printer import Printer
from Moulinette.unit_test import UnitTest, AssertOutput, AssertEqualAfterExecution, ThrowException, AssertEqual, \
    AssertNotEqual, Execute


class TestSuite:
    def __init__(self, function):
        """
        Initialize the test suite with the function to be tested.
        :param function: Function to be tested.
        """
        self.function = function
        self.tests: list[UnitTest] = []
        self.passed: int = 0
        self.total: int = 0

    def add(self, unit_test: UnitTest) -> object:
        """
        Add a test case to the test suite.
        :param unit_test: UnitTest object.
        """
        self.tests.append(unit_test)

    def run(self):
        """
        Run all the tests in the test suite.
        """
        Printer.print_header(self.function.__name__)
        Printer.i = 0

        for test in self.tests:
            if test.type == "AssertOutput":
                self._run_assert_output(test)
            elif test.type == "AssertConsoleOutput":
                self._run_assert_console_output(test)
            elif test.type == "AssertEqualAfterExecution":
                self._run_assert_equal_after_execution(test)
            elif test.type == "AssertEqual":
                self._run_assert_equal(test)
            elif test.type == "AssertNotEqual":
                self._run_assert_not_equal(test)
            elif test.type == "ThrowException":
                self._run_throw_exception(test)
            elif test.type == "Execute":
                self._execute(test)
            else:
                raise TypeError(f"Unknown test type: {type(test)} {test.type}")

        Printer.print_separator()

    def _check_equal(self, expected, actual):
        if expected == actual:
            self.passed += 1
            Printer.print_success()
        else:
            Printer.print_failed(expected, actual)

    def _run_assert_output(self, test: AssertOutput):
        self.total += 1
        try:
            output = self.function(*test.args)
        except Exception:
            Printer.print_error()
            return

        self._check_equal(test.expected, output)

    def _run_assert_console_output(self, test: AssertOutput):
        self.total += 1

        # Capture console output
        buffer = io.StringIO()
        sys.stdout = buffer

        try:
            self.function(*test.args)
            output = buffer.getvalue()
            sys.stdout = sys.__stdout__
        except Exception:
            sys.stdout = sys.__stdout__ # Makes sure the console output is not captured
            Printer.print_error()
            return

        self._check_equal(test.expected, output)

    def _run_assert_equal_after_execution(self, test: AssertEqualAfterExecution):
        self.total += 1
        try:
            self.function(*test.args)
        except Exception as e:
            Printer.print_error(e)
            return

        try:
            self._check_equal(test.expected, test.variable())
        except Exception as e:
            Printer.print_error(e)

    def _run_assert_equal(self, test: AssertEqual):
        self.total += 1
        try:
            self._check_equal(test.expected, test.variable())
        except Exception as e:
            Printer.print_error(e)

    def _run_assert_not_equal(self, test: AssertNotEqual):
        self.total += 1
        for forbidden_value in test.forbidden:
            if test.variable() == forbidden_value:
                Printer.print_error(f"La variable {test.variable().__name__} ne doit pas valoir {forbidden_value}")
                return

        self.passed += 1
        Printer.print_success()

    def _run_throw_exception(self, test: ThrowException):
        self.total += 1
        try:
            self.function(*test.args)
        except test.exception as e:
            if test.error_message == "":
                self.passed += 1
                Printer.print_success()
            else:
                self._check_equal(test.error_message, e)
            return
        except Exception as e:
            Printer.print_failed(str(test.exception.__name__), e.__class__.__name__)
            return

        Printer.print_failed(test.exception.__name__, "No exception raised")

    @staticmethod
    def _execute(test: Execute):
        """
        Execute arbitrary code at a specific point in the test suite.
        :param test: The Execute test.
        """
        if test.args is None:
            test.function()
        else:
            test.function(*test.args)

