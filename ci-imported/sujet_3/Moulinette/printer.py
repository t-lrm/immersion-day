from pyfiglet import Figlet


class Color:
    G = "\033[32m"
    R = "\033[31m"
    O = "\033[38;2;255;165;0m"
    Y = "\033[33m"
    Z = "\033[0m"


class Printer:
    i: int = 0  # Index of the test
    width: int = 100

    @classmethod
    def print(cls, message: str, indent: int = 0, color: str = Color.Z):
        print(indent * '│ ' + f"{color}{message.ljust(cls.width - 2 * indent)}{Color.Z} │")

    @classmethod
    def print_separator(cls, indent: int = 0):
        if indent == 0:
            print('└' + cls.width * '─' + '┘')
        else:
            print(indent * '│ ' + '└' + (cls.width - 2 * indent - 1) * '─' + " │")

    @classmethod
    def print_header(cls, message: str, ):
        print(f"┌{' ' + message + ' ':─^{cls.width}}┐")

    @classmethod
    def print_success(cls):
        cls.i += 1
        cls.print(f"[X] Test {cls.i:02d} réussi", indent=1, color=Color.G)

    @classmethod
    def print_failed(cls, expected: any, actual: any):
        cls.i += 1
        cls.print(f"[ ] Test {cls.i:02d} échoué", indent=1, color=Color.R)
        cls.print(f"Sortie attendue: '{expected}'", indent=2)
        cls.print(f"Sortie reçue:    '{actual}'", indent=2)
        cls.print_separator(indent=1)

    @classmethod
    def print_error(cls, message: str = ""):
        Printer.i += 1

        cls.print(f"[ ] Test {cls.i} échoué", indent=1, color=Color.R)
        cls.print("Une erreur est survenue lors de l'exécution de la fonction", indent=2)

        if message != "":
            cls.print(f"Erreur: {message}", indent=2)

        cls.print_separator(2)

    @staticmethod
    def show_percentage(passed: int, total: int) -> None:
        """
        Show the percentage of tests passed:
        - 0–32%   → red
        - 33–65%  → orange
        - 66–99%  → yellow
        - 100%    → green
        """
        if total == 0:
            print("Aucun test n'a été exécuté.")
            return

        percentage = (passed / total) * 100

        # pick one of four fixed colors
        if percentage == 100:
            color = Color.G
        elif percentage >= 66:
            color = Color.Y
        elif percentage >= 33:
            color = Color.O
        else:
            color = Color.R

        print(f"TOTAL: {color}{percentage:.0f}% ({passed}/{total}){Color.Z}")
