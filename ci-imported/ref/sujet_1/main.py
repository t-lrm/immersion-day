from math import pi
import random


def print_mario():
    """
    Affiche dans la console 'Hello, Mario!'
    """
    print("Hello, Mario!")

def get_mario_age(n: int) -> int:
    """
    Retourne l'âge de Mario dans n années
    """
    return n + 25

def diff(a: int, b: int) -> int:
    """
    Retourne la différence entre a et b
    """
    return a - b

def perimeter(r: float) -> float:
    """
    Retourne le périmètre d'un cercle de rayon r
    """
    return 2 * pi * r

def max(h1: int, h2: int) -> int:
    """
    Retourne le plus grand nombre entre a et b
    """
    if h1 > h2:
        return h1
    else:
        return h2

def give_grade(grade: int):
    """
    Retourne la lettre correspondant à la note
    """
    if grade < 0 or grade > 20:
        return "Note invalide"
    elif grade < 10:
        return "F"
    elif grade < 12:
        return "E"
    elif grade < 14:
        return "D"
    elif grade < 16:
        return "C"
    elif grade < 18:
        return "B"
    else:
        return "A"

def and_gate(hasFruit: bool, hasVegetable: bool) -> bool:
    """
    Retourne vraie si le toad a un fruit et un légume, faux sinon
    """
    return hasFruit and hasVegetable

def or_gate(hasFruit: bool, hasVegetable: bool) -> bool:
    """
    Retourne le résultat d'un OU logique entre a et b
    """
    return hasFruit or hasVegetable

def sum_number(n: int) -> int:
    """
    Retourne la somme des n premiers entiers
    """
    for i in range(n):
        n += i
    return n

def print_square(n: int):
    """
    Affiche dans la console un carré de n lignes et n colonnes
    """
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()

def print_triangle(n: int):
    """
    Affiche dans la console une pyramide de n étages
    """
    for i in range(n):
        for j in range(i + 1):
            print("*", end="")
        print()

def ask_div():
    """
    Demande à l'utilisateur deux nombres et retourne le résultat de la division
    """
    a = int(input("Indiquer le nombre de troupe disponible: "))
    b = int(input("Indiquer le nombre de front sur lesquel vous voulez attaquer: "))
    if b == 0:
        print("La division par 0 est interdite !")
    else:
        print("Vous aurez "+ str(a / b) +" troupes par front")

# --------------------------------------------------
# Medium
# --------------------------------------------------

def xor(hasDesert: bool, hasEntry: bool) -> bool:
    """
    Retourne le résultat d'un OU EXCLUSIF logique
    """
    return hasDesert != hasEntry

def nand(hasDesert: bool, hasEntry: bool) -> bool:
    """
    Retourne le résultat d'un NON ET logique
    """
    return not (hasDesert and hasEntry)

def is_even(n: int) -> bool:
    """
    Retourne True si n est pair, False sinon
    """
    return n % 2 == 0

def print_pyramid(n: int):
    """
    Affiche dans la console un triangle de n lignes
    """
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(i * 2 + 1):
            print("*", end="")
        for j in range(n - i - 1):
            print(" ", end="")
        print()

def count_division(n: int) -> int:
    """
    Retourne le nombre de fois que l'on peut diviser n par 2
    """
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count

# --------------------------------------------------
#                       Hard
# --------------------------------------------------

def is_amstrong(n: int) -> bool:
    """
    Retourne True si n est un nombre d'Armstrong, False sinon
    """
    # Count the number of digits
    count = 0
    tmp = n
    while tmp > 0:
        tmp //= 10
        count += 1
    # Sum of the digits
    sum = 0
    tmp = n
    while tmp > 0:
        sum += (tmp % 10) ** count
        tmp //= 10
    return sum == n

def guess_number():
    """
    Demande à l'utilisateur de deviner un nombre entre 0 et 100
    """
    number = random.randint(0, 100)
    guess = -1
    print("Devinez un nombre entre 0 et 100")
    while guess != number:
        guess = int(input("Entrez un nombre: "))
        if guess < number:
            print("C'est plus !")
        elif guess > number:
            print("C'est moins !")
    print("Bravo !")
