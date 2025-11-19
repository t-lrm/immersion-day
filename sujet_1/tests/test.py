from Moulinette.moulinette import Moulinette
from test_suite import *

moulinette = Moulinette()

moulinette.add_test(test_print_mario)
moulinette.add_test(test_get_mario_age)
moulinette.add_test(test_diff)
moulinette.add_test(test_perimeter)
moulinette.add_test(test_max)
moulinette.add_test(test_give_grade)
moulinette.add_test(test_and_gate)
moulinette.add_test(test_or_gate)
moulinette.add_test(test_sum_number)
moulinette.add_test(test_print_square)
moulinette.add_test(test_print_triangle)
moulinette.add_test(test_ask_div)
moulinette.add_test(test_xor)
moulinette.add_test(test_nand)
moulinette.add_test(test_is_even)
moulinette.add_test(test_print_pyramid)
moulinette.add_test(test_count_division)
moulinette.add_test(test_is_amstrong)
moulinette.add_test(test_print_pyramid)

moulinette.run_all()
