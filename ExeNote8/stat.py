#Auteur : Mohammad Taleb
#Date de creation : 16 avril 2021
import sys
#la fonction readFile prend un seul parametre (path) qui represente un fichier
#et retourne l'ouverture de fichier en mode lecture
def readFile(path):
    return open(path, 'rb').read().decode('utf-8')

#la fonction decouperEnLignes permet de decouper un texte en un tableau 
#prend un seul (contenu) parametre qui represente un texte et retourne un tableau
def decouperEnLignes(contenu):
    lignes = contenu.split('\n') #enleve les nouveau ligne
    if lignes[-1] == '': #si le dernier caractere est egale a un espace
        lignes.pop() #enlever le dernier caractere   
    return lignes

#la fonction lireTxt premet de creer une liste et prend un seul parametre (path) 
#represente un fichier.txt et retourne une liste 
def lireTxt(path):
    lignes = decouperEnLignes(readFile(path)) #appel a la fonction decouperEnLignes
    liste= list(map(lambda ligne: ligne.split(), lignes)) #transformer la chaine de caractere en liste
    return liste

#la fonction ecrireTxt permet de creer un nouveau fichier.txt prend un seul parametre(path)
#qui represente un fichier.txt et retourne un nouveau fichier.txt      
def ecrireTxt(path):
    contenu = open('stat.txt',"wb") #ouvrire un nouveau fichier.txt
    tabMoyenne = moyenne(lireTxt(path)) #appelle de la fonction moyenne 
    texte = ('La taille moyenne des individus fumeurs du sexe masculin : ' + 
            str(tabMoyenne[0]) + '\n')
    texte1 = ('La taille moyenne des individus non-fumeurs du sexe masculin : ' + 
            str(tabMoyenne[1]))
    contenu.write(texte.encode('utf-8')) #ecrire texte dans le nouveau fichier.txt
    contenu.write(texte1.encode('utf-8')) #ecrire texte1 dans le nouveau fichier.txt
    contenu.close() #fermer le fichier.txt
    
#la fonction moyenne calcule la moyenne des gens fumeurs et non fumeurs de sexe masculin
#et prend un seul parametre (tab) qui representer un tableau et retourne
#un nouveau tableau, avec les deux moyennes comme element de nouveau tableau 
def moyenne(tab):
    tabMoyenne=[] #creation d'un tableau
    nbFumeurs = 0 #nombre de fumeurs
    nbNonFumeurs = 0 #nombre de non fumeurs
    taille = 0 #taille des fumeurs
    taille1 = 0 #taille des non fumeurs
    for i in range (len(tab)): #pour i dans l'intervalle du longueur de tab
        if tab[i][3] == '1': #si l'element [i][3] de tab egale str(1) , un masculin
            if tab[i][4]=='1': #si l'element [i][4] de tab egale str(1) , un fumeur
                nbFumeurs +=1 #ajouter 1 a nbFumeurs
                taille += float(tab[i][2]) #ajoute float de l'element de tab a taille                  
            elif tab[i][4] == '0': #si l'element [i][3] de tab egale str(0) , non fumeur
                nbNonFumeurs +=1 #ajouter 1 a nbNonFumeurs
                taille1 += float(tab[i][2]) #ajoute float de l'element de tab a taille1
    if nbFumeurs !=0 : #si nbFumeurs est different que 0     
        moyenneFumeurs = taille/nbFumeurs #moyenne des fumeurs
    else : #sinon
        moyenneFumeurs = 0 #moyenne des fumeurs 
    if nbNonFumeurs != 0 : #si nbNonFumeurs est different que 0        
        moyenneNonFumeurs = taille1/nbNonFumeurs #moyenne des non fumeurs
    else : #sinon
        moyenneNonFumeurs = 0 #moyenne des non fumeurs
    tabMoyenne.append(moyenneFumeurs) #ajouter a la fin de tab moyenneFumeurs
    tabMoyenne.append(moyenneNonFumeurs) #ajouter a la fin de tab moyenneNonFumeurs           
    return tabMoyenne

def moyenneText(): #text-unitaire
    assert moyenne([['11','3','60','1','0'],['12','4','70','1','1']]) == [70,60]
    assert moyenne([['12','4','50','1','1'],['12','4','60','1','1']]) == [55,0]
    assert moyenne([['12','4','50','0','1'],['12','4','60','0','1']]) == [0,0] 
    assert moyenne([['12','4','50','1','1'],['12','4','86','1','0'],
                   ['12','4','90','1','1'],['12','4','60','1','0']]) == [70,73]
    assert moyenne([['11','3','60','1','0'],['12','4','70','0','1']]) == [0,60]  

moyenneText()
ecrireTxt(sys.argv[1])             