import unittest

def methodName() -> None:
    return 1

class TestMethodName(unittest.TestCase):

    def test_methodName_oneunique(self):
        return 1

if __name__ == "__main__":
    unittest.main()