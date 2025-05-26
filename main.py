from fractions.fraction_builder import FractionBuilder
from tokens.tokenizer import UnitTokenizer
from tokens.token_list import TokenList


def print_line():
    print("-" * int(len(max(lines, key=len)) + 1))


if __name__ == '__main__':
    # test_units = ["kW*h", "m^3*kg^-1*s^-2", "km/s/Mpc", "ps/√km"]
    # test_units = ["m", "Hgmm", "km/h", "Pa*s", "hPa^-1"]

    # These two could break the tokenizer before the implementation of compound units,
    #   generating Dim:(c*d) and Dim:(T*orr) tokens respectively
    # test_units = ["cd", "Torr"]

    # Made up complex units
    test_units = ["cd/Torr*s^-2*hPa^-1*kg^-1"]

    # Sizing the first column
    len_max = 1
    for unit in test_units:
        len_max = max(len_max, len(unit))

    # Generate the table rows
    lines = []
    tokens_lists = []
    for unit in test_units:
        tokenizer = UnitTokenizer()
        tokenizer.unit_string = unit
        tokens = tokenizer.tokenize()
        tokens_lists.append(tokens)

        tabs = "\t" * int((len_max - len(unit))/4 + 1)
        lines.append("{0}{1} {2}".format(unit, tabs, tokens))

    # Print the table
    print("Unit{0}Tokens".format(" " * (len_max - 1)))
    print_line()
    for line in lines:
        print(line)

    print("\nReplacement tokens:")
    print_line()
    tabs = "\t" * int(len_max/4 + 1)
    lists = []
    for tokens in tokens_lists:
        l = TokenList(tokens)
        l.do_replacements()
        lists.append(l)
        print(tabs, l)

        fb = FractionBuilder(l)
        fb.find_denominators()
        fb.find_nominators()

        print("REMAIN", fb.token_list)


    """
    print("FRACTIONS:")
    # Print the fractions
    for tokens in tokens_lists:
        frac = Fraction()
        for token in tokens:
            frac.append_numerator(token)
        print(frac)
    """