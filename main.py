import unittest
print("1")
unittest.TestCase().assertEqual(abs(10), 10)
print("2")
unittest.TestCase().assertEqual(abs(-10), 10)
unittest.TestCase().assertEqual(abs(10), -10)