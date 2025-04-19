import unittest
import math
from symbol import Symbol, Ln

class TestSymbolicFunction(unittest.TestCase):
    def test_addition(self):
        x = Symbol()
        f = x + 3

        # Test evaluation
        self.assertEqual(f(2), 5)
        self.assertEqual(f(-3), 0)

        # Test differentiation
        df = f.diff().prune()
        self.assertEqual(df(2), 1)  # Derivative of x + 3 is 1
        self.assertEqual(df(-3), 1)

    def test_multiplication(self):
        x = Symbol()
        f = 3 * x

        # Test evaluation
        self.assertEqual(f(2), 6)
        self.assertEqual(f(-3), -9)

        # Test differentiation
        df = f.diff().prune()
        self.assertEqual(df(2), 3)  # Derivative of 3*x is 3
        self.assertEqual(df(-3), 3)

    def test_exponentiation(self):
        x = Symbol()
        f = x ** 3

        # Test evaluation
        self.assertEqual(f(2), 8)
        self.assertEqual(f(-2), -8)

        # Test differentiation
        df = f.diff().prune()
        self.assertEqual(df(2), 12)  # Derivative of x^3 is 3*x^2
        self.assertEqual(df(-2), 12)

    def test_division(self):
        x = Symbol()
        f = 6 / x

        # Test evaluation
        self.assertEqual(f(2), 3)
        self.assertEqual(f(3), 2)

        # Test differentiation
        df = f.diff().prune()
        self.assertEqual(df(2), -1.5)  # Derivative of 6/x is -6/x^2
        self.assertEqual(df(3), -2/3)

    def test_logarithm(self):
        x = Symbol()
        f = Ln(x + 3)

        # Test evaluation
        self.assertAlmostEqual(f(2), math.log(5), places=5)
        self.assertAlmostEqual(f(-2), math.log(1), places=5)

        # Test differentiation
        df = f.diff().prune()
        self.assertAlmostEqual(df(2), 1/5, places=5)  # Derivative of ln(x + 3) is 1/(x + 3)
        self.assertAlmostEqual(df(-2), 1/1, places=5)

    def test_combined_operations(self):
        x = Symbol()
        f = 2 * x ** 2 + 3 * x + 5

        # Test evaluation
        self.assertEqual(f(2), 2 * 4 + 3 * 2 + 5)  # 8 + 6 + 5 = 19
        self.assertEqual(f(-1), 2 * 1 - 3 + 5)  # 2 - 3 + 5 = 4

        # Test differentiation
        df = f.diff().prune()
        self.assertEqual(df(2), 4 * 2 + 3)  # Derivative: 4x + 3
        self.assertEqual(df(-1), 4 * -1 + 3)

    # def test_combined_function_1(self):
    #     x = Symbol()
    #     f = (x ** 2 + 1) * (x + 3)

    #     # Test evaluation
    #     self.assertEqual(f(2), (2 ** 2 + 1) * (2 + 3))  # (4 + 1) * 5 = 25
    #     self.assertEqual(f(0), (0 ** 2 + 1) * (0 + 3))  # 1 * 3 = 3

    #     # Test differentiation
    #     df = f.diff().prune()
    #     print(df)
    #     self.assertEqual(df(2), 2 * 2 * (2 + 3) + (2 ** 2 + 1))  # Product rule
    #     self.assertEqual(df(0), 2 * 0 * (0 + 3) + (0 ** 2 + 1))

    # def test_combined_function_2(self):
    #     x = Symbol()
    #     f = (x ** 3 + 2 * x) / (x + 1)

    #     # Test evaluation
    #     self.assertAlmostEqual(f(2), (2 ** 3 + 2 * 2) / (2 + 1))  # (8 + 4) / 3 = 4
    #     self.assertAlmostEqual(f(1), (1 ** 3 + 2 * 1) / (1 + 1))  # (1 + 2) / 2 = 1.5

    #     # Test differentiation
    #     df = f.diff().prune()
    #     self.assertAlmostEqual(df(2), ((3 * 2 ** 2 + 2) * (2 + 1) - (2 ** 3 + 2 * 2)) / (2 + 1) ** 2)
    #     self.assertAlmostEqual(df(1), ((3 * 1 ** 2 + 2) * (1 + 1) - (1 ** 3 + 2 * 1)) / (1 + 1) ** 2)

    # def test_combined_function_3(self):
    #     x = Symbol()
    #     f = Ln(x ** 2 + 3 * x + 2)

    #     # Test evaluation
    #     self.assertAlmostEqual(f(1), math.log(1 ** 2 + 3 * 1 + 2), places=5)  # ln(6)
    #     self.assertAlmostEqual(f(0), math.log(0 ** 2 + 3 * 0 + 2), places=5)  # ln(2)

    #     # Test differentiation
    #     df = f.diff().prune()
    #     self.assertAlmostEqual(df(1), (2 * 1 + 3) / (1 ** 2 + 3 * 1 + 2), places=5)  # Chain rule
    #     self.assertAlmostEqual(df(0), (2 * 0 + 3) / (0 ** 2 + 3 * 0 + 2), places=5)

    # def test_combined_function_4(self):
    #     x = Symbol()
    #     f = (x ** 2 + 2) * Ln(x + 1)

    #     # Test evaluation
    #     self.assertAlmostEqual(f(1), (1 ** 2 + 2) * math.log(1 + 1), places=5)  # 3 * ln(2)
    #     self.assertAlmostEqual(f(0), (0 ** 2 + 2) * math.log(0 + 1), places=5)  # 2 * ln(1) = 0

    #     # Test differentiation
    #     df = f.diff().prune()
    #     self.assertAlmostEqual(df(1), (2 * 1 * math.log(1 + 1) + (1 ** 2 + 2) / (1 + 1)), places=5)
    #     self.assertAlmostEqual(df(0), (2 * 0 * math.log(0 + 1) + (0 ** 2 + 2) / (0 + 1)), places=5)

    # def test_combined_function_5(self):
    #     x = Symbol()
    #     f = (x ** 3 + 3 * x ** 2 + 3 * x + 1) / (x + 1)

    #     # Test evaluation
    #     self.assertEqual(f(1), (1 ** 3 + 3 * 1 ** 2 + 3 * 1 + 1) / (1 + 1))  # 8 / 2 = 4
    #     self.assertEqual(f(0), (0 ** 3 + 3 * 0 ** 2 + 3 * 0 + 1) / (0 + 1))  # 1 / 1 = 1

    #     # Test differentiation
    #     df = f.diff().prune()
    #     self.assertAlmostEqual(df(1), ((3 * 1 ** 2 + 6 * 1 + 3) * (1 + 1) - (1 ** 3 + 3 * 1 ** 2 + 3 * 1 + 1)) / (1 + 1) ** 2)
    #     self.assertAlmostEqual(df(0), ((3 * 0 ** 2 + 6 * 0 + 3) * (0 + 1) - (0 ** 3 + 3 * 0 ** 2 + 3 * 0 + 1)) / (0 + 1) ** 2)

    def test_equality(self):
        x = Symbol()

        # Commutativity of addition
        assert x + 3 == 3 + x
        assert (x + 3) + 2 == x + (3 + 2)

        # Commutativity of multiplication
        assert x * 3 == 3 * x
        assert (x * 2) * 3 == x * (2 * 3)

        # Multiplication distributes over addition
        assert x * (2 + 3) == x * 2 + x * 3

        # Powers (non-commutative)
        assert x**2 == x**2
        assert x**2 != 2**x

        # Natural logarithm
        assert Ln(x + 1) == Ln(1 + x)
        assert Ln(x) != Ln(3)

if __name__ == "__main__":
    unittest.main()
