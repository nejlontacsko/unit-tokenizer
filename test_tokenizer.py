import unittest
from tokenizer import UnitTokenizer

class TestUnitTokenizer(unittest.TestCase):

    def test_kWh(self):
        expected = "[Dim:(k*W), Ope:*, Dim:(1*h)]"
        tokenizer = UnitTokenizer("kW*h")
        actual = tokenizer.tokenize()
        self.assertEqual(expected, str(actual))

    def test_m3_kg_s2(self):
        expected = "[Dim:(1*m), Ope:^, Num:3, Ope:*, Dim:(k*g), Ope:^, Num:-1, Ope:*, Dim:(1*s), Ope:^, Num:-2]"
        tokenizer = UnitTokenizer("m^3*kg^-1*s^-2")
        actual = tokenizer.tokenize()
        self.assertEqual(expected, str(actual))

    def test_km_per_s_per_mpc(self):
        expected = "[Dim:(k*m), Ope:/, Dim:(1*s), Ope:/, Dim:(M*pc)]"
        tokenizer = UnitTokenizer("km/s/Mpc")
        actual = tokenizer.tokenize()
        self.assertEqual(expected, str(actual))

    def test_ps_per_sqrt_km(self):
        expected = "[Dim:(p*s), Ope:/, Ope:√, Dim:(k*m)]"
        tokenizer = UnitTokenizer("ps/√km")
        actual = tokenizer.tokenize()
        self.assertEqual(expected, str(actual))

if __name__ == '__main__':
    unittest.main()