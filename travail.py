#Jobs01
for i in range(21):
    print(i)

#Jobs02
for i in range(0,21,2):
    print(i)  

    #Jobs03
    for i in range(1,21):
        print(f"Le carré de {i} est  {i**2}")

#Jobs04
n = int(input("entrez un nombre"))  

if n > 0:
    for i in range(1, n+1):
        print(f"\nTable de multiplication de {i}:")  
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}") 
else:
    print("5")

    #Jobs05

    n=1
    while n < 13 :
        print(n)
        n +=1


#Jobs06

n = int(input("entrez un entier : "))
i = 1
while i <=n :
    print(f"{i} x 7 = {i * 7}" )
    i += 1


#Jobs07

tour = 1
while tour <= 12:
    resultat = (tour * 3) - 2
    print (f"Tour {tour}:(3* {tour}) -2 = {resultat}")


#Jobs08



