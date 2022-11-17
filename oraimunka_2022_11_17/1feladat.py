#1 feladat
"""
szam = 1
while szam <= 20:
    if szam % 2 == 1:
        print(szam)
        szam += 1
    elif szam % 2 == 0:
        print(szam)
        szam += 1        
"""
#------------------------------------------------
#2 feladat
"""
list = []
szam = int(input("Kérek gy számot: "))
szam.append(list)
szam = 0
for a in list:
    szam += 1
    avg = szam / len(list)
        
print("A szám átlaga:",szam)
"""
#------------------------------------------------
#3 feladat
"""
also = int(input("Alső szám: "))
felso = int(input("Felső szám: "))

list = range(also,felso+1)
sum = 0
i = 0

for x in list:
    sum = sum + x
    i += 1

print(sum, sum/i)
"""