import unittest
import math
from calculator import square_root, factorial, natural_log, power

class TestScientificCalculator(unittest.TestCase):

    # ── Square Root Tests ──────────────────────────────────────────────────────

    def test_square_root_positive(self):
        """√9 should return 3.0"""
        self.assertAlmostEqual(square_root(9), 3.0)

    def test_square_root_zero(self):
        """√0 should return 0.0"""
        self.assertAlmostEqual(square_root(0), 0.0)

    def test_square_root_decimal(self):
        """√2 should return approx 1.4142"""
        self.assertAlmostEqual(square_root(2), 1.4142135, places=5)

    def test_square_root_negative(self):
        """√(-1) should raise ValueError"""
        with self.assertRaises(ValueError):
            square_root(-1)

    # ── Factorial Tests ────────────────────────────────────────────────────────

    def test_factorial_normal(self):
        """5! should return 120"""
        self.assertEqual(factorial(5), 120)

    def test_factorial_zero(self):
        """0! should return 1 (by mathematical definition)"""
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        """1! should return 1"""
        self.assertEqual(factorial(1), 1)

    def test_factorial_negative(self):
        """Factorial of negative number should raise ValueError"""
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_factorial_float(self):
        """Factorial of a float should raise ValueError"""
        with self.assertRaises(ValueError):
            factorial(3.5)

    # ── Natural Log Tests ──────────────────────────────────────────────────────

    def test_natural_log_of_e(self):
        """ln(e) should return 1.0"""
        self.assertAlmostEqual(natural_log(math.e), 1.0)

    def test_natural_log_of_one(self):
        """ln(1) should return 0.0"""
        self.assertAlmostEqual(natural_log(1), 0.0)

    def test_natural_log_positive(self):
        """ln(10) should return approx 2.302"""
        self.assertAlmostEqual(natural_log(10), 2.302585, places=5)

    def test_natural_log_zero(self):
        """ln(0) should raise ValueError"""
        with self.assertRaises(ValueError):
            natural_log(0)

    def test_natural_log_negative(self):
        """ln(-5) should raise ValueError"""
        with self.assertRaises(ValueError):
            natural_log(-5)

    # ── Power Tests ───────────────────────────────────────────────────────────

    def test_power_normal(self):
        """2^3 should return 8.0"""
        self.assertAlmostEqual(power(2, 3), 8.0)

    def test_power_zero_exponent(self):
        """5^0 should return 1.0"""
        self.assertAlmostEqual(power(5, 0), 1.0)

    def test_power_one_exponent(self):
        """7^1 should return 7.0"""
        self.assertAlmostEqual(power(7, 1), 7.0)

    def test_power_negative_exponent(self):
        """2^(-1) should return 0.5"""
        self.assertAlmostEqual(power(2, -1), 0.5)

    def test_power_decimal(self):
        """4^0.5 should return 2.0 (same as square root)"""
        self.assertAlmostEqual(power(4, 0.5), 2.0)


# ── Run tests ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    unittest.main(verbosity=2)