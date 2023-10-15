'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Alžběta Karolyiová
email: akarolyiova@gmail.com
discord: betykar
'''
TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#napsat program tak, abychom dopředu nevěděli, kolik textů máme k dispozici
#odevzdat pak na githubu

oddelovac = "-" * 40

#zjištění počtu textů
pocet_textu = len(TEXTS)

#registrovaní uživatelé
uzivatele = {
    "bob" : "123", 
    "ann" : "pass123", 
    "mike" : "password123", 
    "liz" : "pass123"
}

#očíslování textů
cisla_textu = {}
for x, text in enumerate(TEXTS, 1):
    cisla_textu[x] = text

#vstup od uživatele
jmeno = input("username: ")
if jmeno in uzivatele:
    heslo = input("password: ")
    if heslo == uzivatele[jmeno]:
        print(oddelovac, f"Welcome to the app, {jmeno}\nWe have {pocet_textu} texts to be analyzed.", oddelovac, sep="\n")
    else:
        print("unregistered user, terminating the program..")
        quit()
else:
    print("unregistered user, terminating the program..")
    quit()

#výběr čísla textu 
vyber_textu = input(f"Enter a number btw. 1 and {pocet_textu} to select: ")
if vyber_textu.isdigit():
    vyber_textu = int(vyber_textu)
    if 1 <= vyber_textu <= pocet_textu:
        vyber_textu = vyber_textu - 1
    else:
        print(oddelovac,"Selected number is not in the range.", oddelovac, sep="\n")
        quit()
else:
    print(oddelovac,"You have not inserted a number.", oddelovac, sep="\n")
    quit()

# nasleduje analyza textu

slova_neocistena = TEXTS[vyber_textu].split()
slova = []

for slovo in slova_neocistena:
    slovo = slovo.strip(",.")
    slova.append(slovo)

pocet_slov_textu = len(slova)
print(oddelovac, f"There are {pocet_slov_textu} words in the selected text.", sep="\n")

slova_velke_pismeno = 0
slova_velkymi_pismeny = 0
slova_malymi_pismeny = 0
pocet_ciselnych_str = 0
soucet_cisel = 0
for slovo in slova:
    if slovo[0].isupper():
        slova_velke_pismeno += 1
    if slovo.isupper() and slovo.isalpha():
        slova_velkymi_pismeny += 1
    if slovo.islower() and slovo.isalpha():
        slova_malymi_pismeny += 1
    if slovo.isnumeric():
        pocet_ciselnych_str += 1
        soucet_cisel += int(slovo)
print(f"There are {slova_velke_pismeno} titlecase words.", 
      f"There are {slova_velkymi_pismeny} uppercase words.", 
      f"There are {slova_malymi_pismeny} lowercase words.", 
      f"There are {pocet_ciselnych_str} numeric strings.", 
      f"The sum of all the numbers {soucet_cisel}", oddelovac, sep="\n")

#sloupcový graf, četnost slov dle počtu znaků;
#výskyt délky slova bude reprezentovaný jednou hvězdičkou

#udělám slovník, do kterého uchovám informaci o četnosti jednotlivých slov dle délky
delka_slov_cetnost = {}

#projdu text a spočítám počet slov dle četnosti (klíč je počet znaků slova)
for slovo in slova:
    delka_slova = len(slovo)
    if delka_slova in delka_slov_cetnost:
        delka_slov_cetnost[delka_slova] += 1
    else:
        delka_slov_cetnost[delka_slova] = 1

#seřazený slovník, vypsání do grafu
delka_slov_cetnost_sorted = dict(sorted(delka_slov_cetnost.items()))
print("LEN|  OCCURENCES  |NR.", oddelovac, sep="\n")
for delka, pocet in delka_slov_cetnost_sorted.items():
    graf = "*" * pocet
    sirka = max(delka_slov_cetnost_sorted.values())
    print(f"{delka:3}|{graf:<14}|{pocet:1}")






                             
