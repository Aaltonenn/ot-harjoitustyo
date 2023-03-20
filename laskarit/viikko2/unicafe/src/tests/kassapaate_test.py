import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassapaatteessa_oikea_maara_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_aluksi_oikea_maara_edullisia(self):
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_aluksi_oikea_maara_maukkaita(self):
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_edullinen_riittavasti_rahaa_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100240)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_maukas_riittavasti_rahaa_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100400)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_edullinen_liian_koyha_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_maukas_liian_koyha_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_edullinen_raha_riittaa_kortilla(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)
        return True

    def test_maukas_raha_riittaa_kortilla(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        return True

    def test_edullinen_raha_ei_riita_kortilla(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)
        return False
        
    def test_maukas_raha_ei_riita_kortilla(self):
        self.maksukortti = Maksukortti(399)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 399)
        self.assertEqual(self.kassapaate.maukkaat, 0)    
        return False

    def test_lataa_rahaa_kortille(self):
        self.maksukortti = Maksukortti(399)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 1399)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_lataa_negatiivista_rahaa_kortille(self):
        self.maksukortti = Maksukortti(399)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 399)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)