# 1. Utilisation de xgcd(a, b)
a, b = 3, 7
g, u, v = xgcd(a, b)
print(f"PGCD({a}, {b}) = {g}")
print(f"Identité de Bézout : {a}*({u}) + {b}*({v}) = {g}")
print(f"Inverse de {a} mod {b} = {u % b}\n")

# 2. Benchmark de vitesse pour 5, 50 et 500 chiffres
import time

for digits in [5, 50, 500]:
    a = ZZ.random_element(10**(digits-1), 10**digits - 1)
    b = ZZ.random_element(10**(digits-1), 10**digits - 1)
    
    iterations = 10000
    t0 = time.perf_counter()
    for _ in range(iterations):
        _ = xgcd(a, b)
    t1 = time.perf_counter()
    
    avg_time_us = ((t1 - t0) / iterations) * 1e6
    print(f"Taille : {digits:3d} chiffres | Temps moyen par xgcd : {avg_time_us:.3f} µs")