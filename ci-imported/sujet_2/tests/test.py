from test_suite import *
from Moulinette.moulinette import Moulinette

moulinette = Moulinette()

moulinette.add_test(test_caesar_encode)
moulinette.add_test(test_caesar_decode)
moulinette.add_test(test_substitution_encode)
moulinette.add_test(test_substitution_decode)
moulinette.add_test(test_vigenere_encode)
moulinette.add_test(test_vigenere_decode)
moulinette.add_test(test_xor_encode)
moulinette.add_test(test_caesar_door)
moulinette.add_test(test_transposition_encode)
moulinette.add_test(test_transposition_decode)
moulinette.add_test(test_hill_encode)
moulinette.add_test(test_hill_decode)
moulinette.add_test(test_gcd)
moulinette.add_test(test_egcd)
moulinette.add_test(test_generate_key)
moulinette.add_test(test_rsa_encode)
moulinette.add_test(test_rsa_decode)

moulinette.run_all()