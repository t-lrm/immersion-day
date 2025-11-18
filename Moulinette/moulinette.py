from Moulinette.printer import Printer
from Moulinette.test_suite import TestSuite

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
