from sujet_2.skeleton.doors import Door
from sujet_2.ref.warmup import *


def caesar_doors(messages):
    """
    Cette fonction crée une liste de portes chiffrées avec la méthode de César.
    Chaque porte est chiffrée avec une clé qui est la longueur du message.
    """
    return [Door(caesar_encode(message, len(message)), caesar_decode) for message in messages]


def transposition_encode(message, key):
    """
    Cette fonction chiffre un message avec la méthode de transposition.
    key est une liste d'entiers.
    """
    key_len = len(key)
    encoded_message = ""
    for i in range(key_len):
        x = key.index(i)
        for j in range(x, len(message), key_len):
            encoded_message += message[j]
    return encoded_message


def transposition_decode(message, key):
    """
    Cette fonction déchiffre un message avec la méthode de transposition.
    key est une liste d'entiers.
    """
    key_len = len(key)
    result = [[] for _ in range(key_len)]
    idx = 0
    for i in range(key_len):
        x = key.index(i)
        height = len(message) // key_len
        if x < len(message) % key_len:
            height += 1
        for _ in range(height):
            result[x].append(message[idx])
            idx += 1
    decoded_message = ""
    for i in range(len(message)):
        decoded_message += result[i % key_len][i // key_len]
    return decoded_message


def hill_encode(message, key):
    """
    Cette fonction chiffre un message avec la méthode de Hill.
    key est une matrice 2x2.
    Tous les caractères qui ne sont pas des lettres sont ignorés sont remplacés par des "x".
    """
    encoded_message = ""
    if len(message) % 2 == 1:
        message += "x"
    for i in range(0, len(message), 2):
        rank1 = ord(message[i]) - ord('a')
        rank2 = ord(message[i + 1]) - ord('a')
        if rank1 < 0 or rank1 > 25:
            rank1 = 23
        if rank2 < 0 or rank2 > 25:
            rank2 = 23
        encoded_message += chr((rank1 * key[0][0] + rank2 * key[0][1]) % 26 + ord('a'))
        encoded_message += chr((rank1 * key[1][0] + rank2 * key[1][1]) % 26 + ord('a'))
    return encoded_message


def hill_decode(message, key):
    """
    Cette fonction déchiffre un message avec la méthode de Hill.
    key est une matrice 2x2.
    Tous le message ne peut que contenir des lettres.
    """
    inverse_matrix = [[key[1][1], -key[0][1]], [-key[1][0], key[0][0]]]
    determinant = key[0][0] * key[1][1] - key[0][1] * key[1][0]
    if determinant == 0:
        return "La matrice n'est pas inversible."
    modular_inverse = 1
    while (determinant * modular_inverse) % 26 != 1:
        modular_inverse += 1
    for i in range(2):
        for j in range(2):
            inverse_matrix[i][j] *= modular_inverse
            inverse_matrix[i][j] %= 26
    return hill_encode(message, inverse_matrix)


if __name__ == "__main__":
    doors = caesar_doors(["joe", "seme", "phare", "champ"])
    print([door.message for door in doors])
