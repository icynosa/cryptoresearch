def pgcd_etendu_iteratif(a, b):
    # Initialisation des coefficients
    # u1, v1 pour 'a' et u2, v2 pour 'b'
    u1, v1 = 1, 0
    u2, v2 = 0, 1

    while b != 0:
        q = a // b  # Quotient de la division euclidienne

        # Mise à jour de a et b (comme dans l'algorithme d'Euclide classique)
        a, b = b, a % b

        # Mise à jour simultanée des coefficients de Bézout
        u1, u2 = u2, u1 - q * u2
        v1, v2 = v2, v1 - q * v2

    # À la fin de la boucle, 'a' contient le PGCD,
    # et (u1, v1) sont les coefficients de Bézout
    return a, u1, v1


# Saisie utilisateur
a = int(input("Entrez la valeur de a : "))
b = int(input("Entrez la valeur de b : "))

# Calcul
pgcd, u, v = pgcd_etendu_iteratif(a, b)

# Affichage des résultats
print(f"PGCD({a}, {b}) = {pgcd}")
print(f"Coefficients de Bézout : u = {u}, v = {v}")
print(f"Vérification : {a} * ({u}) + {b} * ({v}) = {a * u + b * v}")