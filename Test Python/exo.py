"""
1.
"""

# nombre = int(input("Ecris un nombre entier positif: "))
# for nb in range(1, nombre + 1):
#     print(nb)

"""
2.
"""

# def nb_pos():
#     liste_nb = input("Ecris une suite de nombres positif ou négatif séparés par des espaces et valide une fois la liste complète: ").split()
#     liste_nb_pos = []
#     for nb in liste_nb:
#         if int(nb) > 0:
#             liste_nb_pos.append(int(nb))
#     return liste_nb_pos

# print(nb_pos())

#ou avec une compréhension de liste:

# def liste_pos():
#     x = input("Ecris une suite de nombres positif ou négatif séparés par des espaces et valide une fois la liste complète: ").split()
#     return [int(nb) for nb in x if int(nb) > 0]

# print(liste_pos())

"""
3.
"""
#1ère version corrigée, améliorée dans la suivante:

# def mot_commence_voyelle(ma_liste):
#     vowels = ["a", "e", "i", "o", "u", "y"]
#     liste_voyelle = []
#     for word in ma_liste:
#         for vowel in vowels:
#             if word[0].lower() == vowel:
#                 liste_voyelle.append(word)
#                 break
#     return liste_voyelle
# ma_liste = ["abracadabra", "banane", "soubrette", "italienne", "utopie"]
# print(mot_commence_voyelle(ma_liste))

#Version améliorée:

# def mot_commence_voyelle(ma_liste):
#     vowels = ["a", "e", "i", "o", "u", "y"]
#     liste_voyelle = []
#     for word in ma_liste:
#         if word[0].lower() in vowels:
#             liste_voyelle.append(word)
#     return liste_voyelle
# ma_liste = ["abracadabra", "banane", "soubrette", "italienne", "utopie"]
# print(mot_commence_voyelle(ma_liste))

#ou avec un input pour la liste de mots:

# def mot_commence_voyelle():
#     ma_liste = input("Entrez une liste de mots séparés par des espaces: ").split()
#     vowels = ["a", "e", "i", "o", "u", "y"]
#     liste_voyelle = []
#     for word in ma_liste:
#         if word[0].lower() in vowels:
#             liste_voyelle.append(word)
#     return liste_voyelle
# print(mot_commence_voyelle())

"""
4.
"""

# def nb_status():
#     nb = int(input("Ecris un nombre positif, négatif, ou nul: "))
#     if nb > 0:
#         return f"Le nombre {nb} est positif"
#     elif nb < 0:
#         return f"Le nombre {nb} est négatif"
#     else:
#         return f"Le nombre {nb} est nul"
# print(nb_status())

"""
5.
"""

# mot = input("Ecris un mot: ")
# if len(mot) > 5:
#     print(f"Le mot '{mot}' contient plus de 5 caractères.")
# else:
#     print(f"Le mot '{mot}' ne contient pas plus de 5 caractères")

"""
6.
"""
# Version où l'on demande à l'utilisateur de rentrer les 5 nombres 1 par 1:
# nombres = []
# for i in range(5):
#     nombre = int(input(f"Saisissez le nombre entier {i+1}: "))
#     nombres.append(nombre)
# print("Les nombres saisis sont:", nombres)

# liste_nombre = []
# nombres = input("Ecris 5 nombres entiers séparés par des espaces puis valide: ").split()
# for nb in nombres:
#     liste_nombre.append(int(nb))
# print(liste_nombre)

"""
7.
"""
