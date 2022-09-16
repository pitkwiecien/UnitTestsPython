from unittest import TestCase
from main import encode


class TestEncode(TestCase):
    def test_primary_cypher(self):
        self.assertEqual(encode("GBC"), "ABC")
        self.assertEqual(encode("DPL"), "EOU")

    def test_inverted_cypher(self):
        self.assertEqual(encode("AYE"), "GRD")
        self.assertEqual(encode("OUI"), "PLK")

    def test_mixed_cyphers(self):
        self.assertEqual(encode("ADR"), "GEY")
        self.assertEqual(encode("PROGRAM"), "OYPAYGM")

    def test_small_letters(self):
        self.assertEqual(encode("gbc"), "gbc")
        self.assertEqual(encode("dpl"), "dpl")
        self.assertEqual(encode("aye"), "aye")
        self.assertEqual(encode("oui"), "oui")
        self.assertEqual(encode("adr"), "adr")
        self.assertEqual(encode("program"), "program")