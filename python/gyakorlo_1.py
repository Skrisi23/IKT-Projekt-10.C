#1 feladat
"""
szam1 = int(input("kérném az első számot: "))
szam2 = int(input("Kérném a második számot: "))
szam2 = int(input("Kérném a harmadik számot: "))
"""
#2 feladat
"""
list = []
szam1 = int(input('Kérek egy számot: '))
szam2 = int(input('Kérek egy másik számot: '))
szam3 = int(input('Kérek  egy harmadik számot számot: '))
list.append(szam1)
list.append(szam2)
list.append(szam3)
def nagyobb():
    print(max(list))
nagyobb()
"""


#3 feladat
"""
x = int(input("Kérek egy osztályzatot: "))

if  x<50:
    print("Elégtelen")
elif 50 <=x< 60:
    print("Elégséges")
elif 60 <=x< 70:
    print("Közepes")
elif 70 <=x< 85:
    print("Jó")
elif x>=85:   
    print("Jeles")
"""
#4 feladat
"""
szam1 = int(input("kérek egy számot: "))   

if (szam1 % 3 == 0 ):
    print('osztható 3-mal')
elif (szam1 % 5 == 0 ):
    print('osztható 5-tel')      
else:
    print('nem osztható egyikel sem')
"""
#5 feladat
"""
szam1 = int(input('Kérem az első számot: '))
szam2 = int(input('Kérem a második számot: '))
szam3 = int(input('Kérem a harmadik számot: '))

if szam1 + szam2 == szam3:
    print("Első szám + második szám",szam3)
if szam1 + szam3 == szam2:
    print("Első szám + harmadik szám",szam3)
if szam2 + szam3 == szam1:
    print("Másodi szám + harmadik szám",szam3)
"""
#6 feladat
""" 
szam1 = int(input('Kérek egy számot: '))
szam2 = int(input('Kérek egy másik számot: '))
szam3 = int(input('Kérek egy harmadik számot számot: '))

if szam1 % 2 == 0 and szam2 % 2 == 0 and  szam3 % 2 == 0:
    print('Igen')
else:
    print('Nem ') 
"""
#7 feladat    
"""
szo1 = str(input('Kérek egy szót: '))
szo2 = str(input('Kérek egy másik szót: '))


lista = [szo1 , szo2]
  
print(sorted(lista, key=len))

print("ABC sorrend")
"""
#8 feladat

szam1 = int(input("kérek egy pzitív egész számot: "))   



if (szam1 % 2 == 0):
    print('Osztható 2 vel')

else:
    (szam1 % 2 > 0)
    print("nem osztható 2 vel vagy 20 nál nagyobb")
