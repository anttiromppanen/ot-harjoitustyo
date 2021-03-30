import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
  def setUp(self):
    self.kassapaate = Kassapaate()
    self.maksukortti = Maksukortti(440)
    self.korttiJossaEiRiittavastiMaukkaaseen = Maksukortti(399)
    self.korttiJossaEiRiittavastiEdulliseen = Maksukortti(239)

  def sentit_euroiksi(self, sentit):
    return round(sentit / 100, 2)

  def test_alustetun_kassapaatteen_rahamaara_oikein(self):
    saldoEuroissa = self.sentit_euroiksi(self.kassapaate.kassassa_rahaa)
    self.assertEqual(saldoEuroissa, 1000)

  def test_alustetun_kassapaatteen_myydyt_lounaat_nolla(self):
    myydytLounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat
    self.assertEqual(myydytLounaat, 0)

  def test_syo_maukkaasti_kateisella_kasvattaa_kassaa_riittavalla_summalla(self):
    self.kassapaate.syo_maukkaasti_kateisella(400)
    saldoEuroissa = self.sentit_euroiksi(self.kassapaate.kassassa_rahaa)
    self.assertEqual(saldoEuroissa, 1004)

  def test_syo_maukkaasti_kateisella_palauttaa_oikean_vaihtorahan(self):
    vaihtoraha = self.sentit_euroiksi(self.kassapaate.syo_maukkaasti_kateisella(500))
    self.assertEqual(vaihtoraha, 1)

  def test_syo_edullisesti_kateisella_kasvattaa_kassaa_riittavalla_summalla(self):
    self.kassapaate.syo_edullisesti_kateisella(240)
    saldoEuroissa = self.sentit_euroiksi(self.kassapaate.kassassa_rahaa)
    self.assertEqual(saldoEuroissa, 1002.4)

  def test_syo_edullisesti_kateisella_palauttaa_oikean_vaihtorahan(self):
    vaihtoraha = self.sentit_euroiksi(self.kassapaate.syo_edullisesti_kateisella(300))
    self.assertEqual(vaihtoraha, 0.6)

  def test_maukkaiden_maara_kasvaa_kun_summa_riittava(self):
    self.kassapaate.syo_maukkaasti_kateisella(400)
    self.assertEqual(self.kassapaate.maukkaat, 1)

  def test_edullisten_maara_kasvaa_kun_summa_riittava(self):
    self.kassapaate.syo_edullisesti_kateisella(240)
    self.assertEqual(self.kassapaate.edulliset, 1)

  def test_maukas_kassassa_ei_muutosta_kun_rahamaara_ei_riittava(self):
    self.kassapaate.syo_maukkaasti_kateisella(399)
    saldoEuroissa = self.sentit_euroiksi(self.kassapaate.kassassa_rahaa)
    self.assertEqual(saldoEuroissa, 1000)

  def test_edullinen_kassassa_ei_muutosta_kun_rahamaara_ei_riittava(self):
    self.kassapaate.syo_edullisesti_kateisella(239)
    saldoEuroissa = self.sentit_euroiksi(self.kassapaate.kassassa_rahaa)
    self.assertEqual(saldoEuroissa, 1000)

  def test_maukas_maksu_palautetaan_kun_rahamaara_ei_riittava(self):
    palautus = self.sentit_euroiksi(self.kassapaate.syo_maukkaasti_kateisella(399))
    self.assertEqual(palautus, 3.99)

  def test_edullinen_maksu_palautetaan_kun_rahamaara_ei_riittava(self):
    palautus = self.sentit_euroiksi(self.kassapaate.syo_edullisesti_kateisella(239))
    self.assertEqual(palautus, 2.39)

  def test_maukkaiden_maara_ei_kasva_kun_summa_ei_riittava(self):
    self.kassapaate.syo_maukkaasti_kateisella(399)
    self.assertEqual(self.kassapaate.maukkaat, 0)

  def test_edullisten_maara_ei_kasva_kun_summa_ei_riittava(self):
    self.kassapaate.syo_edullisesti_kateisella(239)
    self.assertEqual(self.kassapaate.edulliset, 0)

  def test_maukas_korttiosto_veloittaa_oikean_maaran_kun_summa_riittava(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
    self.assertEqual(self.sentit_euroiksi(self.maksukortti.saldo), 0.4)

  def test_edullinen_korttiosto_veloittaa_oikean_maaran_kun_summa_riittava(self):
    self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
    self.assertEqual(self.sentit_euroiksi(self.maksukortti.saldo), 2)

  def test_maukas_palauttaa_true_kun_summa_riittava(self):
    osto = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
    self.assertEqual(osto, True)

  def test_edullinen_palauttaa_true_kun_summa_riittava(self):
    osto = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
    self.assertEqual(osto, True)

  def test_maukas_korttiosto_lisaa_maukkaiden_maaraa(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
    self.assertEqual(self.kassapaate.maukkaat, 1)

  def test_edullinen_korttiosto_lisaa_edullisten_maaraa(self):
    self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
    self.assertEqual(self.kassapaate.edulliset, 1)

  def test_maukas_korttiosto_ei_veloita_jos_saldo_ei_riittava(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.korttiJossaEiRiittavastiMaukkaaseen)
    self.assertEqual(self.sentit_euroiksi(self.korttiJossaEiRiittavastiMaukkaaseen.saldo), 3.99)

  def test_edullinen_korttiosto_ei_veloita_jos_saldo_ei_riittava(self):
    self.kassapaate.syo_edullisesti_kortilla(self.korttiJossaEiRiittavastiEdulliseen)
    self.assertEqual(self.sentit_euroiksi(self.korttiJossaEiRiittavastiEdulliseen.saldo), 2.39)

  def test_maukkaiden_maara_ei_muutu_jos_saldo_ei_riittava(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.korttiJossaEiRiittavastiMaukkaaseen)
    self.assertEqual(self.kassapaate.maukkaat, 0)

  def test_edullisten_maara_ei_muutu_jos_saldo_ei_riittava(self):
    self.kassapaate.syo_edullisesti_kortilla(self.korttiJossaEiRiittavastiEdulliseen)
    self.assertEqual(self.kassapaate.edulliset, 0)

  def test_maukas_korttimaksu_palauttaa_false_jos_saldo_ei_riittava(self):
    tulos = self.kassapaate.syo_maukkaasti_kortilla(self.korttiJossaEiRiittavastiMaukkaaseen)
    self.assertEqual(tulos, False)

  def test_edullinen_korttimaksu_palauttaa_false_jos_saldo_ei_riittava(self):
    tulos = self.kassapaate.syo_edullisesti_kortilla(self.korttiJossaEiRiittavastiEdulliseen)
    self.assertEqual(tulos, False)

  def test_kassan_saldo_ei_muutu_maukkaan_korttiostossa(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
    self.assertEqual(self.sentit_euroiksi(self.kassapaate.kassassa_rahaa), 1000)

  def test_kassan_saldo_ei_muutu_edullisen_korttiostossa(self):
    self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
    self.assertEqual(self.sentit_euroiksi(self.kassapaate.kassassa_rahaa), 1000)

  def test_kortille_ladattaessa_kortin_saldo_paivittyy_oikein(self):
    self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
    self.assertEqual(self.sentit_euroiksi(self.maksukortti.saldo), 6.4)

  def test_kortille_ladattaessa_kassan_saldo_paivittyy_oikein(self):
    self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
    self.assertEqual(self.sentit_euroiksi(self.kassapaate.kassassa_rahaa), 1002)

  def test_kortille_ladattaessa_negatiivisella_arvolla_kortin_saldo_ei_muutu(self):
    self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
    self.assertEqual(self.sentit_euroiksi(self.maksukortti.saldo), 4.4)

  def test_kortille_ladattaessa_negatiivisella_arvolla_kassan_saldo_ei_muutu(self):
    self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
    self.assertEqual(self.sentit_euroiksi(self.kassapaate.kassassa_rahaa), 1000)