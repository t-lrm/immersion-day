from main import *
from math import pi
from moulinette import *

def test_print_mario():
    test = Test("print_mario", print_mario, True)
    test.add([], "Hello, Mario!\n")
    test.run()

def test_getMarioAge():
    test = Test("getMarioAge", get_mario_age)
    test.add([1], 26)
    test.add([2], 27)
    test.add([10], 35)
    test.add([100], 125)
    test.add([0], 25)
    test.add([-10], 15)
    test.run()

def test_diff():
    test = Test("diff", diff)
    test.add([1, 2], -1)
    test.add([0, 0], 0)
    test.add([0, 1], -1)
    test.add([1, 0], 1)
    test.add([1, 1], 0)
    test.add([100, 19], 81)
    test.add([27, 12], 15)
    test.add([12, -12], 24)
    test.run()

def test_perimeter():
    test = Test("perimeter", perimeter)
    test.add([1], 2 * pi)
    test.add([0], 0)
    test.add([10], 20 * pi)
    test.add([100], 200 * pi)
    test.add([-2], -4 * pi)
    test.run()

def test_and_gate():
    test = Test("and_gate", and_gate)
    test.add([True, False], False)
    test.add([False, True], False)
    test.add([True, True], True)
    test.add([False, False], False)
    test.run()

def test_or_gate():
    test = Test("or_gate", or_gate)
    test.add([True, False], True)
    test.add([False, True], True)
    test.add([True, True], True)
    test.add([False, False], False)
    test.run()

def test_max():
    test = Test("max", max)
    test.add([1, 2], 2)
    test.add([0, 0], 0)
    test.add([0, 1], 1)
    test.add([1, 0], 1)
    test.add([1, 1], 1)
    test.add([100, 19], 100)
    test.add([27, 12], 27)
    test.add([12, -12], 12)
    test.run()

def test_give_grade():
    test = Test("give_grade", give_grade, True)
    test.add([1], "F\n")
    test.add([0], "F\n")
    test.add([-5], "Note invalide\n")
    test.add([11], "E\n")
    test.add([12], "D\n")
    test.add([15], "C\n")
    test.add([16], "B\n")
    test.add([19], "A\n")
    test.add([20], "A\n")
    test.add([22], "Note invalide\n")
    test.run()

def test_sum_number():
    test = Test("sum_number", sum_number)
    test.add([1], 1)
    test.add([0], 0)
    test.add([10], 55)
    test.add([100], 5050)
    test.add([7], 28)
    test.add([12], 78)
    test.add([1000], 500500)
    test.run()

def test_print_triangle():
    test = Test("print_pyramid", print_triangle, True)
    test.add([1], "*\n")
    test.add([5], "*\n**\n***\n****\n*****\n")
    test.run()
    

def test_print_square():
    test = Test("print_square", print_square, True)
    test.add([1], "*\n")
    test.add([5], "*****\n*****\n*****\n*****\n*****\n")
    test.run()

def test_xor():
    test = Test("xor", xor)
    test.add([True, False], True)
    test.add([False, True], True)
    test.add([True, True], False)
    test.add([False, False], False)
    test.run()

def test_nand():
    test = Test("nand", nand)
    test.add([True, False], True)
    test.add([False, True], True)
    test.add([True, True], False)
    test.add([False, False], True)
    test.run()

def test_is_even():
    test = Test("is_even", is_even)
    test.add([1], False)
    test.add([0], True)
    test.add([10], True)
    test.add([100], True)
    test.add([7], False)
    test.add([12], True)
    test.add([1000], True)
    test.run()

def test_print_pyramid():
    test = Test("print_pyramid", print_pyramid, True)
    s = "  *  \n *** \n*****\n"
    test.add([3], s)
    # Test with n = 5
    s = "    *    \n   ***   \n  *****  \n ******* \n*********\n"
    test.add([5], s)
    test.run()


def test_count_division():
    test = Test("count_division", count_division)
    test.add([1], 0)
    test.add([0], 0)
    test.add([10], 3)
    test.add([100], 6)
    test.add([7], 2)
    test.add([12], 3)
    test.add([1000], 9)
    test.run()

def test_amstrong():
    test = Test("amstrong", is_amstrong)
    test.add([1], True)
    test.add([0], True)
    test.add([10], False)
    test.add([100], False)
    test.add([7], True)
    test.add([12], False)
    test.add([1000], False)
    test.add([153], True)
    test.add([370], True) # 370 = 3^3 + 7^3 + 0^3
    test.add([371], True) # 371 = 3^3 + 7^3 + 1^3
    test.add([407], True) # 407 = 4^3 + 0^3 + 7^3
    test.add([1634], True) # 1634 = 1^4 + 6^4 + 3^4 + 4^4
    test.add([8208], True)
    test.add([9474], True)
    test.add([54748], True)
    test.run()

def run_test():
    print_separator()
    # Test easy
    test_print_mario()
    test_getMarioAge()
    test_diff()
    test_perimeter()
    test_max()
    test_give_grade()
    test_and_gate()
    test_or_gate()
    test_sum_number()
    test_print_square()
    test_print_triangle()
    #  Test medium
    test_xor()
    test_nand()
    test_is_even()
    test_print_triangle()
    test_count_division()
    # Test hard
    test_amstrong()