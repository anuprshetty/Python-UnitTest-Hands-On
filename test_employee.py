import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    # runs before each test cases
    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("Ram", "Raj", 50000)
        self.emp_2 = Employee("Sham", "Lal", 45000)

    # runs after each test cases
    def tearDown(self):
        print("tearDown")

    # Test cases run parallelly (i.e., not run in order). So it's better to keep test cases isolated from one another.
    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, "Ram.Raj@gmail.com")
        self.assertEqual(self.emp_2.email, "Sham.Lal@gmail.com")

        self.emp_1.first = "Bob"
        self.emp_2.first = "Alice"

        self.assertEqual(self.emp_1.email, "Bob.Raj@gmail.com")
        self.assertEqual(self.emp_2.email, "Alice.Lal@gmail.com")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Ram Raj")
        self.assertEqual(self.emp_2.fullname, "Sham Lal")

        self.emp_1.first = "Bob"
        self.emp_2.first = "Alice"

        self.assertEqual(self.emp_1.fullname, "Bob Raj")
        self.assertEqual(self.emp_2.fullname, "Alice Lal")

    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 47250)
