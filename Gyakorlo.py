with open('SuperBowl.txt', 'r', encoding='utf-8') as f:
    adatok = []
    for sor in f:
        sor = sor.strip().split(';')
        donto = {
            'Ssz': sor[0],
            'Dátum': sor[1],
            'Győztes': sor[2],
            'Eredmény': sor[3],
            'Vesztes': sor[4],
            'Helyszín': sor[5],
            'VárosÁllam': sor[6],
            'Nézőszám': sor[7],
            

        }
        adatok.append(donto)

print(len(adatok))

legtobb_nezo = max(adatok, key=lambda x: x['Nézőszám'])
print