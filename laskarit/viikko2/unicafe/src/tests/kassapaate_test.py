import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
	def setUp(self):
		self.kassapaate = Kassapaate()
    
	def test_oikeat_aloitusarvot(self):
		self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
		self.assertEqual(self.kassapaate.edulliset, 0)
		self.assertEqual(self.kassapaate.maukkaat, 0)
	
	def test_edullinen_osto_toimii_kateisella(self):
		maksu = self.kassapaate.syo_edullisesti_kateisella(250)

		self.assertEqual(maksu, 10)
		self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.40)
		self.assertEqual(self.kassapaate.edulliset, 1)

		maksu = self.kassapaate.syo_edullisesti_kateisella(100)

		self.assertEqual(maksu, 100)
		self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.40)
		self.assertEqual(self.kassapaate.edulliset, 1)

	def test_maukas_osto_toimii_kateisella(self):
		maksu = self.kassapaate.syo_maukkaasti_kateisella(410)

		self.assertEqual(maksu, 10)
		self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.00)
		self.assertEqual(self.kassapaate.maukkaat, 1)

		maksu = self.kassapaate.syo_maukkaasti_kateisella(100)

		self.assertEqual(maksu, 100)
		self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.00)
		self.assertEqual(self.kassapaate.maukkaat, 1)

	def test_edullinen_osto_toimii_kortilla(self):
		maksukortti = Maksukortti(1000)

		maksu = self.kassapaate.syo_edullisesti_kortilla(maksukortti)

		self.assertEqual(maksu, True)
		self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
		self.assertEqual(self.kassapaate.edulliset, 1)

		maksukortti = Maksukortti(1)

		maksu = self.kassapaate.syo_edullisesti_kortilla(maksukortti)

		self.assertEqual(maksu, False)
		self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
		self.assertEqual(self.kassapaate.edulliset, 1)

	def test_maukas_osto_toimii_kortilla(self):
		maksukortti = Maksukortti(1000)

		maksu = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

		self.assertEqual(maksu, True)
		self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
		self.assertEqual(self.kassapaate.maukkaat, 1)

		maksukortti = Maksukortti(1)

		maksu = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

		self.assertEqual(maksu, False)
		self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
		self.assertEqual(self.kassapaate.maukkaat, 1)
	
	def test_kortin_lataus_onnistuu(self):
		maksukortti = Maksukortti(1000)

		self.kassapaate.lataa_rahaa_kortille(maksukortti, 100)

		self.assertEqual(maksukortti.saldo_euroina(), 11.00)
		self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1001.00)