class FizzBuzz:

    def __init__(self, debut: int = 1, fin: int = 100):
        """
        Initialise les bornes de la séquence.
         debut: Premier nombre inclus.
         fin: Dernier nombre inclus.
        """
        if debut > fin:
            raise ValueError("Le début doit être inférieur ou égal à la fin.")
        self.debut = debut
        self.fin = fin

        # Dictionnaire des règles de remplacement
        self.regles = {
            3: "Fizz",
            5: "Buzz",
            15: "FrisBee"
        }

    def _mot_pour(self, n: int) -> str:
        """
        Retourne le mot correspondant au nombre selon les règles définies.
         n: nombre à évaluer.
         return: mot associé ou le nombre sous forme de chaîne.
        """
        for diviseur, mot in sorted(self.regles.items(), reverse=True):
            if n % diviseur == 0:
                return mot
        return str(n)

    def genere_sequence(self) -> list[str]:
        """
        Génère la liste complète des valeurs FizzBuzz.
        :return: liste de chaînes.
        """
        return [self._mot_pour(i) for i in range(self.debut, self.fin + 1)]

    def affiche(self) -> str:
        """
        Concatène et renvoie la séquence complète sous forme d'une seule chaîne.
        :return: chaîne concaténée des valeurs FizzBuzz.
        """
        return "".join(self.genere_sequence())


# 💡 Démonstration (ne s’exécute pas pendant les tests)
if __name__ == "__main__":
    fizzbuzz = FizzBuzz()
    print(fizzbuzz.affiche())

