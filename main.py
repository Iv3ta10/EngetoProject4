ukoly = {}

def pridat_ukol():
    while True:
        uziv_nazev = input("Zadejte název úkolu: ")
        uziv_popis = input("Zadejte popis úkolu: ")
        if uziv_nazev == "" or uziv_popis == "":
            print("Zadal jste prázdný vstup.")
            continue

        if uziv_nazev in ukoly:
            print("Tento úkol již existuje.")
            continue

        ukoly[uziv_nazev] = uziv_popis
        print(f"Úkol '{uziv_nazev}' byl přidán.")
        break

def zobrazit_ukoly():
    if ukoly == {}:
        print("Seznam úkolů je prázdný.")
        return
    
    print("Seznam úkolů:")
    for index, ukol in enumerate(ukoly):
        print(f"{index + 1}. {ukol} - {ukoly[ukol]}")

def odstranit_ukol():
    zobrazit_ukoly()
    while True:
        try:
            odstraneny_index = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
        except(KeyboardInterrupt):
            exit()
        except:
            print("Zadal jste neplatný vstup.")
            continue

        if odstraneny_index <= 0 or odstraneny_index > len(ukoly):
            print("Tento úkol neexistuje.")
            continue

        odstraneny_klic = list(ukoly)[odstraneny_index - 1]
        print(f"Úkol '{odstraneny_klic}' byl odstraněn.")
        del ukoly[odstraneny_klic]
        break

def hlavni_menu():
    while True:
        print(
"""
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu
""")
        uziv_vstup = input("Vyberte možnost(1-4): ")
        if uziv_vstup == "1":
            pridat_ukol()
        elif uziv_vstup == "2":
            zobrazit_ukoly()
        elif uziv_vstup == "3":
            odstranit_ukol()
        elif uziv_vstup == "4":
            print("Konec programu.")
            break
        else: 
            print("Neplatná volba.")

if __name__ == "__main__":
    hlavni_menu()