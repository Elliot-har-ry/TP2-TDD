import unittest
from FizzBuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_affiche_contient_FrisBee(self):
        """Étape 1 : Test initial — doit contenir 'FrisBee'"""
        fb = FizzBuzz()
        resultat = fb.affiche()
        self.assertIn("FrisBee", resultat)

    def test_affiche_commence_bien(self):
        """Étape 2 : Test sur le début de la chaîne"""
        fb = FizzBuzz()
        resultat = fb.affiche()
        self.assertTrue(resultat.startswith("12Fizz4BuzzFizz78FizzBuzz"))

    def test_autre_intervalle(self):
        """Étape 3 : Test d'un intervalle personnalisé"""
        fb = FizzBuzz(1, 20)
        resultat = fb.affiche()
        self.assertTrue(resultat.endswith("19Buzz"))

    def test_aucune_erreur_pour_1_a_100(self):
        """Étape 4 : Vérifie qu'on a bien 100 valeurs concaténées"""
        fb = FizzBuzz()
        resultat = fb.affiche()
        self.assertIsInstance(resultat, str)
        self.assertGreater(len(resultat), 0)

if __name__ == '__main__':
    unittest.main()

