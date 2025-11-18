from sujet_1.skeleton.main import *
from math import pi
from Moulinette.moulinette import Moulinette
from Moulinette.test_suite import TestSuite
from Moulinette.unit_test import AssertOutput, AssertConsoleOutput

test_print_mario = TestSuite(print_mario)
test_print_mario.add(AssertConsoleOutput([], "Hello, Mario!\n"))

test_get_mario_age = TestSuite(get_mario_age)
test_get_mario_age.add(AssertOutput([1], 26))
test_get_mario_age.add(AssertOutput([2], 27))
test_get_mario_age.add(AssertOutput([10], 35))
test_get_mario_age.add(AssertOutput([100], 125))
test_get_mario_age.add(AssertOutput([0], 25))
test_get_mario_age.add(AssertOutput([-10], 15))

test_diff = TestSuite(diff)
test_diff.add(AssertOutput([1, 2], -1))
test_diff.add(AssertOutput([1, 2], -1))
test_diff.add(AssertOutput([0, 0], 0))
test_diff.add(AssertOutput([0, 1], -1))
test_diff.add(AssertOutput([1, 0], 1))
test_diff.add(AssertOutput([1, 1], 0))
test_diff.add(AssertOutput([100, 19], 81))
test_diff.add(AssertOutput([27, 12], 15))
test_diff.add(AssertOutput([12, -12], 24))

test_perimeter = TestSuite(perimeter)
test_perimeter.add(AssertOutput([1], 2 * pi))
test_perimeter.add(AssertOutput([0], 0))
test_perimeter.add(AssertOutput([10], 20 * pi))
test_perimeter.add(AssertOutput([100], 200 * pi))
test_perimeter.add(AssertOutput([-2], -4 * pi))

test_max = TestSuite(max)
test_max.add(AssertOutput([1, 2], 2))
test_max.add(AssertOutput([0, 0], 0))
test_max.add(AssertOutput([0, 1], 1))
test_max.add(AssertOutput([1, 0], 1))
test_max.add(AssertOutput([1, 1], 1))
test_max.add(AssertOutput([100, 19], 100))
test_max.add(AssertOutput([27, 12], 27))
test_max.add(AssertOutput([12, -12], 12))
test_max.add(AssertOutput([-61, -12], -12))

test_give_grade = TestSuite(give_grade)
test_give_grade.add(AssertConsoleOutput([0], "F\n"))
test_give_grade.add(AssertConsoleOutput([1], "F\n"))
test_give_grade.add(AssertConsoleOutput([11], "E\n"))
test_give_grade.add(AssertConsoleOutput([12], "D\n"))
test_give_grade.add(AssertConsoleOutput([15], "C\n"))
test_give_grade.add(AssertConsoleOutput([16], "B\n"))
test_give_grade.add(AssertConsoleOutput([19], "A\n"))
test_give_grade.add(AssertConsoleOutput([20], "A\n"))
test_give_grade.add(AssertConsoleOutput([-5], "Note invalide\n"))
test_give_grade.add(AssertConsoleOutput([22], "Note invalide\n"))

test_and_gate = TestSuite(and_gate)
test_and_gate.add(AssertOutput([True, False], False))
test_and_gate.add(AssertOutput([False, True], False))
test_and_gate.add(AssertOutput([True, True], True))
test_and_gate.add(AssertOutput([False, False], False))

test_or_gate = TestSuite(or_gate)
test_or_gate.add(AssertOutput([True, False], True))
test_or_gate.add(AssertOutput([False, True], True))
test_or_gate.add(AssertOutput([True, True], True))
test_or_gate.add(AssertOutput([False, False], False))

test_sum_number = TestSuite(sum_number)
test_sum_number.add(AssertOutput([1], 1))
test_sum_number.add(AssertOutput([0], 0))
test_sum_number.add(AssertOutput([10], 55))
test_sum_number.add(AssertOutput([100], 5050))
test_sum_number.add(AssertOutput([7], 28))
test_sum_number.add(AssertOutput([12], 78))
test_sum_number.add(AssertOutput([1000], 500500))

test_print_square = TestSuite(print_square)
test_print_square.add(AssertConsoleOutput([1], "*\n"))
test_print_square.add(AssertConsoleOutput([5], "*****\n*****\n*****\n*****\n*****\n"))

test_print_triangle = TestSuite(print_triangle)
test_print_triangle.add(AssertConsoleOutput([1], "*\n"))
test_print_triangle.add(AssertConsoleOutput([5], "*\n**\n***\n****\n*****\n"))

test_ask_div = TestSuite(ask_div) # TODO

test_xor = TestSuite(xor)
test_xor.add(AssertOutput([True, False], True))
test_xor.add(AssertOutput([False, True], True))
test_xor.add(AssertOutput([True, True], False))
test_xor.add(AssertOutput([False, False], False))

test_nand = TestSuite(nand)
test_nand.add(AssertOutput([True, False], True))
test_nand.add(AssertOutput([False, True], True))
test_nand.add(AssertOutput([True, True], False))
test_nand.add(AssertOutput([False, False], True))

test_is_even = TestSuite(is_even)
test_is_even.add(AssertOutput([1], False))
test_is_even.add(AssertOutput([0], True))
test_is_even.add(AssertOutput([10], True))
test_is_even.add(AssertOutput([100], True))
test_is_even.add(AssertOutput([7], False))
test_is_even.add(AssertOutput([12], True))
test_is_even.add(AssertOutput([1000], True))
test_is_even.add(AssertOutput([-1], False))
test_is_even.add(AssertOutput([-7], False))
test_is_even.add(AssertOutput([-12], True))
test_is_even.add(AssertOutput([-1000], True))

test_print_pyramid = TestSuite(print_pyramid)
test_print_pyramid.add(AssertConsoleOutput([3], "  *  \n *** \n*****\n"))
test_print_pyramid.add(AssertConsoleOutput([5], "    *    \n   ***   \n  *****  \n ******* \n*********\n"))

test_count_division = TestSuite(count_division)
test_count_division.add(AssertOutput([1], 0))
test_count_division.add(AssertOutput([0], 0))
test_count_division.add(AssertOutput([10], 3))
test_count_division.add(AssertOutput([100], 6))
test_count_division.add(AssertOutput([7], 2))
test_count_division.add(AssertOutput([12], 3))
test_count_division.add(AssertOutput([1000], 9))

test_is_amstrong = TestSuite(is_amstrong)
test_is_amstrong.add(AssertOutput([1], True))
test_is_amstrong.add(AssertOutput([0], True))
test_is_amstrong.add(AssertOutput([10], False))
test_is_amstrong.add(AssertOutput([100], False))
test_is_amstrong.add(AssertOutput([7], True))
test_is_amstrong.add(AssertOutput([12], False))
test_is_amstrong.add(AssertOutput([1000], False))
test_is_amstrong.add(AssertOutput([153], True))
test_is_amstrong.add(AssertOutput([370], True)) # 370 = 3^3 + 7^3 + 0^3
test_is_amstrong.add(AssertOutput([371], True)) # 371 = 3^3 + 7^3 + 1^3
test_is_amstrong.add(AssertOutput([407], True)) # 407 = 4^3 + 0^3 + 7^3
test_is_amstrong.add(AssertOutput([1634], True)) # 1634 = 1^4 + 6^4 + 3^4 + 4^4
test_is_amstrong.add(AssertOutput([8208], True))
test_is_amstrong.add(AssertOutput([9474], True))
test_is_amstrong.add(AssertOutput([54748], True))

test_guess_number = TestSuite(guess_number) # TODO