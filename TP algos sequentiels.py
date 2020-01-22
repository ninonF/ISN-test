##################################
### TP Algorithmes séquentiels ###
##################################

"""
Dans ce TP, on revient sur un certain nombre d'algorithmes dits séquentiels
qui ont été vus dans les exercices de France IOI.

On demande ici d'implémenter les fonctions données.

On s'assurera des petits tests que ces fonctions fonctionnent. Pas besoin de
générer des tests automatisés ici.

Rappels : si t est un tableau 
    + len(t) renvoie sa taille
    + t[4] renvoie le 5eme élément du tableau
    + les éléments de t sont numérotés de 0 à n-1 où n est la taille de t

A rendre pour mardi 20/01 :
    + ce fichier complété avec les traces de vos tests (antoine.becquet@ac-lyon.fr)
    + 1 preuve de correction et 1 complexité de recherche, minimum et somme, sur copie ou en pdf
    + faisable par groupe de 2 max
"""


#################
### FONCTIONS ###
#################

def recherche(t,x):
#Renvoie True si x est dans t et False sinon
    present = False
    for i in t:
        if i==x:
            present = True
    return present


def minimum(t):
    #Renvoie le plus petit élément de t
    x = t[0]
    for i in t:
        if x>i:
            x=i
    return x

def maximum(t):
    #Renvoie le plus grand élément de t
    x = t[0] 
    for i in t:
        if x<i:
            x=i
    return x

def somme(t):
    #Renvoie la somme des éléments de t
    x = 0
    for i in t:
        x+=i
    return x


def moyenne(t):
    #Renvoie la moyenne des éléments de t 
    l=len(t)
    x=0
    for i in t:
        x+=i
    return x/l



#########################
### ESPACE DE LIBERTE ###
#########################

#Testez vos fonctions !

#RECHERCHE
"""
from random import randint
for j in range(10):
    t=[]
    for i in range(10):
        t.append(randint(-150,150))
    x = randint(-100,100)
    t.sort()
    if recherche(t,x):
        print(x,"est dans",t)
    else:
       print(x,"n'est pas dans",t)
"""

#MINIMUM
"""
from random import randint
for j in range(10):
    t=[]
    for i in range(10):
        t.append(randint(-150,150))
    t.sort() 
    print("le minimum de t est",minimum(t))
"""

#MAXIMUM
"""
from random import randint
for j in range(10):
    t=[]
    for i in range(10):
        t.append(randint(-150,150))
    t.sort()
    print("le maximum de", t ,"est",maximum(t))
"""


#SOMME
"""
from random import randint
for j in range(10):
    t=[]
    for i in range(3):
        t.append(randint(-150,150))
    t.sort()
    print("la somme de", t,"est",somme(t))
"""

#MOYENNE
"""
from random import randint
for j in range(10):
    t=[]
    for i in range(2):
        t.append(randint(-150,150))
    t.sort()
    print("la moyenne de", t,"est",moyenne(t))
"""



#PREUVES DES ALGORITHMES
#Recherche
"""

"""
#Minimum
"""
P : x est le minimum dans [t[0] ,..., t[i-1]].

Supposons que P est vrai à l'entrée de la boucle i, dans ce cas x est le minimum dans [t[0] ,..., t[i-1]]

Si t[i] est plus grand que x , x est toujours le minimum de [t[0], t[i]] est n'est pas changé par la boucle.
Sinon t[i] est le minimum de [t[0],...,t[i]] , x prends la valeur de t[i] donc x est toujours le minimum de [t[0] ,..., t[i]].

P sera donc toujours vrai à la fin de la boucle i.
"""
#Maximum
"""
P : x est le maximum dans [t[0] ,..., t[i-1]].

Supposons que P est vrai à lentrée de la boucle i, dans ce cas x est le maximum dans [t[0] ,..., t[i-1]]

Si t[i] est plus petit que x , x est toujours le maximum de [t[0], t[i]] n'est pas changé par la boucle.
Sinon t[i] est le maximum de [t[0],...,t[i]] , x prends la valeur de t[i] donc x est toujours le maximum de [t[0] ,..., t[i]].

P sera donc toujours vrai à la fin de la boucle i.
"""
#Somme
"""

"""
#Moyenne
"""

"""
#COMPLEXITE DES ALGORITHMES
#Recherche
"""
la boucle A effectue 0 opération arithmétiques,1 affectations,1 tests,0 opération booléenne et une affectation en dehors de la boucle. Donc,
dans le pire des cas, nous avons (2n) fois pour un total de (2n)+1= 2n+1 opération elementaire.
le programe de recherche est donc linéaire de complexité O(n)

"""
#Minimum
"""
la boucle A effectue 0 opération arithmétiques,1 affectations,1 tests,0 opération booléenne et une affectation en dehors de la boucle. Donc,
dans le pire des cas, nous avons (2n) fois pour un total de (2n)+1= 2n+1 opération elementaire.
le programe de recherche est donc linéaire de complexité O(n)

"""
#Maximum
"""
la boucle A effectue 0 opération arithmétiques,1 affectations,1 tests,0 opération booléenne et une affectation en dehors de la boucle. Donc,
dans le pire des cas, nous avons (2n) fois pour un total de (2n)+1= 2n+1 opération elementaire.
le programe de recherche est donc linéaire de complexité O(n)

"""
