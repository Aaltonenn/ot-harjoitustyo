import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(1550)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 25.50 euroa")

    def test_rahan_ottaminen_jos_raha_riittaa(self):
        self.maksukortti.ota_rahaa(950)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.50 euroa")
        return True

    
    def test_rahan_ottaminen_jos_raha_ei_riita(self):
        self.maksukortti.ota_rahaa(1001)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        return False