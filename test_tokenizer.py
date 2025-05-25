import unittest
from tokenizer import UnitTokenizer

class TestUnitTokenizer(unittest.TestCase):

    def test_kWh(self):
        expected = ['k', 'W', '*', 'h']
        tokenizer = UnitTokenizer("kW*h")
        actual = tokenizer.tokenize()
        self.assertEqual(expected, actual)

    def test_m3_kg_s2(self):
        expected = ['m', '^3', '*', 'kg', '^-1', '*', 's', '^-2']
        tokenizer = UnitTokenizer("m^3*kg^-1*s^-2")
        actual = tokenizer.tokenize()
        self.assertEqual(expected, actual)

    def test_km_per_s_per_mpc(self):
        expected = ['k', 'm', '/', 's', '/', 'M', 'pc']
        tokenizer = UnitTokenizer("km/s/Mpc")
        actual = tokenizer.tokenize()
        self.assertEqual(expected, actual)

    def test_ps_per_sqrt_km(self):
        expected = ['p', 's', '/', '√', 'k', 'm']
        tokenizer = UnitTokenizer("ps/√km")
        actual = tokenizer.tokenize()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()