import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_email(self):
        emp_1 = Employee("Ram", "Raj", 50000)
        emp_2 = Employee("Sham", "Lal", 45000)

        self.assertEqual(emp_1.email, "Ram.Raj@gmail.com")
        self.assertEqual(emp_2.email, "Sham.Lal@gmail.com")

        emp_1.first = "Bob"
        emp_2.first = "Alice"

        self.assertEqual(emp_1.email, "Bob.Raj@gmail.com")
        self.assertEqual(emp_2.email, "Alice.Lal@gmail.com")

    def test_fullname(self):
        emp_1 = Employee("Ram", "Raj", 50000)
        emp_2 = Employee("Sham", "Lal", 45000)

        self.assertEqual(emp_1.fullname, "Ram Raj")
        self.assertEqual(emp_2.fullname, "Sham Lal")

        emp_1.first = "Bob"
        emp_2.first = "Alice"

        self.assertEqual(emp_1.fullname, "Bob Raj")
        self.assertEqual(emp_2.fullname, "Alice Lal")

    def test_apply_raise(self):
        emp_1 = Employee("Ram", "Raj", 50000)
        emp_2 = Employee("Sham", "Lal", 45000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 47250)
