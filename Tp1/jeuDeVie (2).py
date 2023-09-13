#Auteur : Mohammad taleb , Nehmat Haidar Ahmad , Jad Haidar Ahmad
#Date de creation : 26 Mars 2021
#
#ce programme cree une jeu appelle jeu de la vie à “0 joueur”, d’une grille 
#à deux dimensions dont les cases représentent des cellules qui peuvent 
#prendre deux états distincts : « vivante » ou « mortes ». Une cellule 
#possède huit voisins, qui sont les cellules adjacentes horizontalement, 
#verticalement et diagonalement et dont l’état change au fil du temps suivant 
#des règles prédéfinies.
##################
##################
#la fonction creerGrille crée un modèle de la grille de jeu et prend un seul 
#parametre (tailleGrille) qui est enrigistrement possedant 3 champs 
#nx,ny,larguer) et crée un modèle de la grille de jeu et retourne 
#un tableau 2D

def creerGrille(tailleGrille):
    nx=tailleGrille.nx #nombre de ligne
    ny=tailleGrille.ny #nombre de colonne
    largeur=tailleGrille.largeur #largeur de case
    tab=[0]*nx #creation de tableau
    nombre=0 #nombre de case
    for i in range(len(tab)): #pour i dans l'intervalle (0,len(tab))
        tab[i]=[i]*ny #
    for i in range(len(tab)): #pour i dans l'intervalle (0,len(tab))
        for j in range(len(tab[i])): #pour i dans l'intervalle (0,len(tab[i]))
            tab[i][j]=nombre #l'element [i][j] du tableau egale au nombre
            nombre+=1 #ajouter 1 a nombre de case
    return tab

#la procedure init permet de derterminer de nombre de cellule vivant et 
#de creer le modele a l'etat initial et prend un seul parametre (grille) 
#qui est un tableau

def init(grille):
    
    nx=len(grille) #nombre de ligne
    ny=len(grille[0]) #nombre de colonne
    nbCase=0 #nombre de case
    for i in range(len(grille)): #pour i dans l'intervalle (0,(len(gille))
        for j in range(len(grille[i])): #pour j dans l'intervalle (0,(len(gille))
            nbCase+=1 #ajouter 1 au nbCase
            
    while True: #tant-que c'est vrai
        rand = random()+0.1 
        if rand <=0.2: #si rand <= 0.5
            break
    nbCellVivant = round(rand*nbCase)
    while nbCellVivant>0: #tant-que nbCellVivant > 0
        ligne=math.floor(random()*nx) 
        colonne=math.floor(random()*ny) 
        if grille[ligne][colonne]!= 'cellVivant':
            grille[ligne][colonne] = 'cellVivant'
            nbCellVivant -=1 #soustrere 1 au nbCellVivant

#la procedure bordureGrille dessine la bordure du jeu et prend un seul
#parametre (tailleGrille) qui represente un enrigistrement avec trois 
#champs (nx,ny,largeur)
                        
def bordureGrille(tailleGrille):
    nx=tailleGrille.nx #nombre de ligne
    ny=tailleGrille.ny #nombre de colonne
    largeur=tailleGrille.largeur #largeur de case
    pu() #arreter de laisser un trait
    pencolor(0,0,0) #change le couleur a noir
    pensize(1) #changer le largeur de tracer
    bk(nx*largeur) #reculer d'une distance nx*largeur
    lt(90) #pivoter a gauche d'un angle 90 degres
    bk(largeur/2) #reculer d'une distance largeur/2
    fd(ny*largeur) #avancer d'une distance ny*largeur
    rt(90) #pivoter a droite d'un angle 90 degres
    pd() #commencer de laisser un trait
    for i in range (nx): #pour i dans l'intervalle (0,nx)
        for j in range (ny): #pour j dans l'intervalle (0,ny)
            for k in range (4): #pour k dans l'intervalle (0,4)
                fd(largeur) #avancer de distance largeur
                rt(90) #pivoter a droite de 90 degres
            fd(largeur) #avancer de distance largeur
        pu() #arreter de laisser un trait
        bk(nx*largeur) #reculer d'une distance nx*largeur
        rt(90) #pivoter a droite d'un angle de 90 degres
        fd(largeur) #avancer d'une distance largeur
        lt(90) #pivoter a gauche d'un angle de 90 degres
        pd() #commencer a laisser un trait
                        
#la procedure dessinerGrille prend 2 paramètres (tailleGrille) represente
#un enrigistrement et (grille) reprensente un tableau, et affiche l’état 
#du jeu , et qui choisie le couleur rouge pour les cellules vivantes
#et blanc pour les cellules morts
            
def dessinerGrille(tailleGrille,grille):
    nx=tailleGrille.nx #nombre de ligne
    ny=tailleGrille.ny #nombre de colonne
    largeur=tailleGrille.largeur #largeur de case
    pu() #arreter de dessiner
    bk((nx*largeur)/2) #reculer d'un distance (nx*largeur)/2
    lt(90) #rotation a gauche de 90 degres
    fd((ny*largeur)/2) #avancer d'un distance (ny*largeur)/2
    bk(largeur/2) #reculer d,un distance largeur/2
    rt(90) #rotation a droite de 90 degres
    ht() #enlever la tortue
    pd() #commencer a laisse un trait
    creerGrille(tailleGrille) #appeler la fonction creerGrille
    pensize(largeur) #changer la largeur de trace
    pencolor(1,0,0) #changer la couleur de trace
    for i in range(len(grille)): #pour i dans l'intervalle (0,len(grille))
        if i !=0 : #si i != 0
            pu() #arreter de laiser un trait
            rt(90) #pivoter a droite d'un angle de 90 degres
            fd(largeur) #avancer d'une distance largeur
            rt(90) #pivoter a droitr d'un angle de 90 degres
            fd(nx*largeur) #avancer d'une distance de nx*largeur 
            lt(180) #pivoter d'un angle de 180 degres
            pd() #commencer a laisser un trait
        #pour j dans l'intervalle(0,len(grille[i]))
        for j in range(len(grille[i])): 
            if grille[i][j] == 'cellVivant': #si grille[i][j] == 'cellVivant'
                fd(largeur) #avancer d'une distance largeur  
            else : #si non
                pu() #arreter de laisser un trait
                fd(largeur) #avancer d'une distance largeur
                pd() #commencer de laisser un trait
    bordureGrille(tailleGrille) #appeler la procedure bordureGrille  
    
#la fonction nbCellVoisins determine le nombre de cellule vivant autour
#de chaque cellule et prend trois parametre

def nbCellVoisins(nx,ny,grille):
    nbVoisins=0 #nombre de voisins d'une cellule
    if ny<len(grille): #si ny plus petit que la longueur de la grille
        if nx==0 and ny!=0: #si nx egale a 0 et ny different que 0
            #si l'element [nx-1][ny-1] egale a 'cellVivant'
            if grille[nx+1][ny-1] == 'cellVivant': 
                nbVoisins +=1 #ajouter 1 au nbVoisins
    if nx+1<len(grille): #si nx+1<len(grille)
        if nx==0: # si nx==0
            if grille[nx+1][ny] == 'cellVivant': #si grille[nx+1][ny] == 'cellVivant'
                nbVoisins += 1 #ajouter 1 au nbVoisins
        else: #si no
            if ny!=0:
                if grille[nx+1][ny-1] == 'cellVivant':
                    nbVoisins += 1
            if grille[nx+1][ny] == 'cellVivant':
                nbVoisins += 1
    if ny-1<len(grille[nx]):
        if nx!=0:
            if grille[nx-1][ny] == 'cellVivant':
                nbVoisins += 1
        if nx!=0 and ny!=0:
            if grille[nx-1][ny-1] == 'cellVivant':
                nbVoisins += 1
    if ny+1<len(grille[nx]):
        if nx!=0:
            if grille[nx-1][ny+1] == 'cellVivant':
                nbVoisins +=1
        if grille[nx][ny+1] == 'cellVivant':
                nbVoisins+=1
    if (ny+1 <len(grille[nx]))and (nx+1<(len(grille[nx]))):
        if grille[nx+1][ny+1] == 'cellVivant':
            nbVoisins+=1
    if ny-1<len(grille[nx]):
        if ny!=0:
            if grille[nx][ny-1] == 'cellVivant':
                nbVoisins+=1
    return nbVoisins
def nbCellVoisinsTest(): #test unitaire
    assert nbCellVoisins(31,[[0,0,0],[0,0,0],[0,0,0]])==0
    assert nbCellVoisins(1,1,[[0,0,0],['cellVivant',0,0]]) == 1
    assert nbCellVoisins(1,2,[[0,0,0],['cellVivant',0,0]]) == 0
    assert nbCellVoisins(1,1,[[0,0,0],['cellVivant',0,'cellVivant']]) == 2
    assert nbCellVoisins(1,0,[[1,0,4],[0,0,5]]) == 0

def changementCellulaire(nx,ny,grille):
    tabFuture=[0]*nx
    for i in range (len(tabFuture)):
        tabFuture[i]=[i]*ny
    for i in range(len(tabFuture)):
        for j in range (len(tabFuture[i])):
            nbVoisins = nbCellVoisins(i,j,grille)
            if grille[i][j] == 'cellVivant':
                if nbVoisins<2:
                    tabFuture[i][j]='cellMort'
                if nbVoisins==2 or nbVoisins==3:
                    tabFuture[i][j]='cellVivant'
                if nbVoisins>3:
                    tabFuture[i][j]='cellMort'                    
            if grille[i][j] !='cellVivant':
                if nbVoisins==3:
                    tabFuture[i][j]='cellVivant'
                elif nbVoisins!=3:
                    tabFuture[i][j]='cellMort'
                             
    return tabFuture    
def changementCellulaireTest():
    assert changementCellulaire([1,])
            
def jouerGrille(tailleGrille):
    grille=creerGrille(tailleGrille)
    init(grille)
    while True:
        clear() 
        dessinerGrille(tailleGrille,grille)
        grille=changementCellulaire(tailleGrille.nx,tailleGrille.ny,grille)        
        sleep(0.1)
       
jouerGrille(struct(nx=20,ny=20,largeur=10))                    
                    
    
      
         