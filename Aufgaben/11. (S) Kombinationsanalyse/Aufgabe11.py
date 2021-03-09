import sys
import math

def alg1(iteration, coins, zaehler, n, zw1):
    if zaehler >= 0:
        while True:
            if iteration[zaehler] == coins[-1]:
                break
            else:
                if zaehler < len(iteration)-1:
                    if coins[coins.index(iteration[zaehler])+1] == coins[coins.index(iteration[zaehler+1])]:
                        break
                iteration[zaehler] = coins[coins.index(iteration[zaehler])+1]

                for i in range(1, len(iteration)-zaehler):                    
                    iteration[zaehler+i] = coins[coins.index(iteration[zaehler])+i]

                print(iteration)
                zw1 += alg2(iteration, len(iteration)-1, 0, n)
                zw1 += alg1(iteration, coins, (len(iteration)-1), n, 0)

        zw1 += alg1(iteration, coins, zaehler-1, n, 0)
        return zw1

    else:
        return zw1

def alg2(coins, laenge, zw, n):
    if laenge > 0:
        for i in range(coins[laenge], n, coins[laenge]):
            if alg2(coins, laenge-1, i+zw, n) == 1:
                return 1
            else:
                return 0
        return 0
    else:
        if (n - zw) % coins[0] == 0:
            return 1
        else:
            return 0     



n = 9
s = 3
coins = [5, 6, 10]

erg = 0
coins.sort()
zähl = 0
anzahl = 1


print(n, s)
print(coins)
print()


while anzahl <= len(coins):
    iteration = []
    for z in range(anzahl):
        iteration.append(coins[z])
    print(iteration)
    erg += alg2(iteration, len(iteration)-1, 0, n)
    zaehler = len(iteration)-1

    erg += alg1(iteration, coins, zaehler, n, 0)
    anzahl += 1

print(erg)

