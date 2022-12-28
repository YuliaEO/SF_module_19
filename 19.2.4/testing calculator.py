import pytestpytest
from app .calculator import CalculatorCalculator

class TestCalc:
    def setup (self):
        self.calc = Calculator

    def test_multiply_calculate_correctly (self):
        assert .calc.multiply(self, 2, 2)

    def test_division_calculate_correctly(self):
        assert  .calc.division (self, 6, 2)

    def test_subtraction_calculate_correctly (self):
        assert  .calc.subtraction (self, 5, 2)

    def test_adding_calculate_correctly(self):
        assert  .calc.adding(self, 4, 2)

    def test_adding_failed (self):
        assert .calc.adding(self, 2, 2) == 5
