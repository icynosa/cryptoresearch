def calculer_modulo(a, b):
    return a % b


def pgcd_euclide(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Demande des valeurs à l'utilisateur
a = int(input("Entrez la valeur de a : "))
b = int(input("Entrez la valeur de b : "))

# Calculs et affichage des résultats
print("Modulo :", calculer_modulo(a, b))
print("PGCD :", pgcd_euclide(a, b))