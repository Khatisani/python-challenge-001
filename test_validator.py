import unittest
from validator import bracket_validator

class TestBracketValidator(unittest.TestCase):

    def test_proper_match(self):
        self.assertTrue(bracket_validator("life()"))
        self.assertTrue(bracket_validator("(life)"))
        self.assertTrue(bracket_validator("(l)ife"))

        self.assertTrue(bracket_validator("life[]"))
        self.assertTrue(bracket_validator("[life]"))
        self.assertTrue(bracket_validator("[l]ife"))

        self.assertTrue(bracket_validator("life{}"))
        self.assertTrue(bracket_validator("{lif}e"))
        self.assertTrue(bracket_validator("{l}ife"))


    def test_proper_match_two_brackets(self):
        self.assertTrue(bracket_validator("life(())"))
        self.assertTrue(bracket_validator("(li(f)e"))
        self.assertTrue(bracket_validator("((l)ife)"))   

        self.assertTrue(bracket_validator("life[[]]"))
        self.assertTrue(bracket_validator("[[i]f]e"))
        self.assertTrue(bracket_validator("[[l]ife]"))   

        self.assertTrue(bracket_validator("life{{}}"))
        self.assertTrue(bracket_validator("{{i}f}e"))
        self.assertTrue(bracket_validator("{{l}ife}"))   


    def test_proper_match_three_brackets(self):
        self.assertTrue(bracket_validator("li(f)e(())"))
        self.assertTrue(bracket_validator("(l(i)(f)e)"))
        self.assertTrue(bracket_validator("((l)if()e)"))   

        self.assertTrue(bracket_validator("li[f]e[[]]"))
        self.assertTrue(bracket_validator("[l[i][f]e]"))
        self.assertTrue(bracket_validator("[[l]if[]]e"))   

        self.assertTrue(bracket_validator("li{f}e{{}}"))
        self.assertTrue(bracket_validator("{l{i}{f}e}"))
        self.assertTrue(bracket_validator("{{l}if{}e}"))   


    def test_extra_bracket(self):
        self.assertFalse(bracket_validator("life(()"))
        self.assertFalse(bracket_validator("life)"))
        self.assertFalse(bracket_validator("l(if)(()e"))

        self.assertFalse(bracket_validator("l[if][e[]"))
        self.assertFalse(bracket_validator("l[if]e]"))
        self.assertFalse(bracket_validator("l[if[[]]e"))

        self.assertFalse(bracket_validator("life{}}}"))
        self.assertFalse(bracket_validator("lif{{e}"))
        self.assertFalse(bracket_validator("l{if}{{e}"))


    def test_mixed_brackets(self):
        self.assertTrue(bracket_validator("()[]{}"))
        self.assertTrue(bracket_validator("([{}])"))
        self.assertTrue(bracket_validator("(((())))"))

        self.assertFalse(bracket_validator("(]"))
        self.assertFalse(bracket_validator("{[}]"))


    def test_start_opening_bracket(self):
        self.assertFalse(bracket_validator("life)()"))

        self.assertFalse(bracket_validator("][]life"))

        self.assertFalse(bracket_validator("}{life}"))


    def test_end_closing_bracket(self):
        self.assertFalse(bracket_validator("()(life"))

        self.assertFalse(bracket_validator("[]li[fe"))

        self.assertFalse(bracket_validator("lif{}e{"))

    def test_string(self):
        with self.assertRaises(ValueError):
            (789)

    def test_empty_string(self):
        self.assertTrue("")


