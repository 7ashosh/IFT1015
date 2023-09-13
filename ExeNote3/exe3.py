#nom de fichier: exe3.py
#auteur: Mohammad Taleb
#date de creation: 7 fev 2021
#
#ce programme decrit l'approximation du nombre pi en faisons la somme
#d'un serie de nombre pour determiner le nombre de terme pour obtenir la
#premier fois 3.14... , 3.141... et 3.1415...
i=100 #puissance de 10
terme = 0 #nombre de terme 
nombre1 = 3.14 #PI a deux decimales
nombre2 = 3.141 #PI a trois decimales
nombre3 = 3.1415 #PI a quatre decimales
somme = 0 
k = 0 # nombre entier >=0
repeter = True 
while repeter : #tant-que c'est repeter
    somme = somme + 4*(-1)**k/(2*k+1) #somme += la somme d'un serie de pi
    terme = terme + 1 #terme +=1    
    if  math.floor(somme*i) == nombre1*i: #si l'entier du somme*100 = 314
            i=1000 #changer la valeur de 100 a 1000          
            nombre1 = 0 #changer la valeur a 0                      
            terme1 = terme
    if  math.floor(somme*i) == nombre2*i: #si l'entier du somme*1000 = 3141                    
            i = 10000 #changer la valeur de 1000 a 10000   
            nombre2 = 0 #changer la valeur a 0            
            terme2 = terme
    if  math.floor(somme*i) == nombre3*i: #si l'entier du somme*10000 = 31415            
            terme3 = terme
            repeter = False #la boucle est epuisee
    k = k + 1 #k +=1    

#imprimer le nombre de terme pour chaque valeur     
print("3.14... ",terme1,"termes")
print("3.141... ",terme2,"termes")
print("3.1415...",terme3,"termes")