import io
import sys


class Test:

    def __init__(self, name, function, read_output = False, unauthorized_fonction = []):
        """
        name: Function's name
        function: Function to test
        read_output: If the function read the console input
        unauthorized_fonction: List of unauthorized function
        """
        self.name = name # Nom de la fonction
        self.function = function # Fonction à tester
        self.args = []
        self.expected = []
        self.read_input = read_output # Si la fonction lit l'entrée console
        self.unauthorized_fonction = unauthorized_fonction

    def run(self):
        """
        Run the test suite
        """

        # Check if the function is defined or not
        index_to_test = -1 
        # Search an expected value that is not None to test the function
        for i in range(len(self.expected)):
            if self.expected[i] is not None:
                index_to_test = i
                break

        # If all expected value are None, the function is not tested
        if index_to_test == -1:
            print("Impossible de tester la fonction " + self.name + "(): aucune valeur de retour n'est attendue")
            return
        
        if not self.read_input:
            # Check if the function is defined and check if there is an error
            try: 
                # If the function is not defined, the test is not run
                if self.function(*self.args[index_to_test]) is None:
                    return
            except:
                # If there is an error, the function is not tested
                print("Test de " + self.name + "():")
                test_error(1)
                print_separator()
                return
            # The function is tested without output
            print("Test de " + self.name + "():")
            self.__testWithoutOutput()
            print_separator()
        else:
            # The function is tested with output
            self.__testWithOutput()

    def add(self, args: list, expected: list):
        """
        Add a test case
        args: List of arguments (in order)
        expected: Expected output of the function
        """
        self.args.append(args)
        self.expected.append(expected)

    def __testWithoutOutput(self):
        test_number = 0
        for i in range(len(self.args)):
            test_number += 1
            try: 
                received = self.function(*self.args[i])
            except:
                test_error(test_number)
                continue
            if(received == self.expected[i]):
                success(test_number)
            else:
                test_failed(self.expected[i], received, test_number)

    def __testWithOutput(self):
        test_number = 0
        flag = False
        for i in range(len(self.args)):
            test_number += 1
            captured_output = io.StringIO()
            sys.stdout = captured_output
            try: 
                self.function(*self.args[i])
            except Exception as e:
                sys.stdout = sys.__stdout__  # Reset stdout before printing
                if not flag:
                    print("Test de " + self.name + "():")
                    flag = True
                test_error(test_number)
                continue
            finally:
                sys.stdout = sys.__stdout__

            if(captured_output.getvalue() == ""):
                return
            if not flag:
                print("Test de " + self.name + "():")
                flag = True
            if(captured_output.getvalue() == self.expected[i]):
                success(test_number)
            else:
                test_failed(self.expected[i].replace("\n", "\\n"), captured_output.getvalue().replace("\n", "\\n"), test_number)
        if flag:
            print_separator()

    def check_cheat(self, file):
        """
        Allow to check if the student use an unauthorized function
        file: Path of the file to check
        """
        if self.unauthorized_fonction == []:
            return True
        with open(file) as f:
            content = f.read()
            for i in self.unauthorized_fonction:
                if i in content:
                    print("La fonction " + i + " est interdite")
                    return False


def success(n: int):
    print("\033[32mTest " + str(n) + " réussi ✅\033[0m")


def test_failed(expected: any, received: any, n: int):
    print("\033[31mTest " + str(n) + " échoué ❌\033[0m")
    print("Sortie attendue: '" + str(expected) +"'")
    print("Sortie reçue: '" + str(received) + "'")


def test_error(n: int):
    print("\033[31mTest " + str(n) + " échoué ❌\033[0m")
    print("Une erreur est survenue lors de l'exécution de la fonction")


def print_separator():
    print("\n---------------------------------------------------------------\n")
