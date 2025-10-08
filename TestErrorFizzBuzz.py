import unittest
from FizzBuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_affiche_avec_parametre(self):
        fb = FizzBuzz()
        resultat = fb.affiche(15)
        self.assertEqual(resultat, "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee")

if __name__ == "__main__":
    unittest.main()

