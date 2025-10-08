class FizzBuzz:
    def __init__(self, debut=1, fin=100):
        self.debut = debut
        self.fin = fin

    def _mot_pour(self, n):
        """Renvoie le mot approprié pour un nombre donné"""
        if n % 15 == 0:
            return "FrisBee"
        if n % 3 == 0:
            return "Fizz"
        if n % 5 == 0:
            return "Buzz"
        return str(n)

    def affiche(self, n=None):
        """Construit la chaîne finale concaténée.
        Si n est fourni → affiche de 1 à n.
        Sinon → affiche de self.debut à self.fin.
        """
        # Si un paramètre n est passé, on l’utilise à la place de self.fin
        limite = n if n is not None else self.fin
        return "".join(self._mot_pour(i) for i in range(self.debut, limite + 1))


# Démonstration
if __name__ == "__main__":
    fizz = FizzBuzz()
    print(fizz.affiche(15))

