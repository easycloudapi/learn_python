import os
import sys
import unittest
import pytest

# sys.path[0]: D:\pythonProject\local_python_project\tests\test_learn_unittest
print(f"sys.path[0]: {sys.path[0]}")

# os.getcwd(): D:\pythonProject\local_python_project\tests\test_learn_unittest
print(f"os.getcwd(): {os.getcwd()}")

# root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
root_dir = os.getcwd()
print(f"root_dir: {root_dir}")
sys.path.append(root_dir)

from learn_unittest.check_even_or_odd import _check_even_or_odd


class Test_Positive_Unittest(unittest.TestCase):
    def test_check_even(self):
        """
        Check positive test case to check the param input is even
        """
        self.assertEqual("6 is even", _check_even_or_odd(6))

    def test_check_odd(self):
        """
        Check positive test case to check the param input is odd
        """
        self.assertEqual("7 is odd", _check_even_or_odd(7))


# parameterized unittest cases using pytest
# @pytest.mark.parametrize not working inside unittest class
@pytest.mark.parametrize("arg1, expected_result",  # param name, passing to the below function definitions
                         [(0, "0 is even"),  # another test case 1
                          (11.5, "11.5 is odd"),  # another test case 2
                          (38.00, "38.0 is even")],  # another test case 3
                         ids=["0_is_even", "decimal_value_is_odd", "decimal_value_is_even"])  # test names
def test_check_even_or_odd(arg1, expected_result):
    # assert expected_result == _check_even_or_odd(arg1)
    unittest.TestCase().assertEqual(expected_result, _check_even_or_odd(arg1))


class Test_Negative_Unittest(unittest.TestCase):
    def test_missing_param(self):
        """
        testing exception if param is missing
        """
        # using context manager of error
        with self.assertRaises(TypeError):
            _check_even_or_odd()

    def test_wrong_param(self):
        """
        testing exception if wrong param "float_var" has been passed instead of "int_var"
        """
        # using context manager of error
        with pytest.raises(TypeError):
            _check_even_or_odd(float_var=11.5)


if __name__ == "__main__":
    unittest.main()
