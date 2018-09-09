import unittest


class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        print("Hello Unit Tests!")
        self.assertTrue(True)