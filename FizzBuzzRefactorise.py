class FizzBuzz:

    def __init__(self, debut: int = 1, fin: int = 100):
        """
        Initialise la plage de nombres à traiter.
        :param debut: borne de départ (incluse)
        :param fin: borne de fin (incluse)
        """
        if debut > fin:
            raise ValueError("Le début doit être inférieur ou égal à la fin.")
        self.debut = debut
        self.fin = fin

        # Centralisation des règles dans une structure unique
        # -> plus facile à modifier ou étendre
        self.regles = {
            15: "FrisBee",
            3: "Fizz",
            5: "Buzz"
        }

    def _mot_pour(self, nombre: int) -> str:
        """
        Retourne le mot approprié pour un nombre donné selon les règles.
        :param nombre: entier à évaluer
        :return: mot associé ou le nombre sous forme de chaîne
        """
        for diviseur, mot in sorted(self.regles.items(), reverse=True):
            if nombre % diviseur == 0:
                return mot
        return str(nombre)

    def _genere_sequence(self, limite: int) -> list[str]:
        """
        Génère une liste des valeurs transformées de debut à limite.
        :param limite: borne de fin
        :return: liste des chaînes de caractères
        """
        return [self._mot_pour(i) for i in range(self.debut, limite + 1)]

    def affiche(self, n: int | None = None) -> str:
        """
        Construit la chaîne finale concaténée.
        Si n est fourni → affiche de 1 à n.
        Sinon → affiche de self.debut à self.fin.
        :param n: borne de fin facultative
        :return: chaîne concaténée
        """
        limite = n if n is not None else self.fin
        return "".join(self._genere_sequence(limite))


# Démonstration
if __name__ == "__main__":
    fizz = FizzBuzz()
    print(fizz.affiche(15))

