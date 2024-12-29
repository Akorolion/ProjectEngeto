# projeсt 1

"""
projekt_1.py: prvni projekt do Engeto Online Python Akademie

author: Alexandr Korolev
email: onekorolev@gmail.com
"""

# default inputs

uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
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

prihlasovaci_jmeno = input("username: ")
prihlasovaci_heslo = input("password: ")

# kontrola prihlasovacich udaju

if prihlasovaci_jmeno in uzivatele and uzivatele[prihlasovaci_jmeno] == prihlasovaci_heslo:
    print(f"Welcome to the app,", prihlasovaci_jmeno)

    cislo_textu = input("Enter a number between 1 and 3 to select: ")

    # kontrola ze vstup je cislo

    if cislo_textu.isdigit():
      cislo_textu = int(cislo_textu)

      # kontrola spravneho cisla textu

      if cislo_textu in (1, 2, 3):
           vybrany_text = TEXTS[cislo_textu - 1]
    
    # (inactive command to check) print("Vybrany text:", vybrany_text)

           # Rozdělení textu na slova

           slova = vybrany_text.split()

           # počet slov

           print("There are", len(slova), "words in the selected text.")

           # počet slov začínajících velkými písmeny

           pocet_titlecap = 0
           for slovo in slova:
               if slovo.istitle():
                   pocet_titlecap += 1
           print("There are", pocet_titlecap, "titlecase words.")

           # pocet slov psanych velkymi pismeny

           pocet_fullcaps = 0
           for slovo in slova:
               if slovo.isupper():
                   pocet_fullcaps += 1
           print("There are", pocet_fullcaps, "uppercase words.")

           # pocet slov psanych malymi pismeny
          
           pocet_lowercase = 0
           for slovo in slova:
               if slovo.islower():
                   pocet_lowercase += 1
           print("There are", pocet_lowercase, "lowercase words.")

           # pocet cisel (ne cifer)
          
           pocet_cisel = 0
           for slovo in slova:
               if slovo.isdigit():
                   pocet_cisel += 1
           print("There are", pocet_cisel, "numeric strings.")

           # sumu všech čísel (ne cifer) v textu
          
           suma_cisel = 0
           for slovo in slova:
               if slovo.isdigit():
                   suma_cisel += int(slovo)
           print("The sum of all of the numbers", suma_cisel)

           # puvodni stav slovniku / dict: pocet pismen: pocet vyskytu

           delka_slova_count = {
               1: 0,
               2: 0,
               3: 0,
               4: 0,
               5: 0,
               6: 0,
               7: 0,
               8: 0,
               9: 0,
               10: 0,
               11: 0
           }

           # Loop pres slova abych spocital jejich delku

           for slovo in slova:
            
            # odstranim znaky co nejsou pismena
               
            slovo_bez = slovo.strip('.,!?";:')

            # dostanu delku slova bez extra znaku
               
            delka = len(slovo_bez)

            # Pokud tato delka jeste nebyla
               
            if delka not in delka_slova_count:
              delka_slova_count[delka] = 1

            else:

              # V opacnem pripade navysim pocet vyskytu o 1
                
              delka_slova_count[delka] = delka_slova_count[delka] + 1

# (inactive command to check) print("delka_slova_count",delka_slova_count)

           # Header
           print("--------------------------")
           print(" LEN | OCCURRENCES  | NR. ")
           print("--------------------------")

           # Display the data
           for delka, delka_slova_count in delka_slova_count.items():
            print(f" {delka:>3} | {'*' * delka_slova_count:<12} | {delka_slova_count:<3} ")

           # Footer
           print("--------------------------")

      else:
          print("Invalid text number, terminating the program")
          exit()

    else:
      print("Invalid input format, terminating the program")
      exit()
else:
    print("Unregistered user, terminating the program")
    exit()
