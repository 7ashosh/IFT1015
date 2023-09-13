#Auteur : Mohammad Taleb
#Date de creation : 2 avril 2021
####
####
#la fonction nbJour prend un seul parametre (jour) qui represente
#un entier positive compris entre 01 et 31 et retourne un string 
#d'entier positive compris entre 01 et 31
####
def nbJour(jour):
    tab=[] #creation un tableau vide
    if type(jour) == int: #si le type de jour est un int
        if jour <=31 and jour > 0 : #si jour entre 0 et 31
            for i in range (1,(jour)+1): #pour i dans l'intervalle (1,jour+1)
                if i < 10: #si i est plus petit que 10
                    tab.append('0'+str(i)) #ajouter a la fin de tab'0'et str i
                else: #sinon
                    tab.append(str(i)) #ajouter a la fin de tab le string de i
            return tab[jour-1]    
        else: #sinon
            return '' 
    else: #sinon
        return ''

def nbJourTest(): #test unitaire
    assert nbJour(0) == ''
    assert nbJour(20) == '20'
    assert nbJour(31) == '31'
    assert nbJour(5) == '05'
    assert nbJour('b') == ''

####    
#la fonction nbMois prend trois parametre (mois) qui reprensente un string 
#et (jour) qui represente un string d'entier positive entre
#01 et 31 et (annee) qui reprentre un entier positive et la fonction retourne 
#deux string (newmois,jour)  
def nbMois(mois,jour,annee): 
    tabMois = ['janvier','fevrier','mars','avril','mai','juin','juillet',
              'aout','septembre','octobre','novembre','decembre']
    
    tab = ['01','02','03','04','05','06','07','08','09','10','11','12']
    
    if mois in tabMois: #si mois est dans tabMois
        for i in range(len(tabMois)): #pour i dans l'intervalle len(tabMois) 
            if mois == tabMois[i]: #si mois egale tabMois[i]
                newMois=tab[i] #newMois egale tab[i]
                break
    elif mois in tab: #sinon, si mois dans tab 
        newMois=tabMois[int(mois)-1] #newMois egale tabMois[int(mois)-1]
    else: #sinon
        return '' 
    if newMois=='fevrier': #si newMois egale 'fevrier'
        if int(annee)%4==0: #si l'annee est bissextiles
            if int(jour)<=29 : #si l'entier jour est plus petit ou egale a 29
                return newMois,str(int(jour)) 
        elif int(annee)%4!=0: #sinon, si l'annee n'est pas bissextiles
            if int(jour)<=28: #si l'entier jour est plus petit ou egale a 28
                return newMois,str(int(jour)) 
        else: #sinon
             return ('','')
    
    elif newMois == '02': #si newMois egale '02'
        if int(annee)%4==0: #si l'annee est bissextiles
            if int(jour)<=29 : #si l'entier jour est plus petit ou egale a 29
                return newMois,jour
        elif int(annee)%4!=0: #sinon, si l'annee n'est pas bissextiles
            if int(jour)<=28: #si l'entier jour est plus petit ou egale a 28
                return newMois,jour
        else: #sinon
             return ('','')
    
    if newMois in tabMois and newMois!='fevrier': #si newMois dans tabMois
        for i in range (len(tabMois)): #pour i dans l'intervalle len(tabMois) 
                if int(jour) <= 30: #si l'entier jour plus petit ou egale 30
                        return newMois,str(int(jour))                
                elif int(jour) == 31: #sinon, si l'entier jour egale a 31
                    if i<=6 and i%2==0: #si i plus petit ou egale 6 et paire
                        return newMois,str(int(jour))               
                    else: #sinon       
                        return newMois,str(int(jour))
                                       
    elif newMois in tab and newMois!='02': #si newMois dans tab et pas '02'
        for i in range (len(tab)): #pour i dans l'intervalle len(tab)
                if int(jour)<=30: #si l'entier jour plus petit ou egal 30
                    return newMois,jour
                elif int(jour) == 31: #sinon, si l'entier jour egale a 31  
                    if i<=6 and i%2==0: #si i plus petit ou egal 6 et paire
                        return newMois,jour
                    else: #sinon
                        return newMois,jour
            
    else: #sinon
        return ('','')

def nbMoisTest(): #test unitaire
    assert nbMois('novembre','30','2000') == ('11','30')
    assert nbMois('','','29') == '',''
    assert nbMois('02','29','2000') == ('fevrier','29')
    assert nbMois('0','24','1900') == '',''
    assert nbMois('8','0','200') == '',''

####    
#la fonction nbAnnee prend un seul parametre (annee) qui represente
#un entier positive different que zero et doit retourner un entier
#positive different que zero
####
def nbAnnee(annee):
    if type(annee) == int: #si annee est un entier
        if annee >0: #si l'entier de l'annee est plus grand que 0 
            return annee
        else : #sinon
            return ''
    else: #sinon
        return ''

def nbAnneeTest(): #test unitaire
    assert nbAnnee(0) == ''
    assert nbAnnee(2000) == 2000
    assert nbAnnee(-654) == ''
    assert nbAnnee('') == ''
    assert nbAnnee('U') == ''

####
#la fonction convDate lit une date d’une forme et la convertit en un autre. 
#La fonction prend comme paramètre un texte et si ce texte représentante 
#une date valide, la fonction retourne un texte de conversion de la même date 
#dans l’autre format
####
def convDate(texte):
    if '/' in texte: #si '/' se trouve dans le texte
        tab=texte.split('/') #decouper le texte au separateur '/' dans tab 
    else: #sinon
        tab=texte.split() #decouper le texte au separateur blanc dans tab  
    if tab[0]!='': #si l'element 0 de tab n'est pas vide    
        jour= nbJour(int(tab[0])) #appeller la fonction nbJour 
        if jour!='': #si jour n'est pas vide
            annee = nbAnnee(int(tab[2])) #appeller la fonction nbAnnee       
            if annee!='': #si annnee n'est pas vide
                mois,jours= nbMois(tab[1],jour,annee) #appeller la fonction 
                if mois!='': #si mois n'est pas vide
                    tab1=[] #nouveau tableau vide
                    tab1.append(str(jours)) #ajouter a la fin de tab1 str jour
                    tab1.append(mois) #ajouter a la fin de tab1 le mois
                    tab1.append(str(annee)) #ajouter a la fin de tab1 str annee
                    if '/' in texte: #si '/' dans le texte
                        text = ' '.join(tab1) #nouveau text avec espace blanc
                                              #entre les element de tab1
                    elif '' in texte: #sinon, si espace blanc dans le texte
                            text = '/'.join(tab1) #nouveau text avec '/'
                                                  #entre les element de tab1
                    return text
                else: #sinon
                    return ''
            else: #sinon
                return ''
        else: #sinon
            return '' 
    else: #sinon
        return ''

def convDateTest(): #test unitaire
    assert convDate('2 mars 2021') == '02/03/2021'
    assert convDate('42 mars 1900') == ''
    assert convDate('29 fevrier 2019') == ''
    assert convDate('02/02/0') == ''
    assert convDate('29/02/2020')=='29 fevrier 2020'
    assert convDate('//a/') ==''
    assert convDate('  2  novembre   21  ') == '02/11/21'
    assert convDate('09/12/-2019') == ''
    assert convDate('03/04/2011') == '3 avril 2011'