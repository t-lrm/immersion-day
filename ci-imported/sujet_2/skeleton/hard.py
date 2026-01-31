def gcd(a, b):
    """
    Cette fonction calcule le pgcd de deux nombres a et b.
    Elle renvoie un triplet (g, x, y) tel que a*x + b*y = g = pgcd(a, b).
    """
    pass


def egcd(a, b):
    """
    Cette fonction calcule le pgcd de deux nombres a et b.
    Elle renvoie un triplet (g, x, y) tel que a*x + b*y = g = pgcd(a, b).
    """
    pass


def generate_key(p, q):
    """
    Cette fonction génère la clé publique et la clé privée pour RSA.
    Elle prend deux nombres premiers p et q et renvoie un triplet (n, e, d)
    """
    pass


def rsa_encode(message, key):
    """
    Cette fonction chiffre un message avec la méthode de RSA.
    key est un tuple (n, e) et message est un entier.
    message est une chaine de caractères.
    retourne une liste d'entiers.
    """
    pass


def rsa_decode(message, key):
    """
    Cette fonction déchiffre un message avec la méthode de RSA.
    key est un tuple (n, d).
    message est une liste d'entiers.
    retourne une chaine de caractères.
    """
    pass
