from tokens.tokens import *


class TokenList:
    def __init__(self, tokens: list[UnitToken]):
        self.tokens = tokens

    def do_replacements(self):
        self.replace_single()
        self.replace_div_and_sqrt()

        while self.tokens.count(UnitToken.div()) > 0:
            self.replace_div_with_pow()
        while self.tokens.count(UnitToken.sqrt()):
            self.replace_sqrt_with_pow()

        self.remove_duplicates()
        self.trim_operators()

    def replace_single(self):
        """Extend the single Dim tokens with the first exponent."""
        if len(self.tokens) == 1 and self.tokens[0].type == TokenTypeEnum.Dimension:
            self.tokens.append(UnitToken.pow())
            self.tokens.append(UnitToken.one())
            return

    def replace_div_and_sqrt(self):
        for i in range(len(self.tokens)):
            if self.tokens[i].value == "/" and self.tokens[i + 1].value == "√":
                self.tokens[i].value = "*"
                self.tokens.remove(self.tokens[i + 1])
                self.tokens.insert(i + 3, UnitToken.pow())
                self.tokens.insert(i + 4, UnitToken(TokenTypeEnum.Number, "-0.5"))
                self.tokens.insert(i + 5, UnitToken.mul())

    def replace_div_with_pow(self):
        for i in range(len(self.tokens)):
            if self.tokens[i].value == "/":
                self.tokens[i].value = "*"
                self.tokens.insert(i + 2, UnitToken.pow())
                self.tokens.insert(i + 3, UnitToken.neg_one())
                self.tokens.insert(i + 4, UnitToken.mul())

    def replace_sqrt_with_pow(self):
        for i in range(len(self.tokens)):
            if self.tokens[i].value == "√":
                self.tokens.insert(i + 3, UnitToken.pow())
                self.tokens.insert(i + 4, UnitToken(TokenTypeEnum.Number, "0.5"))
                self.tokens.insert(i + 5, UnitToken.mul())
                self.tokens.remove(self.tokens[i])

    def remove_duplicates(self):
        """The whole list can have duplications, but operators with the same value should not follow each other."""
        for i in range(len(self.tokens) - 1, 0, -1):
            if self.tokens[i] == self.tokens[i - 1]:
                self.tokens.pop(i)

    def trim_operators(self):
        """Remove operators at the beginning and end of the list assuming that the duplications where removed before."""
        if len(self.tokens) == 0:
            return
        if self.tokens[0].type == TokenTypeEnum.Operator:
            self.tokens.pop(0)
        if self.tokens[-1].type == TokenTypeEnum.Operator:
            self.tokens.pop(-1)

    def __str__(self):
        return str(self.tokens)
