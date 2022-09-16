from unittest import TestCase
from main import encode


class TestEncode(TestCase):
    def test_primary_cypher(self):
        """
        Sprawdza czy przekształcanie w pierwszą stronę działa
        """

        self.assertEqual(encode("GBC"), "ABC")
        self.assertEqual(encode("DPL"), "EOU")

    def test_inverted_cypher(self):
        """
        Sprawdza czy przekształcanie w drugą stronę działa
        """

        self.assertEqual(encode("AYE"), "GRD")
        self.assertEqual(encode("OUI"), "PLK")

    def test_mixed_cyphers(self):
        """
        Sprawdza czy przekształcanie w obie strony w jednym tekście działa
        """

        self.assertEqual(encode("ADR"), "GEY")
        self.assertEqual(encode("PROGRAM"), "OYPAYGM")

    def test_small_letters(self):
        """
        Sprawdza czy małe litery pozostają niezmienne
        """

        self.assertEqual(encode("gbc"), "gbc")
        self.assertEqual(encode("dpl"), "dpl")
        self.assertEqual(encode("aye"), "aye")
        self.assertEqual(encode("oui"), "oui")
        self.assertEqual(encode("adr"), "adr")
        self.assertEqual(encode("program"), "program")
