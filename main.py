from tokenizer import UnitTokenizer

if __name__ == '__main__':
    test_units = ["kW*h", "m^3*kg^-1*s^-2", "km/s/Mpc", "ps/√km"]

    len_max = 1
    for unit in test_units:
        len_max = max(len_max, len(unit))

    for unit in test_units:
        tokenizer = UnitTokenizer(unit)
        tokens = tokenizer.tokenize()

        tabs = "\t" * int((len_max - len(unit))/4 + 1)
        print(unit, tabs, tokens)
