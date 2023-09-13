#auteur: Mohammad Taleb
#date de creation:17 Mars 2021
#
#la fonction entrelacer prend en parametre deux tableaux (tab1,tab2) 
#et retourne un un tableau (tab) résultat qui combine des éléments 
#de deux tableaux entrelaçant les éléments entre eaux
def entrelacer(tab1 , tab2):
    tab=[] #nouveau tableau
    minTab=min(len(tab1),len(tab2)) #longueur minimal entre tab1 et tab2
    for i in range (minTab): #pour i dans l'intervalle (0,minTab)
        tab.append(tab1[i]) #ajouter a la fin tab1[i] a tab
        tab.append(tab2[i]) #ajouter a la fin tab2[i] a tab
    while len(tab1)>len(tab2): #tant-que long tab1 plus grand que long tab2
        tab.append(tab1[minTab]) #ajouter a la fin tab1[mintab] a tab
        minTab= minTab+1 #ajouter 1 a minTab
        if minTab==len(tab1): #si minTab egale a longueur de tab1          
            break
    while len(tab1)<len(tab2): #tant-que long tab1 plus petit que long tab2
        tab.append(tab2[minTab]) #ajoute a la fin tab2[minTab] a tab
        minTab= minTab+1 #ajouter 1 a minTab
        if minTab==len(tab2): #si minTab egale a longueur de tab2
            break
    return tab 
def entrelacerTest(): #test unitaire
    assert entrelacer([],[]) == []
    assert entrelacer([1],[]) == [1]
    assert entrelacer([],[2]) == [2]
    assert entrelacer([1],[2]) == [1,2]
    assert entrelacer([1,2,3,67,8], [2, 8]) == [1,2,2,8,3,67,8]
    assert entrelacer([-2,7,-92],[3,-5]) ==[-2,3,7,-5,-92]
    assert entrelacer(['math','info'],['stat']) == ['math','stat','info']
    
entrelacerTest()    