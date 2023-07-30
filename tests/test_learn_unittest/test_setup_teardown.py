import unittest

# module level fixture, runs before all test methods in the test module
def setUpModule():
    print('Running setUpModule')

# module level fixture, runs after all test methods in the test module
def tearDownModule():
    print('Running tearDownModule')


# unittest test cases
class TestFixtureModule(unittest.TestCase):
    # class level fixture, runs before all test methods of a class
    @classmethod
    def setUpClass(cls):
        print('Running setUpClass')

    # class level fixture, runs after all test methods of a class
    @classmethod
    def tearDownClass(cls):
        print('Running tearDownClass')

    # method level fixture, runs befor every test methods of the test class
    def setUp(self):
        print()
        print('Running setUp')

    # method level fixture, runs after every test methods of the test class
    def tearDown(self):
        print('Running tearDown')

    def test_case_1(self):
        print('Running test_case_1')
        self.assertEqual(10, 5+5)

    def test_case_2(self):
        print('Running test_case_2')
        self.assertEqual(11, 22/2)


if __name__ == "__main__":
    unittest.main()
    # pytest -v -s .\tests\test_learn_unittest\test_setup_teardown.py
    # python -m unittest -v .\tests\test_learn_unittest\test_setup_teardown.py
