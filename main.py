ukoly = []

def pridat_ukol():
    uziv_nazev = input("Zadejte název úkolu: ")
    uziv_popis = input("Zadejte popis úkolu: ")
    cely_ukol = " - ".join([uziv_nazev, uziv_popis])
    if uziv_nazev == "" or uziv_popis == "":
        print("Zadal jste prázdný vstup")
        pridat_ukol()
    else:
        ukoly.append(cely_ukol)
        print(f"Úkol '{uziv_nazev}' byl přidán.")

def zobrazit_ukoly():
    if ukoly == []:
        print("Seznam úkolů je prázdný.")
    else:
        print("Seznam úkolů:")
        for index, ukol in enumerate(ukoly):
            print(f"{index + 1}. {ukol}")

def odstranit_ukol():
    zobrazit_ukoly()
    odstraneny_ukol = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
    try:
        if ukoly[odstraneny_ukol - 1] in ukoly:
            print(f"Úkol '{ukoly[odstraneny_ukol - 1]}' byl odstraněn.")
            ukoly.remove(ukoly[odstraneny_ukol - 1])
    except IndexError:
        print("Tento úkol neexistuje.")

def hlavni_menu():
    print(
"""
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu
""")
    try:
        uziv_vstup = int(input("Vyberte možnost(1-4): "))
        if uziv_vstup == 1:
            pridat_ukol()
            hlavni_menu()
        elif uziv_vstup == 2:
            zobrazit_ukoly()
            hlavni_menu()
        elif uziv_vstup == 3:
            odstranit_ukol()
            hlavni_menu()
        elif uziv_vstup == 4:
            print("Konec programu.")
        elif uziv_vstup > 4 or uziv_vstup < 1:
            print("Neplatná volba.")
            hlavni_menu()
    except:
        print("Neplatná volba.")
        hlavni_menu()

if __name__ == "__main__":
    hlavni_menu()