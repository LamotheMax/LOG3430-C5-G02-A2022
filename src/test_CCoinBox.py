import unittest
from CCoinBox import CCoinBox

class Test_CCoinBox(unittest.TestCase):

    def setUp(self):
        self.coin_box = CCoinBox()

    def test_ajouter_25_c(self):
        monnaie = self.coin_box.get_monnaie_courante()
        self.coin_box.ajouter_25c()
        self.assertEqual(self.coin_box.get_monnaie_courante(), monnaie + 1)