from sujet_3.Moulinette.printer import Printer
from sujet_3.Moulinette.test_suite import TestSuite
from sujet_3.Moulinette.unit_test import UnitTest, AssertOutput, AssertEqualAfterExecution, ThrowException

class Moulinette:
    def __init__(self):
        self.test_suites = []

    def add_test(self, test: TestSuite):
        """
        Add a test suite to the moulinette.
        :param test: TestSuite object.
        """
        self.test_suites.append(test)

    def run_all(self) -> None:
        for test in self.test_suites:
            test.run()

        passed = sum(test.passed for test in self.test_suites)
        total = sum(test.total for test in self.test_suites)
        Printer.show_percentage(passed, total)
