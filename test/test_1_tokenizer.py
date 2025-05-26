import unittest
from tokens.tokenizer import UnitTokenizer

class TestUnitTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = UnitTokenizer()

    def test_kWh(self):
        # Assert
        input_str = "kW*h"
        expected = "[Dim:(k*W), Ope:*, Dim:(1*h)]"

        # Act
        self.tokenizer.unit_string = input_str
        actual_tokens = self.tokenizer.tokenize()
        actual = str(actual_tokens)

        # Assert
        self.assertEqual(expected, actual)

    def test_m3_kg_s2(self):
        # Arrange
        input_str = "m^3*kg^-1*s^-2"
        expected = "[Dim:(1*m), Ope:^, Num:3, Ope:*, Dim:(k*g), Ope:^, Num:-1, Ope:*, Dim:(1*s), Ope:^, Num:-2]"

        # Act
        self.tokenizer.unit_string = input_str
        actual_tokens = self.tokenizer.tokenize()
        actual = str(actual_tokens)

        # Assert
        self.assertEqual(expected, actual)

    def test_km_per_s_per_mpc(self):
        # Arrange
        input_str = "km/s/Mpc"
        expected = "[Dim:(k*m), Ope:/, Dim:(1*s), Ope:/, Dim:(M*pc)]"

        # Act
        self.tokenizer.unit_string = input_str
        actual_tokens = self.tokenizer.tokenize()
        actual = str(actual_tokens)

        # Assert
        self.assertEqual(expected, actual)

    def test_ps_per_sqrt_km(self):
        # Arrange
        input_str = "ps/√km"
        expected = "[Dim:(p*s), Ope:/, Ope:√, Dim:(k*m)]"

        # Act
        self.tokenizer.unit_string = input_str
        actual_tokens = self.tokenizer.tokenize()
        actual = str(actual_tokens)

        # Assert
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
