#auteur: Mohammad Taleb
#date:27 FEV 2021
#
#
#la procedure spiraleTournante prend quantre parametre dont trois entier
#positive et une entier negative. Elle retoune le dessin d'une spirale
#tournante.
def spiraleTournante(base, taille, nbFormes, vAng): 
    rotation = 0 
    while True: #tant-que c'est vrai
    #effacer le dessin        
        if vAng >= 0: #si l'angle est plus grand que zero
            rt(rotation) #pivoter vers le droite d'un angle (rotation) degres
            rotation += vAng #ajouter vAng a rotation
        else: #sinon
            lt(rotation) #pivoter vers le gauche d'un angle (rotation) degres 
            rotation -= vAng #soustraire vAng a rotation 
        spirale(base,taille,nbFormes) #appeler la procedure spirale    
        ht() #enlever la tortue 
        sleep(0.01) #suspendre pour 0.01 seconde 
        clear()
        
#la procedure spirale prend trois parametre (base,taille,nFormes)
#des entiers positives. Elle retourne le dessin d'une spirale 

def spirale(base,taille,nbFormes):
    for i in range (nbFormes): #pour i dans l'intervalle [nb,Formes)  
        for _ in range (2):
            pu() #cesser de laisser un trait
            fd(100) #avancer d'une distance 100 pixels
            pd() #commencer a laisser un trait
            ligne(base,taille,i+1) #appeler la procedure ligne
            lt(90) #pivoter a gauche d'un angle 90 degres 
            
#la procedure ligne prend trois parametre (base,taille,n)
#des entiers pisitives. Elle retourne le dessin d'une ligne.

def ligne(base,taille,n):
    pu() #cesser de laisser un trait
    bk(100) #reculer d'une distance 100 pixels
    pd() #commencer a laisser un trait
    for k in range(n):
        triangle(base) #appeler la procedure triangle
        pu() #cesser de laisser un trait 
        fd(taille/2) #avancer d'une distance (taille/2) pixels
        pd() #commencer a laisser un trait
        carre(taille) #appeler la procedure carre    

#la procedure triangle prend un seul parametre (base) qui est
#un entier positive. Elle retourne le dessin d'un triangle isocele.
        
def triangle(base):
    for j in range(1,(base//2)+1): #pour j dans l'intervalle [1,(base//2)+1)
        pensize(j*2) #trait de largeur j*2
        fd(1) #avancer d'une distance 1 pixels

#la procedure carre prend un seul parametre (taille) qui est 
#un entier positive. Elle returne le dessin d'une carre.        

def carre(taille):
    pu() #cesser de laisser un trait 
    bk(taille/2) #reculer d'une distance (taille/2) pixels
    pd() #commencer a laisser un trait
    pensize(taille) #trait de largeur (taille)    
    fd(taille) #avancer d'une distance (taille) pixels
    
    
#carre(100)  
#triangle(100)
#ligne(20,10,5)
#spirale(10,10,10)
spiraleTournante(15,10,10,2)