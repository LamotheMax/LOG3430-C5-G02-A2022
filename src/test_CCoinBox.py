import unittest
from CCoinBox import CCoinBox

class Test_CCoinBox(unittest.TestCase):

    def setUp(self):
        self.coin_box = CCoinBox()

    def test_ajouter_25_c(self):
        monnaie = self.coin_box.get_monnaie_courante()
        self.coin_box.ajouter_25c()
        self.assertEqual(self.coin_box.get_monnaie_courante(), monnaie + 1)

    def test_ajouter_25c_get_vente_permise(self):
        self.assertFalse(self.coin_box.get_vente_permise())

    def test_apres_vente_avec_2_monnaie_courante_vente_non_permise(self):
        self.coin_box.ajouter_25c()
        self.coin_box.ajouter_25c()
        self.coin_box.vente()
        self.assertFalse(self.coin_box.get_vente_permise())

    def test_vente_non_permise_apres_insertion_1_monnaie(self):
        self.coin_box.ajouter_25c()
        self.assertFalse(self.coin_box.get_vente_permise())