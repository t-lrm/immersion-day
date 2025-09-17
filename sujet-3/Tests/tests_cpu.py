from Moulinette.moulinette import Moulinette
from test_handle_0 import test_handle_0
from test_handle_1 import test_handle_1
from test_handle_2 import test_handle_2
from test_handle_3 import test_handle_3
from test_handle_4 import test_handle_4
from test_handle_5 import test_handle_5
from test_handle_6 import test_handle_6
from test_handle_7 import test_handle_7
from test_handle_8 import test_handle_8
from test_handle_9 import test_handle_9
from test_handle_A import test_handle_A
from test_handle_B import test_handle_B
from test_handle_C import test_handle_C
from test_handle_E import test_handle_E
from test_handle_F import test_handle_F

moulinette = Moulinette()

moulinette.add_test(test_handle_0)
moulinette.add_test(test_handle_1)
moulinette.add_test(test_handle_2)
moulinette.add_test(test_handle_3)
moulinette.add_test(test_handle_4)
moulinette.add_test(test_handle_5)
moulinette.add_test(test_handle_6)
moulinette.add_test(test_handle_7)
moulinette.add_test(test_handle_8)
moulinette.add_test(test_handle_9)
moulinette.add_test(test_handle_A)
moulinette.add_test(test_handle_B)
moulinette.add_test(test_handle_C)
moulinette.add_test(test_handle_E)
moulinette.add_test(test_handle_F)

if __name__ == "__main__":
    moulinette.run_all()
