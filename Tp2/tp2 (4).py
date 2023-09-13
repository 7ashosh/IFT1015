#####
#ce programmeimplante un jeu qui s’exécute dans l'environnement du
#navigateur web. Ce jeu consiste à trouver les nombres associés à cinq 
#symboles remplissant une grille 5 par 5 qui permettent de donner comme 
#sommes les valeurs affichées au bout de chacune des rangées et de chacune 
#des colonnes. Le joueur gagne lorsque la bonne combinaison de 5 nombres est 
#retrouvée. Si les assignations partielles aux symboles ne peuvent pas former 
#les sommes demandées, le joueur perd.
#####
import functools

nombre=''

# Dimension de la surface de jeu
colonne = 6
ligne= 6

# Grille contenant des chiffre de 0 jusqu'a 35
grille = list(range(36)) 

# Grille qui contient tout les images
grilleSym=["symboles/circle.svg","symboles/pyramide.svg","symboles/penta.svg",
           "symboles/star.svg","symboles/cube.svg"]*(ligne-1)
symbole=["symboles/circle.svg","symboles/pyramide.svg","symboles/penta.svg",
         "symboles/star.svg","symboles/cube.svg"]

# Le style HTML de la surface de jeu.
styleHTML="""<style>
              #jeu table { float: none; }
              #jeu table td {
                  border: 1px solid black;
                  padding: 1px 2px;
                  width: 80px;    
                  height: 80px;
                  font-family: Helvetica;
                  font-size: 20px;
                  text-align: center;
              }
              #jeu table td img {
                  display: block;
                  margin-left: auto;
                  margin-right: auto;
                  object-fit: contain;
                  width: 80%;
                  height: 80%;
              }
              #jeu h1 {
                  colonneor: crimson;
              }
              .container {
                  position: relative;
                  text.align: centre;
              }
              .centered {
                  position: absolute;
                  top: 50%;
                  left: 50%;
                  transform: translate(-50%, -50%);
              }
              msg {color: red;}
              .h1 {
                   margin-left: 40px;       
              }    
             </style>"""

# La fonction tableHTML en parametre un texte et
# retourne la balise table en string
def tableHTML(contenu):
    return '<table>' + contenu + '</table>'

# La fonction trHTML prend en parametre un texte et retourne une balise tr 
#en string 
def trHTML(contenu):   
    return '<tr>' + contenu + '</tr>'

# La fonction tdHTML prend deux textes en parametre et retourne le
# texte HTML correspondant a une balise "td" .
def tdHTML(attrs, contenu):
    return "<td" + attrs + ">" + contenu + '</td>'

# La fonction imgHTML prend un texte en parametre et retourne la balise img 
#en string 
def imgHTML(src):
    return '<img src="' + src + '"alt="Snow" style="width:100%;">'

# La fonction cont prend deux parametre qui represente un texte
# et un entier positive et retourne un classe container
def cont(contenue,nombre):   
    return'<div class="container">'+(contenue
                                    )+'<div class="centered">'+(nombre
                                                               )+'</div></div>'

# La foction accoupler prend en parametre un tableau et l'aire du tableau et 
#retourne un tableau
def accoupler(tab, aire):
    couple = []
    case = []
    for element in tab:
        case.append(element)
        if len(case) == aire:
            couple.append(case)
            case = []
   
    return couple

# La fonction trHTMLJoin prend en parametre un tableau et retourne un tbaleu 
#la balise tr
def trHTMLJoin(tab):
    return trHTML(''.join(tab))

# La fonction tableHTMLJoin prend en parametre un tableau et retourne la 
#balise table
def tableHTMLJoin(tab):
    return tableHTML(''.join(tab))

# La fonction grilleTableHTML prend en parametre un tableau de string et 
#l'aire du tableau et retourne un tableau qui contient les elements 
#du table HTML
def grilleATableHTML(tab, aire):   
    return tableHTMLJoin(list(map(trHTMLJoin, accoupler(tab, aire)[::-1])))
   
# La fonction caseHTML prend en parametre un entier positive index et retourne
# un tableau qui contient le contenu du balise td du HTML
def caseHTML(index):
    contenu=''
    #si l'index egale a 5
    if index == 5:
        conteu = ''
    #si, sinon le restant de la division egale a (ligne-1)    
    elif index%ligne == (ligne-1) :
        contenu = str(table[index])
    #si, sinon la quotient de la division egale a 0
    elif index//colonne == 0 :
        contenu = str(table[index])
    #sinon
    else:    
        contenu = cont(imgHTML(grilleSym[table[index]]),nombre)       
    
    return tdHTML(' id="case' + str(index) +
                  '" onclick="clic(' + str(index) + ')"',
                 contenu)

# La fonction HTML retourne un tableau qui contient tout les balise td
def HTML():
    return grilleATableHTML(list(map(caseHTML, list(range((colonne)*(ligne))))
                                ), colonne)

# La fonction brHTML prend en parametre le un string et retourne la balise br
def brHTML(contenu):
    return '<br>'+contenu+'</br>'

# La fonction jeu prend en parametre un text HTML et retoure l'identifiant 
#jeu en string
def jeu(contenu):
    return '<div id="jeu">'+contenu+'</div>'

# La fonction buttonHTML prend en parametre un texte de HTML et un tableau
# et retourne la balise button 
def buttonHTML(contenu,tab):    
    return '<button onclick='+tab+' >'+contenu+'</button>'

#la fonction classMsg prend en parametre une string et retourne une class 
#HTML h1
def classMsg(contenu):
    return '<div class="h1">'+contenu+'</div> '

# La fonction string ne prend rien en parametre et retourne une string
def string():    
    msg='<h1><msg>' "Jouer!"'</msg></h1>'   
    return classMsg(msg)
        
# La fonction associerNombre prend en parametre un tableau d'entier et 
#retourne un tableau  
def assosierNombre(tab):
    global tabSymbNumb
    #copy le tab
    tabSymbNumb=tab.copy()
    #nouveau tableau de longeuer (ligne-1)
    tabNum=[0]*(ligne-1)
    i=0
    #tant-que i plus petit que longeuer de tab 
    while i<len(tab):
        #l'element de tabNum egale a l'entier choisis aleatoire entre 1 et 20       
        tabNum[i]=math.floor((random()*20)+1)
        #si l'element a l'index i de tabNum n'est pas dans tabSymbNumb
        if tabNum[i] not in tabSymbNumb:
            tabSymbNumb[i]=tabNum[i]
            #iteration de 1 pour i
            i+=1
        #sinon
        else: continue       
    return tabSymbNumb 

        
# La fonction melanger prend en parametre un tableau et retourne un tableau 
#(global) melanger 
def melanger(tab):
    global table
    #nouveau tableau vide
    table=[]
    i=0
    #tant-que i est plus petit ou egale au longeuer de tab -1
    while i<=len(tab)-1:
        #un entier choisis aleatoirement multipier par le longeuer de tab
        nombre =(math.floor(random()*len(tab)))
        #ajouter a la fin de table un nombre
        table.append(nombre)
        #iteration de 1 pour i
        i=i+1       
    
    return table

# La fonction sommeLigne permet d'addition les entier associer a chaque 
#symbole dans le meme ligne et ne prend pas de parametre et retourne un 
#table qui contient les sommes de chaque ligne.
def sommeLigne():
    global somme
    #tableau de longeuer (ligne-1)
    somme=[0]*(ligne-1)
    j=0
    #pour i dans l'intervalle [0,longeuer de table]
    for i in range (len(table)):
        #si l'element de grilleSym a l'index table[i] est un circle
        if grilleSym[table[i]]=="symboles/circle.svg":
            #iteration de tabSymNum[0] pour somme[j]
            somme[j]+=tabSymbNumb[0]
        #si, sinon l'element de grilleSym a l'index table[i] est un pyramide
        elif grilleSym[table[i]]=="symboles/pyramide.svg":
            #iteration de tabSymNum[1] pour somme[j]
            somme[j]+=tabSymbNumb[1]
        #si, sinon l'element de grilleSym a l'index table[i] est un penta
        elif grilleSym[table[i]]=="symboles/penta.svg":
            #iteration de tabSymNum[2] pour somme[j]
            somme[j]+=tabSymbNumb[2]
        #si, sinon l'element de grilleSym a l'index table[i] est un star
        elif grilleSym[table[i]]=="symboles/star.svg":
            #iteration de tabSymNum[3] pour somme[j]
            somme[j]+=tabSymbNumb[3]
        #si, sinon l'element de grilleSym a l'index table[i] est un cube
        elif grilleSym[table[i]]=="symboles/cube.svg":
            #iteration de tabSymNum[4] pour somme[j]
            somme[j]+=tabSymbNumb[4]    
        #si i egale a 4 ou 9 ou 14 ou 19
        if i==4 or i==9 or i==14 or i==19 :
            #iteration de 1 pour j
            j=j+1             
    
    return somme

# La fonction sommeColonne permet d'addition les entier associer a chaque 
#symbole dans le meme colonne et ne prend pas de parametre et retourne un 
#table qui contient les sommes de chaque colonne.
def sommeColonne():
    global somme1
    #tableau de longeuer (colonne-1)
    somme1 =[0]*(colonne-1)
    j=0
    #pour k dans l'intervalle [0,colonne-1]
    for k in range (colonne-1):
        #pour i dans l'intervalle [0,longeuer de table]
        for i in range (len(table)):
            #si le restant de la division i/(colonne-1) egale a k
            if i%(colonne-1)==k:
                #si l'element de grilleSym a l'index table[i] est circle
                if grilleSym[table[i]]=="symboles/circle.svg":
                    #iteration de tabSymNum[0] pour somme1[k]
                    somme1[k]+=tabSymbNumb[0]
                #si, sinon l'element de grilleSym[table[i]] est pyramide   
                elif grilleSym[table[i]]=="symboles/pyramide.svg":
                    #iteration de tabSymNum[1] pour somme1[k]
                    somme1[k]+=tabSymbNumb[1]
                #si, sinon l'element de grilleSym a l'index table[i] est penta    
                elif grilleSym[table[i]]=="symboles/penta.svg":
                    #iteration de tabSymNum[2] pour somme1[k]
                    somme1[k]+=tabSymbNumb[2]
                #si, sinon l'element de grilleSym a l'index table[i] est star    
                elif grilleSym[table[i]]=="symboles/star.svg":
                    #iteration de tabSymNum[3] pour somme1[k]
                    somme1[k]+=tabSymbNumb[3]
                #si, sinon l'element de grilleSym a l'index table[i] est cube    
                elif grilleSym[table[i]]=="symboles/cube.svg":
                    #iteration de tabSymNum[4] pour somme1[k]
                    somme1[k]+=tabSymbNumb[4]    
    
    return somme1           

# La fonction insertSomme permet d'inserer les sommes des ligne et 
#des colonnes dans un tableau et retourne un tableau qui contient les sommes 
#et les positions de chaque symbole. 
def insertSomme():
    #appeler la fonction associerNombre
    assosierNombre(symbole)
    #appeler la fonction sommeLigne 
    tab=sommeLigne()
    #appeler la fonction sommeColonne
    tab1=sommeColonne()
    #inserer l'element tab1[i] a l'index i associer dans table
    table.insert(0,str(tab1[0]))
    table.insert(1,str(tab1[1]))
    table.insert(2,str(tab1[2]))
    table.insert(3,str(tab1[3]))
    table.insert(4,str(tab1[4]))
    #inserer l'element vide a l'index 5 dans table
    table.insert(5,'')
    #inserer l'element tab[i] a l'index associer dans table
    table.insert(11,str(tab[0]))
    table.insert(17,str(tab[1]))
    table.insert(23,str(tab[2]))
    table.insert(29,str(tab[3]))
    table.insert(35,str(tab[4]))
    
    return table

# la fonction elem prend en parametre un entier positive et retourne
# DOM de la case
def elem(n):
    return document.querySelector('#case'+ str(n))

# La procedure clic permet de rentre le numero choisis par le joueur
# et le soustraire de la somme du ligne et du colonne associer
# en modifiant le tableau du jeu et indique si le joueur a gagner ou 
# a perdu, et prend un seul parametre 'case' qui represente un entier 
# positive 
def clic(case):
    global tabLigcolonne
    tabLigcolonne=[]
    #appeler la fonction imgHTML
    contenue = imgHTML(grilleSym[table[case]])
    #choisir un entier entre 1 et 20 par le joueur
    nombre = (input('veillez saisir un nombre de 1 a 20')) 
    #Donner le contenue de la case cliquer
    caseTouch=elem(case).innerHTML
    #separe caseTouch par le seperateur (")
    tdCase=caseTouch.split('"')
    #image egale a l'element a l'index 3 de tdCase
    image=tdCase[3]
    #la repetition du symbole dans un ligne
    compteLigne=0
    #la repetition du symbole dans un colonne
    compteColonne=0
    if int(nombre)<=20 and int(nombre)>0:
    #pour j dan l'intervalle du longeuer de table
      for j in range (len(table)):        
        symCase=elem(j).innerHTML.split('"')        
        #si la longeuer de symCase et tdCase sont eagaux
        if len(symCase)==len(tdCase):
            #si l'image egale a l'element a l'index 3 de symCase      
            if image==symCase[3]:
                #changer le contenue de la case
                elem(j).innerHTML=cont(contenue,nombre) 
                #iteration de 1 pour compteLigne
                compteLigne=compteLigne+1
        
        #si j est plus grand que 5            
        if j>5:
            #si l'element a l'index j de table est un string            
            if type(table[j]) is str:
                #changer l'element a l'index j en int
                var=int(table[j])
                #soustraire le nombre choisi de la somme du ligne associer
                newSom=str(var-int(nombre)*compteLigne)
                #changer l'element a l'index j par newSom
                elem(j).innerHTML=newSom
                #supprimer l'element a l'index j du table
                table.pop(j)
                #inserer la nouvelle somme dans l'index j de table
                table.insert(j,newSom)
                #reinisaliser le compteLigne a zero 
                compteLigne=0
        
        #pour k dans l'intervalle de [0,colonne-1]
        for k in range (colonne-1):
            #si la longeuer de symCase et tdCase sont eagaux
            if len(symCase)==len(tdCase):          
                #si le restant de la division de j par colonne egale a k
                if j%colonne==k:
                    #si l'image egale a l'element a l'index 3 de symCase
                    if image==symCase[3]:
                        #iteration de 1 pour compteColonne
                        compteColonne=compteColonne+1
            #si le restant de la division de j par colonne egale a k 
            #et j different que k               
            if j%colonne==k and j!=k:
                #si l'element a l'index k de table est un string              
                if type(table[k]) is str:
                    #changer l'element a l'index k en int 
                    var=int(table[k])
                    #soustraire le nombre choisi du somme du colonne associer
                    newSom=str(var-int(nombre)*compteColonne)
                    #changer l'element a l'index k par newSom
                    elem(k).innerHTML=newSom
                    #supprimer l'element a l'index k de table
                    table.pop(k)
                    #inserer la nouvelle somme dans l'index k de table
                    table.insert(k,newSom)
                    #reinisaliser le compteColonne a zero                     
                    compteColonne=0
    #nouveau tableau avec les nouveau somme
    tabLigcol=table[11:36:6]
    #ajouter les element de l'index (0:5) de table au nouveau tableau
    tabLigcol.extend(table[0:5])
    #la somme des sommes du ligne et du colonne
    som= functools.reduce(lambda x,y:int(x)+int(y),tabLigcol)
    #pour i dans l'intervalle de la longeuer de tabLigCol
    for i in range(len(tabLigcol)):       
        #si l'element a l'index i du tabLigCol est plus grand que 0
        if int(tabLigcol[i])>0:
            msg='<h1><msg>' "Jouer!"'</msg></h1>'
        #si un seule element de tabLigCol est plus petit que zero
        if int(tabLigcol[i])<0:
            msg='<h1><msg>'"Vous avez perdu."'</msg></h1>'
            break
        #si la somme egale a zero
        if som==0:          
            msg='<h1><msg>'"Vous avez gagne!"'</msg></h1>'               
            break
    
    main=document.querySelector('h1')
    main.innerHTML=msg

#La procedure init sans parametre pour initier le programme et fait 
#apparaitre le jeu
def init():
    #appeler la fonction melanger
    melanger(grilleSym)
    #appeler la fonction insertSomme
    insertSomme()
    main=document.querySelector('#main')
    main.innerHTML = brHTML(buttonHTML("nouvelle partie","init()")
                           )+string()+ styleHTML+ jeu(HTML())    

init() 
