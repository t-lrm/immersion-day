def caesar_encode(message, key):
    """
    Cette fonction chiffre un message avec la méthode de César.
    """
    encoded_message = ""
    for c in message:
        if 'a' <= c <= 'z':
            rank = ord(c) - ord('a')
            rank = (rank + key) % 26
            letter = chr(ord('a') + rank)
            encoded_message += letter
        else:
            encoded_message += c
    return encoded_message


def caesar_decode(message, key):
    """
    Cette fonction déchiffre un message avec la méthode de César.
    """
    return caesar_encode(message, -key)


def substitution_encode(message, key):
    """
    Cette fonction chiffre un message avec la méthode de substitution.
    key est une chaîne de 26 caractères qui représente un nouvel alphabet.
    """
    encoded_message = ""
    for c in message:
        if 'a' <= c <= 'z':
            rank = ord(c) - ord('a')
            letter = key[rank]
            encoded_message += letter
        else:
            encoded_message += c
    return encoded_message


def substitution_decode(message, key):
    """
    Cette fonction déchiffre un message qui a été chiffré avec la fonction précédente.
    """
    reverse_key = [None] * 26 # implémentation bonus
    for i in range(len(key)):
        c = key[i]
        rank = ord(c) - ord('a')
        reverse_key[rank] = chr(ord('a') + i)
    decoded_message = ""
    for c in message:
        if 'a' <= c <= 'z':
            rank = ord(c) - ord('a')
            letter = reverse_key[rank]
            decoded_message += letter
        else:
            decoded_message += c
    return decoded_message


def vigenere_encode(message, key):
    """
    Cette fonction chiffre un message avec la méthode de Vigenère.
    key est une chaîne de lettres uniquement.
    """
    encoded_message = ""
    key_length = len(key)
    for i in range(len(message)):
        c = message[i]
        if 'a' <= c <= 'z':
            key_c = key[i % key_length]
            rank = ord(c) - ord('a')
            rank += ord(key_c) - ord('a')
            rank %= 26
            letter = chr(ord('a') + rank)
            encoded_message += letter
        else:
            encoded_message += c
    return encoded_message


def vigenere_decode(message, key):
    """
    Cette fonction déchiffre un message qui a été chiffré avec la fonction précédente.
    """
    decoded_message = ""
    key_length = len(key)
    for i in range(len(message)):
        c = message[i]
        if 'a' <= c <= 'z':
            key_c = key[i % key_length]
            rank = ord(c) - ord('a')
            rank -= ord(key_c) - ord('a')
            rank %= 26
            letter = chr(ord('a') + rank)
            decoded_message += letter
        else:
            decoded_message += c
    return decoded_message


def xor_encode(message, key):
    """
    Cette fonction chiffre un message avec la méthode XOR.
    key est une chaîne de 26 caractères qui représente un nouvel alphabet.
    """
    return "".join([chr(ord(message[i]) ^ ord(key[i % len(key)])) for i in range(len(message))])
