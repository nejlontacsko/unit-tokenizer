from tokenizer import UnitTokenizer

if __name__ == '__main__':
    test_units = ["kW*h", "m^3*kg^-1*s^-2", "km/s/Mpc", "ps/√km"]

    # Sizing the first column
    len_max = 1
    for unit in test_units:
        len_max = max(len_max, len(unit))

    # Generate the table rows
    lines = []
    for unit in test_units:
        tokenizer = UnitTokenizer()
        tokenizer.unit_string = unit
        tokens = tokenizer.tokenize()

        tabs = "\t" * int((len_max - len(unit))/4 + 1)
        lines.append("{0}{1}{2}".format(unit, tabs, tokens))

    # Print the table
    print("Unit{0}Tokens".format(" " * (len_max - 1)))
    print("-" * int(len(max(lines, key=len)) + 1))
    for line in lines:
        print(line)