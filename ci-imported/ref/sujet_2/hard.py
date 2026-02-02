def gcd(a, b):
    """
    Cette fonction calcule le pgcd de deux nombres a et b.
    Elle renvoie un triplet (g, x, y) tel que a*x + b*y = g = pgcd(a, b).
    """
    if a == 0:
        return abs(b)
    else:
        return gcd(b % a, a)


def egcd(a, b):
    """
    Cette fonction calcule le pgcd de deux nombres a et b.
    Elle renvoie un triplet (g, x, y) tel que a*x + b*y = g = pgcd(a, b).
    """
    if a == 0:
        if b < 0:
            return -b, 0, -1
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def generate_key(p, q):
    """
    Cette fonction génère la clé publique et la clé privée pour RSA.
    Elle prend deux nombres premiers p et q et renvoie un triplet (n, e, d)
    """
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while gcd(e, phi) != 1:
        e += 1
    if e >= phi:
        raise Exception("Pas de clé publique possible")
    g, x, y = egcd(e, phi)
    d = x % phi
    return n, e, d


def rsa_encode(message, key):
    """
    Cette fonction chiffre un message avec la méthode de RSA.
    key est un tuple (n, e) et message est un entier.
    message est une chaine de caractères.
    retourne une liste d'entiers.
    """
    n, e = key
    encoded_message = []
    for c in message:
        encoded_message.append(pow(ord(c), e, n))
    return encoded_message


def rsa_decode(message, key):
    """
    Cette fonction déchiffre un message avec la méthode de RSA.
    key est un tuple (n, d).
    message est une liste d'entiers.
    retourne une chaine de caractères.
    """
    n, d = key
    decoded_message = ""
    for c in message:
        decoded_message += chr(pow(c, d, n))
    return decoded_message
