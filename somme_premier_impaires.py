#Programme qui demande à l'utilisateur de taper un entier n, puis qui calcule la somme des carrées des n premiers entiers impairs.
import math
n=int(input("Veuillez entrer un entier : "))
s=0
j=1
for i in range(1,n+1):
        s=s+math.pow(j,2)
        j=j+2
print(f"La somme est : {s}")