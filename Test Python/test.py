import numpy

from numpy.random import rand

# toto = 1
# while toto > 0.5:
#     print(toto)
#     toto = rand()

# print("fin", toto)

a = input("écris: ")
# print(a)
# print(type(a))
# print(len(a))

# for indice in range(len(a)):
#     print(a[indice])

# for carac in a:
#     print(carac)

list_numeric = list() #déclarer list python2
list_pasnumeric = [] #déclarer list python3

for carac in a:
    if carac.isnumeric():
        list_numeric.append(int(carac)*1.0)
        list_numeric.append(float(carac))
    else:
        list_pasnumeric.append(carac)

print("")
print("="*20)
print("Numeric", list_numeric)
print("Pas numeric", list_pasnumeric)

