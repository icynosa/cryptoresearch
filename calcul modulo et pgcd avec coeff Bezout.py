def euclide_etendu(a, b):
    # Cas de base
    if b == 0:
        return a, 1, 0

    # Appel récursif
    pgcd, u1, v1 = euclide_etendu(b, a % b)

    # Mise à jour des coefficients selon la formule de Bézout
    u = v1
    v = u1 - (a // b) * v1

    return pgcd, u, v


# Demande des valeurs à l'utilisateur
a = int(input("Entrez la valeur de a : "))
b = int(input("Entrez la valeur de b : "))

# Calculs
pgcd, u, v = euclide_etendu(a, b)

# Affichage des résultats
print(f"PGCD({a}, {b}) = {pgcd}")
print(f"Coefficients de Bézout : u = {u}, v = {v}")
print(f"Vérification : {a} * ({u}) + {b} * ({v}) = {a * u + b * v}")