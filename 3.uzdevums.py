import csv

def lasi_csv(datnes_nosaukums):
    try:
        with open(datnes_nosaukums, 'r') as faila_iekšpuse:
            lasītājs = csv.reader(faila_iekšpuse)
            masīvs = list(lasītājs)
        return masīvs
    except FileNotFoundError:
        print(f"Datne ar nosaukumu '{datnes_nosaukums}' netika atrasta.")
        return None
    except Exception as e:
        print(f"Notikusi kļūda: {e}")
        return None

def izvadi_masīva_garumu(masīvs):
    if masīvs is not None:
        print(f"Masīva garums: {len(masīvs)}")

def izvadi_pirmo_elementu(masīvs):
    if masīvs is not None and len(masīvs) > 0:
        print(f"Pirmā elementa saturs: {masīvs[0]}")

def izvadi_pirmos_5_elementus(masīvs):
    if masīvs is not None:
        pirmie_5_elementi = masīvs[:5]
        print(f"Pirmo 5 elementu saturs: {pirmie_5_elementi}")

datnes_nosaukums = input("Ievadiet datnes nosaukumu: ")

datu_masīvs = lasi_csv(datnes_nosaukums)

izvadi_masīva_garumu(datu_masīvs)
izvadi_pirmo_elementu(datu_masīvs)
izvadi_pirmos_5_elementus(datu_masīvs)
