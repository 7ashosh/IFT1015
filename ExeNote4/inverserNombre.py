#Auteur: mohammad taleb
#Date: 16 Fev 2021
#
#la fonction de ce programme calcule l'inverse d'un entier positive
#prend un seul parametre qui n un entier positive
#retourne l inverse de n en un entier positive 
#le nom de la fonction est inverser
def inverser (n):
    nbInverser = "0"
    while n>0: # tant-que n>0         
            restant = n % 10 # le restant de la division de n par 10
            n = n // 10 # le quotient de la division de n par 10               
            nbInverser = nbInverser + str(restant) # nombre inverser
    return int(nbInverser) # return un nombre entier
def inverserTest(): # test unitaire
    assert inverser(0) == 0
    assert inverser(10) == 1
    assert inverser(121) == 121
    assert inverser(7631) == 1367
    assert inverser(7) == 7
      
inverserTest() 