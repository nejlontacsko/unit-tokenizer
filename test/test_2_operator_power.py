import unittest
from tokens.tokenizer import UnitTokenizer
from tokens.token_list import TokenList


class TestUnitTokenList(unittest.TestCase):
    def setUp(self):
        self.tokenizer = UnitTokenizer()

    def test_kWh(self):
        # Assert
        input_str = "kW*h"
        expected = "[Dim:(k*W), Ope:*, Dim:(1*h)]"

        # Act
        self.tokenizer.unit_string = input_str
        tokens = self.tokenizer.tokenize()

        token_list = TokenList(tokens)
        token_list.do_replacements()
        actual = str(token_list)

        # Assert
        self.assertEqual(expected, actual)

    def test_m3_kg_s2(self):
        # Arrange
        input_str = "m^3*kg^-1*s^-2"
        expected = "[Dim:(1*m), Ope:^, Num:3, Ope:*, Dim:(k*g), Ope:^, Num:-1, Ope:*, Dim:(1*s), Ope:^, Num:-2]"

        # Act
        self.tokenizer.unit_string = input_str
        tokens = self.tokenizer.tokenize()

        token_list = TokenList(tokens)
        token_list.do_replacements()
        actual = str(token_list)

        # Assert
        self.assertEqual(expected, actual)

    def test_km_per_s_per_mpc(self):
        # Arrange
        input_str = "km/s/Mpc"
        expected = "[Dim:(k*m), Ope:*, Dim:(1*s), Ope:^, Num:-1, Ope:*, Dim:(M*pc), Ope:^, Num:-1]"

        # Act
        self.tokenizer.unit_string = input_str
        tokens = self.tokenizer.tokenize()

        token_list = TokenList(tokens)
        token_list.do_replacements()
        actual = str(token_list)

        # Assert
        self.assertEqual(expected, actual)

    def test_ps_per_sqrt_km(self):
        # Arrange
        input_str = "ps/√km"
        expected = "[Dim:(p*s), Ope:*, Dim:(k*m), Ope:^, Num:-0.5]"

        # Act
        self.tokenizer.unit_string = input_str
        tokens = self.tokenizer.tokenize()

        token_list = TokenList(tokens)
        token_list.do_replacements()
        actual = str(token_list)

        # Assert
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
