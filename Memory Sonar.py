#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#

'''
    Lorenz Cazaubon   G1
    Paul   Mauvoisin  G1
    Jeu python: Memory
'''

##################################################################################################################

'''Importations:'''

from turtle import *
import time
import random


##################################################################################################################

'''Définition des fonctions:'''


#~~~~~~~~~~#  1) Fonction(s) en rapport avec les coordonnées:  #~~~~~~~~~~#

#Coordonnées des points rouges (cases) en fonction du nombre total de cases: (Numéro de la case, Nombre total)
def Coordonnees(num,n):

    if n==6:

        if num == 1 or num == 4:        #Exemple: points rouges 1 et 4.
            x = 370 * ((-1) ** num)
            y = 55
            
        elif num == 2 or num ==3:
            x = -130 * ((-1) ** num)
            y = 190
            
        elif num == 5 or num == 6:
            x = 80 * ((-1) ** num)
            y = -30

    elif n==8:

        if num == 1 or num == 4:
            x = 370 * ((-1) ** num)
            y = 55
            
        elif num == 2 or num ==3:
            x = -130 * ((-1) ** num)
            y = 190

        elif num == 6 or num == 7:
            x = -80 * ((-1) ** num)
            y = -30

        elif num == 5 or num == 8:
            x = 220 * ((-1) ** num)
            y = -110
    
    elif n==10:

        if num == 1 or num == 6:
            x = 510 * ((-1) ** num) 
            y = -170
        
        elif num == 2 or num == 5:
            x = -370 * ((-1) ** num)
            y = 55
            
        elif num == 3 or num == 4:
            x = 130 * ((-1) ** num)
            y = 190

        elif num == 8 or num == 9:
            x = -80 * ((-1) ** num)
            y = -30

        elif num == 7 or num == 10:
            x = 220 * ((-1) ** num)
            y = -110

    elif n==12:

        if num == 1 or num == 6:
            x = 510 * ((-1) ** num) 
            y = -170
        
        elif num == 2 or num == 5:
            x = -370 * ((-1) ** num)
            y = 55
            
        elif num == 3 or num == 4:
            x = 130 * ((-1) ** num)
            y = 190

        elif num == 7 or num == 12:
            x = 300 * ((-1) ** num)
            y = -240

        elif num == 9 or num == 10:
            x = 80 * ((-1) ** num)
            y = -30

        elif num == 8 or num == 11:
            x = -210 * ((-1) ** num)
            y = -110
    

    output = [x,y]
    return output

#Retrouve le numéro d'une case selon x, y et le nombre total de cases.
def num_case(x,y,n):
    
    delta = 20//2 + 1          #Taille d'une case divisé par 2 + 1 pixel de marge.
    
    if n==6:

        if abs(y-55) <= delta:                #On cherche à retrouver les coordonnées du centre de la case sachant que l'utilisateur peut cliquer sur toute la case, d'où |y-(+100)| <= delta
            
            if abs(x+370) <= delta:
                num = 1
            
            elif abs(x-370) <= delta:
                num = 4

        elif abs(y-190) <= delta: 
            
            if abs(x+130) <= delta:
                num = 2
            
            elif abs(x-130) <= delta:
                num =3

        elif abs(y+30) <= delta:

            if abs(x+80) <= delta:
                num = 5

            elif abs(x-80) <= delta:
                num = 6

    if n==8:

        if abs(y-55) <= delta:                
            
            if abs(x+370) <= delta:
                num = 1
            
            elif abs(x-370) <= delta:
                num = 4

        elif abs(y-190) <= delta: 
            
            if abs(x+130) <= delta:
                num = 2
            
            elif abs(x-130) <= delta:
                num =3
        
        elif abs(y+110) <= delta:

            if abs(x+220) <= delta:
                num = 5
            
            elif abs(x-220) <= delta:
                num = 8

        elif abs(y+30) <= delta:

            if abs(x+80) <= delta:
                num = 6

            elif abs(x-80) <= delta:
                num = 7

    if n==10:

        if abs(y+170) <= delta:

            if abs(x+510) <= delta:
                num = 1
            
            elif abs(x-510) <= delta:
                num = 6

        elif abs(y-55) <= delta:                
            
            if abs(x+370) <= delta:
                num = 2
            
            elif abs(x-370) <= delta:
                num = 5

        elif abs(y-190) <= delta: 
            
            if abs(x+130) <= delta:
                num = 3
            
            elif abs(x-130) <= delta:
                num = 4
        
        elif abs(y+110) <= delta:

            if abs(x+220) <= delta:
                num = 7
            
            elif abs(x-220) <= delta:
                num = 10

        elif abs(y+30) <= delta:

            if abs(x+80) <= delta:
                num = 8

            elif abs(x-80) <= delta:
                num = 9

    if n == 12:

        if abs(y+170) <= delta:

            if abs(x+510) <= delta:
                num = 1
            
            elif abs(x-510) <= delta:
                num = 6

        elif abs(y-55) <= delta:                
            
            if abs(x+370) <= delta:
                num = 2
            
            elif abs(x-370) <= delta:
                num = 5

        elif abs(y-190) <= delta: 
            
            if abs(x+130) <= delta:
                num = 3
            
            elif abs(x-130) <= delta:
                num = 4
        
        elif abs(y+240) <= delta:

            if abs(x+300) <= delta:
                num = 7
            
            elif abs(x-300) <= delta:
                num = 12
        
        elif abs(y+110) <= delta:

            if abs(x+210) <= delta:
                num = 8
            
            elif abs(x-210) <= delta:
                num = 11

        elif abs(y+30) <= delta:

            if abs(x+80) <= delta:
                num = 9

            elif abs(x-80) <= delta:
                num = 10

    return num

#Donne les coordonnées d'une vie:
def Coordonnees_vies(n):

    output = (-650+(n+1)*150,-400)
    return output

#~~~~~~~~~~#  2) Fonction(s) pour Dessiner:  #~~~~~~~~~~#

#aller à:
def aller(x,y,t):
    t.up()
    t.goto(x,y)
    t.down()

#Dessiner un polygone:
def dessinePolygone(x,y,nc,lc,t,couleur):
    aller(x,y,t)
    t.color(couleur)
    angle = 360/nc
    for i in range (nc):
        t.forward(lc)
        t.left(angle)
    
#Dessiner un pixel pour les pixels arts:
def pixel(p,c,x,y,t):
    t.begin_fill()
    dessinePolygone(x,y,4,p,t,c)
    t.end_fill()

#Dessiner un sous-marins en pixel art:    
def sous_marin(numero, x, y, p, tortue):
    
    if numero == 1:

        t = "turquoise"
        b = "thistle"
        bf = "dodgerblue"
        bc = "deepskyblue"
        jf = "gold"
        jc = "yellow"
        of = "darkorange"
        oc = "orange"

    elif numero == 2:

        t = "turquoise"
        b = "thistle"
        bf = "dodgerblue"
        bc = "deepskyblue"
        jf = "deeppink"
        jc = "hotpink"
        of = "darkred"
        oc = "crimson"

    x, y = x - 24, y - 14  # Bien positionner le dessin.

    # On stock les coordonnées dans des listes pour éviter les lignes inutiles.
    coo_x = [x + p * 17, x + p * 9, x + p * 9, x + p * 10, x + p * 15, x + p * 15, x + p * 16, x + p * 16, x + p * 16, x + p * 17, x + p * 18, x + p * 18, x + p * 18, x + p * 18, x + p * 10, x + p * 15, x + p * 15, x + p * 16, x + p * 16, x + p * 17, x + p * 17, x + p * 17, x + p, x + p * 2, x+p*5, x+p*5, x+p*6, x+p*6, x+p*7, x+p*11, x+p*11, x+p*12, x+p*13, x+p*13, x+p*8, x+p*8, x+p*9, x+p*9, x+p*10, x+p*10, x+p*11, x+p*11, x+p*14, x+p*14, x+p*14, x+p*14, x+p*15, x+p*15, x+p*16, x+p*17, x+p*18, x, x, x+p*3, x+p*3, x+p*3, x+p*4, x+p*4, x+p*17, x+p*17, x+p*18, x+p*5, x+p*6, x+p*7, x+p*8, x+p*9, x+p*10, x+p*11, x+p*12, x+p*13, x+p*14, x+p*15, x+p*16, x+p*5, x+p*6, x+p*7, x+p*8, x+p*9, x+p*10, x+p*11, x+p*12, x+p*13, x+p*14, x+p*15, x+p*16, x+p, x+p, x+p, x+p*2, x+p*2, x+p*2, x+p*8, x+p*8, x+p*8, x+p*9, x+p*9, x+p*10, x+p*11, x+p*12, x+p*4, x+p*5, x+p*6, x+p*7, x+p*8, x+p*11, x+p*12, x+p*13, x+p*14, x+p*5, x+p*6, x+p*7, x+p*8, x+p*9, x+p*10, x+p*11, x+p*12, x+p*13, x+p*14, x+p*15, x+p*16, x+p*10, x+p*10, x, x+p*3, x+p*3, x+p, x+p, x+p, x+p*2, x+p*2, x+p*2, x+p*10, x+p*10, x+p*10, x+p*10, x+p*11, x+p*12, x+p*12, x+p*4, x+p*4, x+p*4, x+p*4, x+p*5, x+p*5, x+p*5, x+p*6, x+p*6, x+p*6, x+p*7, x+p*7, x+p*7, x+p*7, x+p*8, x+p*8, x+p*8, x+p*9, x+p*9, x+p*10, x+p*10, x+p*11, x+p*11, x+p*11, x+p*12, x+p*12, x+p*12, x+p*12, x+p*13, x+p*13, x+p*13, x+p*14, x+p*9]
    coo_y = [y + p *7, y + p *4, y + p *5, y + p *4, y + p *4, y + p *5, y + p *4, y + p *5, y + p *8, y + p *8, y + p *4, y + p *5, y + p *6, y + p *7, y + p *5, y + p *6, y + p *7, y + p *6, y + p *7, y + p *4, y + p *5, y + p *6, y + p *6, y + p *6, y + p *5, y + p *6, y + p *5, y + p *6, y + p *6, y + p *10, y + p *11, y + p *6, y + p *5, y + p *6, y + p *4, y + p *5, y + p *3, y + p *6, y + p *3, y + p *6, y + p *4, y + p *5, y + p *4, y + p *5, y + p *6, y + p *7, y + p *3, y + p *8, y + p *3, y + p *3, y + p *3, y + p *3, y + p *4, y + p *2, y + p *3, y + p *4, y + p, y + p *2, y + p, y + p *2, y + p*2, y, y, y, y, y, y, y, y, y, y, y, y, y + p, y + p, y + p, y + p, y + p, y + p, y + p, y + p, y + p, y + p, y + p, y + p, y + p, y + p*2, y + p*3, y + p, y + p*2, y + p*3, y + p*9, y + p*10, y + p*11, y + p*10, y + p*11, y + p*9, y + p*9, y + p*9, y + p*3, y + p*3, y + p*3, y + p*3, y + p*3, y + p*3, y + p*3, y + p*3, y + p*3, y + p*2, y + p*2, y + p*2, y + p*2, y + p*2, y + p*2, y + p*2, y + p*2, y + p*2, y + p*2, y + p*2, y + p*2, y + p*12, y + p*13, y + p*5, y + p*5, y + p*6, y + p*4, y + p*5, y + p*7, y + p*4, y + p*5, y + p*7, y + p*10, y + p*11, y + p*14, y + p*15, y + p*15, y + p*10, y + p*11, y + p*4, y + p*5, y + p*6, y + p*7, y + p*4, y + p*7, y + p*8, y + p*4, y + p*7, y + p*8, y + p*4, y + p*5, y + p*7, y + p*8, y + p*6, y + p*7, y + p*8, y + p*7, y + p*8, y + p*7, y + p*8, y + p*6, y + p*7, y + p*8, y + p*4, y + p*5, y + p*7, y + p*8, y + p*4, y + p*7, y + p*8, y + p*8, y + p*9]
    ordre_couleur = [t, bf, bf, bf, bf, bf, bf, bf, bf, bf, bf, bf, bf, bf, bc, bc, bc, bc, bc, bc, bc, bc, jc, jc, jc, jc, jc, jc, jc, jc, jc, jc, jc, jc, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, jf, of]


    for i in range(len(coo_x)):
        pixel(p, ordre_couleur[i], coo_x[i], coo_y[i], tortue)

#Dessiner une ancre:
def Ancre(x,y,c,p,t):

    x, y = x-14, y-14  #Bien positionner le dessin.

    #On stock les coordonnées des pixels et leurs couleurs dans des listes pour éviter les lignes inutiles.
    coo_x = [x, x+p, x+p*2, x+p*3, x+p*3, x+p*4, x+p*4, x+p*4, x+p*4, x+p*4, x+p*5, x+p*5, x+p*5, x+p*5, x+p*5, x+p*5, x+p*5, x+p*5, x+p*5, x+p*6, x+p*6, x+p*6, x+p*6, x+p*6, x+p*7, x+p*7, x+p*8, x+p*9, x+p*10]
    coo_y = [y+p*3, y+p*2, y+p*2, y+p, y+p*5, y+p, y+p*5, y+p*7, y+p*8, y+p*9, y, y+p, y+p*2, y+p*3, y+p*4, y+p*5, y+p*6, y+p*7, y+p*9, y+p, y+p*5, y+p*7, y+p*8, y+p*9, y+p, y+p*5, y+p*2, y+p*2, y+p*3]
    couleurs = [c] * 29

    #Faire les pixels:
    for i in range(len(coo_x)):           
        pixel(p,couleurs[i],coo_x[i],coo_y[i],t)

#Dessiner une vague:
def Vague(num,x,y,c,p,t):
    
    if num==1:
        p1 = p
    else:
        p1 = -p

    w = "azure2"
    x, y = x-14, y-7  #Bien positionner le dessin.

    #On stock les coordonnées des pixels et leurs couleurs dans des listes pour éviter les lignes inutiles.
    coo_x = [x, x, x, x, x, x+p1, x+p1, x+p1, x+p1, x+p1, x+p1, x+p1*2, x+p1*2, x+p1*2, x+p1*2, x+p1*2, x+p1*2, x+p1*2, x+p1*3, x+p1*3, x+p1*3, x+p1*3, x+p1*3, x+p1*3, x+p1*3, x+p1*4, x+p1*4, x+p1*4, x+p1*4, x+p1*5, x+p1*5, x+p1*6, x+p1*7, x+p1*8, x+p1*9, x+p1*9, x+p1*5,x+p1*4,x+p1*6]
    coo_y = [y, y+p, y+p*2, y+p*3, y+p*4, y, y+p, y+p*2, y+p*3, y+p*4, y+p*5, y, y+p, y+p*2, y+p*3, y+p*4, y+p*5, y+p*6, y, y+p, y+p*2, y+p*3, y+p*4, y+p*5, y+p*6, y, y+p, y+p*5, y+p*6, y, y+p*5, y, y, y, y, y+p, y+p*6,y+p*4,y+p*5]
    couleurs = [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, w, w, w]

    #Faire les pixels:
    for i in range(len(coo_x)):           
        pixel(p,couleurs[i],coo_x[i],coo_y[i],t)

#Dessiner une mine:
def Mine(x,y,c,p,t):
    
    w = "azure"
    x, y = x-14, y-14  #Bien positionner le dessin.
    
    #On stock les coordonnées des pixels et leurs couleurs dans des listes pour éviter les lignes inutiles.
    coo_x = [x, x+p, x+p*2, x+p*2, x+p*2, x+p*3, x+p*3, x+p*3, x+p*3, x+p*3, x+p*4, x+p*4, x+p*4, x+p*5, x+p*5, x+p*5, x+p*5, x+p*5, x+p*5, x+p*5, x+p*5, x+p*5, x+p*5, x+p*6, x+p*6, x+p*6, x+p*6, x+p*6, x+p*7, x+p*7, x+p*7, x+p*7, x+p*7, x+p*8, x+p*8, x+p*8, x+p*9, x+p*10, x+p*4, x+p*4, x+p*5]
    coo_y = [y+p*5, y+p*5, y+p*2, y+p*5, y+p*8, y+p*3, y+p*4, y+p*5, y+p*6, y+p*7, y+p*3, y+p*4, y+p*7, y, y+p, y+p*2, y+p*3, y+p*4, y+p*5, y+p*7, y+p*8, y+p*9, y+p*10, y+p*3, y+p*4, y+p*5, y+p*6, y+p*7, y+p*3, y+p*4, y+p*5, y+p*6, y+p*7, y+p*2, y+p*5, y+p*8, y+p*5, y+p*5, y+p*5, y+p*6, y+p*6]
    couleurs = [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, w, w, w]
    
    #Faire les pixels:
    for i in range(len(coo_x)):           
        pixel(p,couleurs[i],coo_x[i],coo_y[i],t)

#Dessiner une tentacule:
def Tentacule(x,y,c,p,t):
    
    x, y = x-7, y-14  #Bien positionner le dessin.
    w = "lime"

    #On stock les coordonnées des pixels et leurs couleurs dans des listes pour éviter les lignes inutiles.
    coo_x = [x, x, x, x, x+p, x+p, x+p, x+p, x+p*2, x+p*2, x+p*2, x+p*3, x+p*3, x+p*3, x+p*3, x+p*4, x+p*4, x+p*4, x+p*4, x+p*4, x+p*4, x+p*4, x+p*4, x+p*5, x+p*5, x+p*5, x+p*5, x+p*5, x+p, x+p, x+p, x+p*2, x+p*2, x+p*2, x+p*3, x+p*3, x+p*3, x+p*4, x+p*4]
    coo_y = [y, y+p*6, y+p*7, y+p*8, y, y+p*5, y+p*8, y+p*9, y, y+p*8, y+p*9, y, y+p, y+p*2, y+p*9, y, y+p, y+p*2, y+p*3, y+p*4, y+p*6, y+p*8, y+p*9, y+p*3, y+p*4, y+p*5, y+p*6, y+p*7, y+p*2, y+p*7, y+p, y+p, y+p*2, y+p*3, y+p*3, y+p*4, y+p*8, y+p*5, y+p*7]
    couleurs = [c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, c, w, w, w, w, w, w, w, w, w, w, w]

    #Faire les pixels:
    for i in range(len(coo_x)):           
        pixel(p,couleurs[i],coo_x[i],coo_y[i],t)

#Dessiner une mouette:
def Mouette(x,y,p,t,para):

    w = "white"
    n = "black"
    g = "lavender"
    jf = "goldenrod"
    jc = "gold"
    
    if para == 1:       #Si p1 = p le dessin est dans le bon sens, si p1 = -p le dessin est en symétrie par rapport à l'axe vertical.
        p1 = p
        x, y = x-14, y-14  #Bien positionner le dessin.

    else:
        p1 = -p
        x, y = x+14, y-14  #Bien positionner le dessin.
    
    #On stock les coordonnées des pixels et leurs couleurs dans des listes pour éviter les lignes inutiles.
    coo_x = [x, x+p1, x+p1, x+p1*2, x+p1*2, x+p1*2, x+p1*3, x+p1*3, x+p1*4, x+p1*4, x+p1*5, x+p1*5, x+p1*5, x+p1*5, x+p1*5, x+p1*6, x+p1*6, x+p1*6, x+p1*6, x+p1*7, x+p1*7, x+p1*7, x+p1*7, x+p1*7, x+p1*8, x+p1*8, x+p1*8, x+p1*8, x+p1*8, x+p1*8, x+p1*9, x+p1*9, x+p1*9, x+p1*9, x+p1*9, x+p1*9, x+p1*9, x+p1*9, x+p1*10, x+p1*10, x+p1*10, x+p1*10, x+p1*10, x+p1*6, x+p1, x+p1*2, x+p1*2, x+p1*3, x+p1*3, x+p1*3, x+p1*4, x+p1*4, x+p1*4, x+p1*5, x+p1*5, x+p1*5, x+p1*6, x+p1*6, x+p1*6, x+p1*7, x+p1*7, x+p1*7, x+p1*8, x+p1*8, x+p1*7, x+p1*7, x+p1*7, x+p1*4, x+p1*4 ,x+p1*4, x+p1*9, x+p1*10, x+p1*11, x+p1*12, x+p1*13]
    coo_y = [y+p*7, y+p*6, y+p*7, y+p*3, y+p*6, y+p*7, y+p*6, y+p*7, y+p*6, y+p*7, y+p*10, y+p*6, y+p*7, y+p*8, y+p*9, y+p*10, y+p*6, y+p*7, y+p*9, y+p*10, y+p*6, y+p*7, y+p*8, y+p*9, y+p*10, y+p*3, y+p*6, y+p*7, y+p*8, y+p*9, y+p*10, y+p*3, y+p*4, y+p*5, y+p*6, y+p*7, y+p*9, y+p*10, y+p*4, y+p*5, y+p*6, y+p*7, y+p*9, y+p*8, y+p*5, y+p*4, y+p*5, y+p*3, y+p*4, y+p*5, y+p*3, y+p*4, y+p*5, y+p*3, y+p*4, y+p*5, y+p*3, y+p*4, y+p*5, y+p*3, y+p*4, y+p*5, y+p*4, y+p*5, y, y+p, y+p*2, y, y+p, y+p*2, y+p*8, y+p*8, y+p*8, y+p*8, y+p*8]
    couleurs = [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, n, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, jf, jf, jf, jc, jc, jc, jc, jc, jc, jc, jc]

    #Faire les pixels:
    for i in range(len(coo_x)):           
        pixel(p,couleurs[i],coo_x[i],coo_y[i],t)

#Dessiner les poissons:
def Poisson(numero,x,y,p,tortue):
   
    if numero == 1:
    
        w = "coral"
        n = "black"
        s = "cornsilk"
        couleurs = [ n, w, w, w, w, w, w, s, w, w, s, s, w, w, w, w, s, s, s, w, w, w, s, s, s, s, w, w, w, w, w, s, s, w, w, w, w, w, w, w, w, s, s, s, s, w, w, w, w, w, s, s, w, w, w, s, s, s, s, w, w, w, w, w, w, w, s, s, s, s, w, w, w, s, s, s, w, w, s, s, w, w, w, w, w, w, w, s, s, s, w, w, s, s, s, w, w, s, s, w, w, w, s, s, s, s, w, w, w, s, s, s, s, s, s, w, w, s, s, s, w, w, s, w]

    elif numero == 2:

        w = "royalblue"
        n = "black"
        s = "teal"
        t = "lightskyblue"
        couleurs = [ n, t, t, t, t, t, t, t, t, t, w, t, t, t, t, w, w, w, t, t, w, w, w, w, w, w, w, w, w, s, s, w, w, w, w, w, w, w, s, s, s, t, t, w, w, w, w, w, w, w, t, t, s, s, s, t, s, s, w, w, w, w, w, s, s, s, t, t, w, w, w, w, w, t, t, t, s, s, w, w, w, w, w, s, s, s, s, t, s, w, w, w, t, t, w, w, w, s, t, w, t, s, s, s, t, s, t, s, s, t, s, t, s, t, s, t, s, t, s, s, t, s, t, s]
    
    x, y = x-24, y-24  #Bien positionner le dessin.
    
    #On stock les coordonnées dans des listes pour éviter les lignes inutiles:
    coo_x = [ x+p*2, x, x, x+p*1, x+p*1, x+p*1, x+p*1, x+p*2, x+p*2, x+p*2, x+p*3, x+p*3, x+p*3, x+p*3, x+p*3, x+p*3, x+p*4, x+p*4, x+p*4, x+p*4, x+p*4, x+p*4, x+p*5, x+p*5, x+p*5, x+p*5, x+p*5, x+p*5, x+p*5, x+p*6, x+p*6, x+p*6, x+p*6, x+p*6, x+p*6, x+p*6, x+p*6, x+p*6, x+p*6, x+p*6, x+p*7, x+p*7, x+p*7, x+p*7, x+p*7, x+p*7, x+p*7, x+p*7, x+p*7, x+p*7, x+p*7, x+p*7, x+p*7, x+p*7, x+p*8, x+p*8, x+p*8, x+p*8, x+p*8, x+p*8, x+p*8, x+p*8, x+p*8, x+p*8, x+p*8, x+p*8, x+p*8, x+p*8, x+p*9, x+p*9, x+p*9, x+p*9, x+p*9, x+p*9, x+p*9, x+p*9, x+p*9, x+p*10, x+p*10, x+p*10, x+p*10, x+p*10, x+p*10, x+p*10, x+p*10, x+p*10, x+p*11, x+p*11, x+p*11, x+p*11, x+p*11, x+p*11, x+p*11, x+p*11, x+p*12, x+p*12, x+p*12, x+p*13, x+p*13, x+p*13, x+p*13, x+p*13, x+p*14, x+p*14, x+p*14, x+p*14, x+p*14, x+p*14, x+p*14, x+p*15, x+p*15, x+p*15, x+p*15, x+p*15, x+p*15, x+p*15, x+p*15, x+p*16, x+p*16, x+p*16, x+p*16, x+p*16, x+p*17, x+p*17]
    coo_y = [ y+p*7,y+p*6, y+p*7, y+p*5, y+p*6, y+p*7, y+p*8, y+p*5, y+p*6, y+p*8, y+p*4, y+p*5, y+p*6, y+p*7, y+p*8, y+p*9, y+p*4, y+p*5, y+p*6, y+p*7, y+p*8, y+p*9, y+p*4, y+p*5, y+p*6, y+p*7, y+p*8, y+p*9, y+p*10, y+p*2, y+p*3, y+p*4, y+p*5, y+p*6, y+p*7, y+p*8, y+p*9, y+p*10, y+p*11, y+p*12, y+p, y+p*2, y+p*3, y+p*4, y+p*5, y+p*6, y+p*7, y+p*8, y+p*9, y+p*10, y+p*11, y+p*12, y+p*13, y+p*14, y, y+p, y+p*2, y+p*3, y+p*5, y+p*6, y+p*7, y+p*8, y+p*9, y+p*10, y+p*11, y+p*12, y+p*13, y+p*14, y+p*5, y+p*6, y+p*7, y+p*8, y+p*9, y+p*10, y+p*11, y+p*12, y+p*13, y+p*4, y+p*5, y+p*6, y+p*7, y+p*8, y+p*9, y+p*10, y+p*11, y+p*12, y+p*3, y+p*4, y+p*5, y+p*6, y+p*7, y+p*8, y+p*10, y+p*11, y+p*6, y+p*7, y+p*8, y+p*5, y+p*6, y+p*7, y+p*8, y+p*9, y+p*4, y+p*5, y+p*6, y+p*7, y+p*8, y+p*9, y+p*10, y+p*4, y+p*5, y+p*6, y+p*7, y+p*8, y+p*9, y+p*10, y+p*11, y+p*4, y+p*5, y+p*9, y+p*10, y+p*11, y+p*4, y+p*11]

    #Faire les pixels:
    for i in range(len(coo_x)):           
        pixel(p,couleurs[i],coo_x[i],coo_y[i],tortue)

#Dessiner des Hippocamlpes:
def Hippocampe(numero,x,y,p,t):

    b = "white"             #8 blanc
    n = "black"             #1 noir
    g = "silver"            #22 gris
    j = "gold"              #47 jaune
    of = "darkorange"       #68 orange foncé
    oc = "orange"           #67 orange claires
    rf = "darkred"          #42 rouge foncé
    rc = "orangered"        #14 rouge clair

    if numero == 1:       #Si p1 = p le dessin est dans le bon sens, si p1 = -p le dessin est en symétrie par rapport à l'axe vertical.
        p1 = p
        x, y = x-14, y-14  #Bien positionner le dessin.

    else:
        p1 = -p
        x, y = x+14, y-14  #Bien positionner le dessin.
    
    #On stock les coordonnées des pixels et leurs couleurs dans des listes pour éviter les lignes inutiles.
    coo_x = [ x+p1*8, x+p1*6, x+p1*11, x+p1*3, x+p1*14, x+p1*11, x+p1*11, x+p1*9, x+p1*12, x+p1*5, x+p1*2, x+p1*7, x+p1, x, x, x+p1, x+p1*3, x+p1*3, x+p1*2, x+p1*2, x+p1*2, x+p1*3, x+p1*3, x+p1*3, x+p1*4, x+p1*4, x+p1*5, x+p1*5, x+p1*7, x+p1*9, x+p1*13, x+p1*4, x+p1*4, x+p1*3, x+p1*3, x+p1*4, x+p1*11, x+p1*9, x+p1*10, x+p1*3, x+p1*4, x+p1*7, x+p1*13, x+p1*4, x+p1*9, x+p1*11, x+p1*12, x+p1*13, x+p1*8, x+p1*10, x+p1*12, x+p1*5, x+p1*6, x+p1*7, x+p1*8, x+p1*8, x+p1*9, x+p1*15, x+p1*6, x+p1*7, x+p1*14, x+p1*4, x+p1*5, x+p1*10, x+p1*11, x+p1*12, x+p1*13, x+p1*10, x+p1*13, x+p1*6, x+p1*9, x+p1*10, x+p1*6, x+p1*9, x+p1*10, x+p1*11, x+p1*10, x+p1*11, x+p1*5, x+p1*3, x+p1*5, x+p1*6, x+p1*4, x+p1*7, x+p1*2, x+p1*3, x+p1*5, x+p1*7, x+p1*1, x+p1*2, x+p1*2, x+p1*3, x+p1*4, x+p1*3, x+p1*5, x+p1*1, x+p1*4,  x+p1*5, x+p1*6, x+p1*7, x+p1*8, x+p1*4, x+p1*7, x+p1*8, x+p1*3, x+p1*7, x+p1*4, x+p1*9, x+p1*10, x+p1*11, x+p1*2, x+p1*7, x+p1*8, x+p1*3, x+p1*4, x+p1*11, x+p1*12, x+p1*9, x+p1*10, x+p1*11, x+p1*12, x+p1*4, x+p1*5, x+p1*8, x+p1*9, x+p1*10, x+p1*3, x+p1*4, x+p1*8, x+p1*9, x+p1*10, x+p1*11, x+p1*12, x+p1*8, x+p1*9, x+p1*10, x+p1*12, x+p1*13, x+p1*12, x+p1*7, x+p1*11, x+p1*7, x+p1*8, x+p1*12, x+p1*6, x+p1*8, x+p1*10, x+p1*4, x+p1*3, x+p1*1, x+p1*2, x+p1*1, x+p1*2, x+p1*2, x+p1*3, x+p1*4, x+p1*5, x+p1*6, x+p1*7, x+p1*6, x+p1*5, x+p1*8, x+p1*9, x+p1*10, x+p1*7, x+p1*8, x+p1*5, x+p1*9, x+p1*10, x+p1*12, x+p1*7, x+p1*8, x+p1*5, x+p1*8, x+p1*13, x+p1*11, x+p1*12, x+p1*5, x+p1*8, x+p1*10, x+p1*13, x+p1*7, x+p1*11, x+p1*12, x+p1*13, x+p1*6, x+p1*7, x+p1*9, x+p1*6, x+p1*7, x+p1*8, x+p1*9, x+p1*10, x+p1*11, x+p1*9, x+p1*5, x+p1*6, x+p1*7, x+p1*16, x+p1*4, x+p1*5, x+p1*6, x+p1*5, x+p1*6, x+p1*7,x+p1*14, x+p1*5, x+p1*13, x+p1*13, x+p1*7, x+p1*8, x+p1*9, x+p1*12, x+p1*9, x+p1*5, x+p1*6, x+p1*7, x+p1*6, x+p1*3, x+p1*3, x+p1*4, x+p1*5, x+p1*6, x+p1*7, x+p1*8, x+p1*5, x+p1*9, x+p1*6, x+p1*10, x+p1*6, x+p1*7, x+p1*10, x+p1*6, x+p1*11, x+p1*6, x+p1*6, x+p1*6, x+p1*6, x+p1*7, x+p1*7, x+p1*6, x+p1*7, x+p1*5, x+p1*6, x+p1*5, x+p1*4, x+p1*5, x+p1*4, x+p1*15, x+p1*4, x+p1*14, x+p1*10, x+p1*11, x+p1*15, x+p1*8, x+p1*9, x+p1*4, x+p1*3, x+p1*8, x+p1*9, x+p1*9, x+p1*5, x+p1*5, x+p1*6, x+p1*10, x+p1*8, x+p1*7, x+p1*8, x+p1*9, x+p1*8]
    coo_y = [ y+p*4, y+p*6, y+p*25, y+p*29, y+p*30, y+p*31, y+p*36, y+p*37, y+p*32, y, y+p, y+p*2, y+p*3, y+p*5, y+p*8, y+p*10, y+p*12, y+p*15, y+p*17, y+p*19, y+p*20, y+p*21, y+p*25, y+p*27, y+p*31, y+p*32, y+p*33, y+p*35, y+p*36, y+p*36, y+p*35, y+p*15, y+p*16, y+p*17, y+p*18, y+p*18, y+p*18, y+p*19, y+p*19, y+p*20, y+p*20, y+p*20, y+p*21, y+p*22, y+p*22, y+p*22, y+p*22, y+p*22, y+p*25, y+p*25, y+p*25, y+p*27, y+p*27, y+p*27,y+p*27, y+p*28, y+p*28,y+p*28, y+p*29, y+p*29,y+p*29, y+p*30, y+p*30,y+p*30, y+p*30, y+p*30, y+p*30, y+p*31, y+p*31, y+p*32, y+p*32, y+p*32, y+p*33, y+p*33, y+p*33, y+p*33, y+p*34, y+p*34, y+p, y+p*2, y+p*2, y+p*2, y+p*3, y+p*3, y+p*4, y+p*4, y+p*5, y+p*5, y+p*6, y+p*6, y+p*8, y+p*8, y+p*9, y+p*10, y+p*10, y+p*5, y+p*11, y+p*12, y+p*12, y+p*13, y+p*13, y+p*14, y+p*14, y+p*15, y+p*16, y+p*16, y+p*17, y+p*17, y+p*17, y+p*17, y+p*18, y+p*18, y+p*18, y+p*19, y+p*19, y+p*19, y+p*19, y+p*20, y+p*20, y+p*20, y+p*20, y+p*21, y+p*21, y+p*21, y+p*21, y+p*21, y+p*22, y+p*23, y+p*23, y+p*23, y+p*23, y+p*23, y+p*23, y+p*24, y+p*24, y+p*24, y+p*29, y+p*29, y+p*31, y+p*32, y+p*32, y+p*33, y+p*33, y+p*33, y+p*34, y+p*35, y+p*35, y+p*2, y+p*3, y+p*5, y+p*5, y+p*7, y+p*7, y+p*9, y+p*9, y+p*10, y+p*11, y+p*11, y+p*12, y+p*13, y+p*16, y+p*16, y+p*16, y+p*16, y+p*17, y+p*17, y+p*18, y+p*18, y+p*18, y+p*18, y+p*19, y+p*19, y+p*20, y+p*20, y+p*20, y+p*21, y+p*21, y+p*22, y+p*22, y+p*22, y+p*23, y+p*24, y+p*24, y+p*24, y+p*24, y+p*25, y+p*25, y+p*25, y+p*26, y+p*26, y+p*26, y+p*26, y+p*26, y+p*26, y+p*27, y+p*28, y+p*28, y+p*28, y+p*28, y+p*29, y+p*29, y+p*30, y+p*31, y+p*31, y+p*31, y+p*31, y+p*32, y+p*32, y+p*33, y+p*34, y+p*34, y+p*34, y+p*34, y+p*35, y+p*3, y+p*3, y+p*4, y+p*5, y+p*6, y+p*7, y+p*8, y+p*9, y+p*10, y+p*11, y+p*12, y+p*13, y+p*13, y+p*14, y+p*14, y+p*15, y+p*15, y+p*15, y+p*16, y+p*16, y+p*17, y+p*18, y+p*19, y+p*20, y+p*21, y+p*22, y+p*23, y+p*23, y+p*24, y+p*24, y+p*25, y+p*26, y+p*26, y+p*27, y+p*27, y+p*28, y+p*28, y+p*29, y+p*29, y+p*29, y+p*30, y+p*30, y+p*4, y+p*5, y+p*14, y+p*14, y+p*15, y+p*17, y+p*19, y+p*21, y+p*27, y+p*29, y+p*30, y+p*31, y+p*31, y+p*32]
    couleurs = [ b, b, b, b, b, b, b, b, n, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, j, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, of, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, oc, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rf, rc, rc, rc, rc, rc, rc, rc, rc, rc, rc, rc, rc, rc, rc]

    #Faire les pixels:
    for i in range(len(coo_x)):           
        pixel(p,couleurs[i],coo_x[i],coo_y[i],t)

#Déssiner un crâne:
def skull(x,y,p,t):

    b = "teal"
    v = "darkseagreen"
    w = "ivory"
    i = "lightslategrey"
    k = "beige"

    x, y = x - 14, y - 14  # Bien positionner le dessin.

    # On stock les coordonnées dans des listes pour éviter les lignes inutiles.
    coo_x = [ x+p, x+p*2, x+p*3, x+p*4, x+p*5, x+p*4, x+p*5, x+p*5, x+p*6, x+p*6, x+p*6, x+p*8, x+p*10, x+p*11, x+p*12, x+p*13, x+p*14, x+p*13, x+p*14, x+p*15, x+p*16, x+p*17, x+p*12, x+p*12, x+p*12, x+p*13, x+p*13, x+p*14, x+p, x+p, x, x, x, x, x+p, x+p*2, x+p*3, x+p*4, x+p*4, x+p*5, x+p*5, x+p*6, x+p*6, x+p*8, x+p*8, x+p*10, x+p*10, x+p*12, x+p*12, x+p*4, x+p*5, x+p*6, x+p*7, x+p*8, x+p*9, x+p*10, x+p*10, x+p*11, x+p*12, x+p*13, x+p*14, x+p*15, x+p*7, x+p*8, x+p*8, x+p*9, x+p*9, x+p*10, x+p*10, x+p*11, x+p*2, x+p*2, x+p*2, x+p*3, x+p*3, x+p*3, x+p*4, x+p*4, x+p*14, x+p*14, x+p*15, x+p*15, x+p*15, x+p*16, x+p*16, x+p*16, x+p*13, x+p*13, x+p*14, x+p*14, x+p*15, x+p*16, x+p*16, x+p*17, x+p*18, x+p*18, x+p*18, x+p*18, x+p*18, x+p*18, x+p*18, x+p*18, x+p*17, x+p*17, x+p*16, x+p*17, x+p*16, x+p*16, x+p*15, x+p*15, x+p*14, x+p*7, x+p*8, x+p*9, x+p*9, x+p*9, x+p*10, x+p*11, x+p*2, x+p*3, x+p*3, x+p*4, x+p*4, x+p*5, x+p*5, x+p*5, x+p*6, x+p*12, x+p*13, x+p*13, x+p*13, x+p*14, x+p*14, x+p*15, x+p*15, x+p*16, x+p*7, x+p*9, x+p*11, x+p*3, x+p*3, x+p*3, x+p*3, x+p*3, x+p*4, x+p*4, x+p*5, x+p*5, x+p*6, x+p*6, x+p*7, x+p*7, x+p*8, x+p*8, x+p*9, x+p*9, x+p*10, x+p*11, x+p*12, x+p*13, x+p*14, x+p*15, x+p*15, x+p*15, x+p*15, x+p*7, x+p*7, x+p*7, x+p*8, x+p*8, x+p*8, x+p*9, x+p*9, x+p*9, x+p*10, x+p*10, x+p*10, x+p*11, x+p*11, x+p*11, x+p*5, x+p*6, x+p*6, x+p*12, x+p*12, x+p*13, x, x, x+p, x+p, x+p*2, x+p*3, x+p*4, x+p*5, x+p*6, x+p*7, x+p*7, x+p*8, x+p*8, x+p*10, x+p*10, x+p*11, x+p*11, x+p*12, x+p*13, x+p*14, x+p*15, x+p*16, x+p*17, x+p*2, x+p*3, x+p*4, x+p*5, x+p*6, x+p*6, x+p*6, x+p*7, x+p*7, x+p*9, x+p*9, x+p*9, x+p*11, x+p*11, x+p*12, x+p*12, x+p*12, x+p*13, x+p*14, x+p*15, x+p*17, x, x, x+p, x+p, x+p, x+p, x+p, x+p*2, x+p*2, x+p*3, x+p*4, x+p*6, x+p*7, x+p*7, x+p*7, x+p*8, x+p*8, x+p*8, x+p*9, x+p*9, x+p*9, x+p*10, x+p*10, x+p*10, x+p*11, x+p*11, x+p*11, x+p*12, x+p*2, x+p*2, x+p*3, x+p*4, x+p*5, x+p*6, x+p*7, x+p*8, x+p*9, x+p*10, x+p*11, x+p*12, x+p*12, x+p*13, x+p*13, x+p*14, x+p*14, x+p*14, x+p*14, x+p*13, x+p*15, x+p*15, x+p*15, x+p*16, x+p*16, x+p*17, x+p*17, x+p*17, x+p*17, x+p*17, x+p*14, x+p*15, x+p*6, x+p*7, x+p*8, x+p*9, x+p*10, x+p*11, x+p*4, x+p*5, x+p*6, x+p*7, x+p*8, x+p*9, x+p*10, x+p*11, x+p*12, x+p*3, x+p*4, x+p*5, x+p*6, x+p*7, x+p*8, x+p*9, x+p*10, x+p*11, x+p*12, x+p*13, x+p*3, x+p*4, x+p*5, x+p*6, x+p*7, x+p*8, x+p*9, x+p*10, x+p*11, x+p*12, x+p*13, x+p, x+p*2, x+p*2, x+p*3, x+p*3, x+p*4, x+p*4, x+p*5, x+p*5, x+p*5, x+p*6, x+p*6, x+p*6, x+p*7, x+p*7, x+p*7, x+p*7, x+p*8, x+p*8, x+p*9, x+p*9, x+p*10, x+p*10, x+p*11, x+p*11, x+p*11, x+p*11, x+p*12, x+p*12, x+p*12, x+p*13, x+p*13, x+p*14, x+p*14, x+p*15, x+p*16]
    coo_y = [ y+p*9, y+p*8, y+p*8, y+p*7, y+p*6, y+p*12, y+p*12, y+p*13, y+p*13, y+p*14, y+p*15, y+p*9, y+p*9, y-p, y-p, y, y+p, y+p*6, y+p*7, y+p*8, y+p*8, y+p*9, y+p*13, y+p*14, y+p*15, y+p*13, y+p*12, y+p*12, y+p*20, y+p*19, y+p*18, y+p*17, y+p*16, y+p*11, y+p*10, y+p*9, y+p*9, y+p*9, y+p*8, y+p*8, y+p*7, y+p*4, y+p*5, y+p*4, y+p*5, y+p*4, y+p*5, y+p*4, y+p*5, y+p, y, y-p, y-p, y-p, y-p, y-p, y, y, y, y+p, y+p*2, y+p*3, y+p*10, y+p*11, y+p*12, y+p*13, y+p*14, y+p*12, y+p*11, y+p*10, y+p*13, y+p*14, y+p*15, y+p*14, y+p*15, y+p*16, y+p*15, y+p*16, y+p*16, y+p*15, y+p*16, y+p*15, y+p*14, y+p*15, y+p*14, y+p*13, y+p*7, y+p*8, y+p*8, y+p*9, y+p*9, y+p*9, y+p*10, y+p*10, y+p*11, y+p*12, y+p*13, y+p*14, y+p*15, y+p*16, y+p*17, y+p*18, y+p*18, y+p*19, y+p*19, y+p*20, y+p*20, y+p*21, y+p*21, y+p*22, y+p*23, y+p*9, y+p*10, y+p*10, y+p*11, y+p*12, y+p*10, y+p*9, y+p*12, y+p*12, y+p*13, y+p*13, y+p*14, y+p*14, y+p*15, y+p*16, y+p*16, y+p*16, y+p*16, y+p*15, y+p*14, y+p*14, y+p*13, y+p*13, y+p*12, y+p*12, y+p*2, y+p*2, y+p*2, y+p*7, y+p*6, y+p*5, y+p*4, y+p*3, y+p*3, y+p*2, y+p*2, y+p, y+p, y, y+p, y, y+p, y, y+p, y, y+p, y+p, y+p, y+p*2, y+p*3, y+p*4, y+p*5, y+p*6, y+p*7, y+p*6, y+p*7, y+p*8, y+p*6, y+p*7, y+p*8, y+p*7, y+p*8, y+p*9, y+p*6, y+p*7, y+p*8, y+p*6, y+p*7, y+p*8, y+p*10, y+p*10, y+p*9, y+p*10, y+p*9, y+p*10, y+p*13, y+p*12, y+p*12, y+p*11, y+p*11, y+p*11, y+p*11, y+p*11, y+p*11, y+p*11, y+p*12, y+p*13, y+p*14, y+p*14, y+p*13, y+p*12, y+p*11, y+p*11, y+p*11, y+p*11, y+p*11, y+p*11, y+p*12, y+p*10, y+p*10, y+p*10, y+p*9, y+p*8, y+p*7, y+p*6, y+p*5, y+p*4, y+p*6, y+p*5, y+p*4, y+p*5, y+p*4, y+p*6, y+p*7, y+p*8, y+p*9, y+p*10, y+p*10, y+p*11, y+p*14, y+p*15, y+p*13, y+p*14, y+p*15, y+p*16, y+p*17, y+p*17, y+p*18, y+p*18, y+p*19, y+p*12, y+p*13, y+p*14, y+p*15, y+p*15, y+p*16, y+p*19, y+p*15, y+p*17, y+p*18, y+p*15, y+p*16, y+p*19, y+p*13, y+p*14, y+p*15, y+p*12, y+p*20, y+p*21, y+p*22, y+p*23, y+p*23, y+p*24, y+p*24, y+p*24, y+p*24, y+p*24, y+p*24, y+p*24, y+p*23, y+p*23, y+p*22, y+p*22, y+p*21, y+p*20, y+p*20, y+p*19, y+p*19, y+p*19, y+p*18, y+p*18, y+p*17, y+p*17, y+p*16, y+p*15, y+p*14, y+p*13, y+p*19, y+p*20, y+p*23, y+p*23, y+p*23, y+p*23, y+p*23, y+p*23, y+p*22, y+p*22, y+p*22, y+p*22, y+p*22, y+p*22, y+p*22, y+p*22, y+p*22, y+p*21, y+p*21, y+p*21, y+p*21, y+p*21, y+p*21, y+p*21, y+p*21, y+p*21, y+p*21, y+p*21, y+p*20, y+p*20, y+p*20, y+p*20, y+p*20, y+p*20, y+p*20, y+p*20, y+p*20, y+p*20, y+p*20, y+p*18, y+p*16, y+p*19, y+p*17, y+p*19, y+p*17, y+p*18, y+p*17, y+p*18, y+p*19, y+p*17, y+p*18, y+p*19, y+p*16, y+p*17, y+p*18, y+p*19, y+p*17, y+p*18, y+p*16, y+p*19, y+p*17, y+p*18, y+p*16, y+p*17, y+p*18, y+p*19, y+p*17, y+p*18, y+p*19, y+p*17, y+p*18, y+p*17, y+p*18, y+p*17, y+p*16]
    ordre_couleur = [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, i, v, v, v, k, k, k, k, k, w, k, w, k, w, k, w, k, w, k, w, k, k, k, k, k, k, k, k, k, k, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]

    for i in range(len(coo_x)):
        pixel(p, ordre_couleur[i], coo_x[i], coo_y[i], t)

#Dessiner un symbole:
def symbole(x,y,i,symbole,f):
    tracer(0,0)
    bouton[i].ht()

    if symbole == 1.1:
        sous_marin(1,x,y,f-0.4,bouton[i])
    
    elif symbole == 1.2:
        sous_marin(2,x,y,f-0.4,bouton[i])
    ####
    
    elif symbole == 2.1:
        Poisson(1,x,y,f,bouton[i])
    
    elif symbole == 2.2:
        Poisson(2,x,y,f,bouton[i])
    ####
    
    elif symbole == 3.1:
        Mouette(x,y,f-0.2,bouton[i],1)
    
    elif symbole == 3.2:
        Mouette(x,y,f-0.2,bouton[i],2)
    ####
    
    elif symbole == 4.1:
        Mine(x,y,"orangered4",f,bouton[i])

    elif symbole == 4.2:
        Mine(x,y,"slategrey",f,bouton[i])
    ####
    
    elif symbole == 5.1:
        Tentacule(x-14,y+14,"purple",f+0.4,bouton[i])
        Tentacule(x+14,y-14,"purple",f+0.4,bouton[i])

    elif symbole == 5.2:
        Tentacule(x+14,y+14,"purple",f+0.4,bouton[i])
        Tentacule(x-14,y-14,"purple",f+0.4,bouton[i])
    ####
    
    elif symbole == 6.1:
        Ancre(x,y,"peachpuff3",f,bouton[i])

    elif symbole == 6.2:
        Ancre(x,y,"azure4",f,bouton[i])
    ####
    
    elif symbole == 7.1:
        Vague(1,x,y,"lightseagreen",f,td)
    
    elif symbole == 7.2:
        Vague(2,x,y,"lightseagreen",f,td)
    ####

    elif symbole == 8.1:
        Hippocampe(1,x,y,f,td)
    ####

    elif symbole == 8.2:
        Hippocampe(2,x,y,f,td)
    update()

#Dessiner les cercles du sonar:
def cercles(t):

    #Grand cercle:
    t.left(90)
    aller(650,-320,t)   
    t.circle(650, 180, 1000)
    
    #Moyen cercle:
    t.left(180)  
    aller(400,-320,t)
    t.circle(400, 180, 1000)
    
    #Petit cercle:
    t.left(180)
    aller(150,-320,t)
    t.circle(150, 180, 1000)
    
    #Base:
    t.left(90)  
    aller(-740,-320,t)
    t.forward(1480)

#Dessiner les "rayons" du sonar:
def rayon(t, angle):
    t.seth(0)
    aller(0,-320,t)
    t.left(angle)
    t.forward(685)
    t.up()
    t.color("lime")
    t.write(str(angle)+"°", font=("Arial", 15, 'normal'))
    t.color("green")

#Dessiner le sonar:
def sonar(couleur):
    td.color("lime")
    FONT = ('Arial', 12, 'bold')

    
    t_sonar.ht()
    t_sonar.color(couleur)
    t_sonar.pensize(2)
    angle = [30,60,90,120,150]
    co_x = [-557,-331,-14,14,331,557,-342,-207,-14,14,207,342]
    co_y = [-34,214,308,308,214,-34,-150,-3,54,54,-3,-150]

    cercles(t_sonar)
    
    for i in angle:
        rayon(t_sonar,i)
    
    for i in range(12):
        aller(co_x[i],co_y[i],td)
        td.write(i+1, align='center', font=FONT)

    aller(-650,-400,td)
    td.write("Vies:",align='center', font=('Arial', 16, 'bold','underline'))

    Hippocampe(1,-750,90,10,td)
    skull(610,180,10,td)

    posi_x = [-770,770] 
    for i in posi_x:
        Vague(1,i-55,-210,"lightseagreen",8,td)
        Vague(1,i+25,-180,"lightseagreen",8,td)
        Vague(1,i,-280,"lightseagreen",8,td)

#Déssiner décor début:
def decor_debut():
    
    global tb

    message = "#####################################################################################" \
    "\n\nSonar [version 10.0.19042.1415]" \
        "\n(c) Memory Corporation. Tous droits réservés." \
            "\n\nSélectionner la difficulté:" \
                "\n\n\t1 --> Plancton" \
                    "\n\t2 --> Dauphin" \
                        "\n\t3 --> Requin" \
                            "\n\t4 --> Mobidick" \
                                "\n\t5 --> Leviathan" \
                                    "\n\t6 --> Kraken" \
                                        "\n\t7 --> Cthulhu" \
                                            "\n\n Avertissement: \n\tSi votre écran n'est pas en 1920*1080 le jeu risque de ne pas bien s'afficher." \
                                                "\n\tLes vies pourraient ne pas s'afficher, de même pour le décor." \
                                                    "\n\nÉchap pour quitter" \
                                                        "\n\n#####################################################################################"

    tb = Turtle()
    tracer(0,0)
    tb.ht()
    tb.up()
    tb.goto(-500,-200)
    tb.color("lime")
    tb.write(message,font=('Arial',14,'normal'))
    update()

#Déssiner décor fin:
def decor_fin(num):
    
    if num==1:
        Hippocampe(1,-450,-185,10,td)
        Hippocampe(2,450,-185,10,td)
    else:
        skull(-450,-100,10,td)
        skull(305,-100,10,td)

#Effacer tout:
def effacer():
    
    for i in range(len(cache)):             
            bouton[i].clear()
            bouton[i].ht()
    
    for i in range(vies):
        life[i].clear()

    t_sonar.clear()
    td.clear()

#~~~~~~~~~~#  3) Fonction(s) en rapport avec le clic de la souris:  #~~~~~~~~~~#

#Quoi faire quand un joueur clique sur une case:                     
def clique(x,y):
    
    global vies, n_false                            #Voir def jeu pour plus d'explications.
    

    #Toutes les cases sont masquées ou masquées avec une ou des paires trouvée(s):
    if n_false==0:
        n_false = 1                                 #Il s'agit donc du premier clic de la souris pour cette tentative, une seule et unique case va donc être retournée. 

    #Une seule case est retournée (On ne compte pas les paires déjà trouvées:
    elif n_false==1:
        n_false = 2                                 #Il s'agit donc du deuxième clic de la souris.


    #n_false vaut 1, l'utilisateur a donc cliqué sur une case fermée, résultat: 1 case a pour état "False" dans la liste "cache".
    if n_false==1:                                                                  
        
        num = num_case(x,y,n)                       #Retrouver le numéro de la case grâce aux coordonées x et y.
        choix.append(num)                           #On ajoute la case que l'utilisateur a choisit dans la liste "choix".
        
        cache[num-1] = False                        #On change la valeur qui correspond à son état dans la liste "cache" par "False" (Rappel: False ---> case ouverte)

        x_1, y_1 = Coordonnees(num,len(cache))                                      #Trouver les coordonnées de la case avec son numéro et le nb total de cases. (Pourquoi ne pas réutiliser les coo du clic? Le clic ne se trouvera jamais parfaitement au centre de la case pour bien centrer les symboles derrières les cases mieux vaut utiliser cette méthode.)
        symbole(x_1,y_1,num-1,liste_symboles[num-1],facteur)                        #On montre le symbole derrière la case en attendant que l'utilisateur fasse son second choix.

    #n_false vaut 2, l'utilisateur a donc cliqué sur deux cases fermées, résultat: 2 cases ont pour état "False" dans la liste "cache".
    elif n_false==2:                                                                

        #On bloque le jeu le temps que cette vérification se termine: 
        n_false = -1

        num = num_case(x,y,n)                       #Retrouver le numéro de la case grâce aux coordonées x et y.
        choix.append(num)                           #On ajoute la case que l'utilisateur a choisit dans la liste "choix".
        
        cache[num-1] = False                        #On change la valeur qui correspond à son état dans la liste "cache" par "False" (Rappel: False ---> case ouverte)

        x_2, y_2 = Coordonnees(num,len(cache))                                      #Trouver les coordonnées de la case avec son numéro et le nb total de cases. (Pourquoi ne pas réutiliser les coo du clic? Le clic ne se trouvera jamais parfaitement au centre de la case pour bien centrer les symboles derrières les cases mieux vaut utiliser cette méthode.)
        symbole(x_2,y_2,num-1,liste_symboles[num-1],facteur)                        #Afficher le symbole derrière la deuxième case cliquée.
        

        #Si les deux symboles sont de la même couleur: (int car 1.1 et 1.2 par exemple correspondent au même symbole, il s'agit juste de deux variantes.)
        if int(liste_symboles[choix[-1]-1]) == int(liste_symboles[choix[-2]-1]):    
                    
            #On remplace l'état des deux cases dans la liste "cache" par "bon".
            cache[choix[-1]-1], cache[choix[-2]-1] = "bon", "bon"           


        #Sinon: (Les deux symboles ne sont pas identiques)
        else:                                                                       
            
            #Attendre x secondes:
            time.sleep(duree) 

            #Retirer une vie:
            vies -= 1
            life[vies].clear()
                                                          

            for i in range(len(cache)):                     #Vérifier n fois, n étant la longueur de la liste "cache".
        
                if cache[i] == False:                       #Si la case a été retournée:

                    cache[i] = True                         #On réinitialise l'état des cases. (Rappel: l'état à l'origine est "True")
                    x, y = Coordonnees(i+1,len(cache))      #Coordonées du centre de la case i.
                    
                    tracer(0,0)                             #Ne pas montrer les mouv. de la tortue.
                    bouton[i].clear()                       #On efface ce que le bouton i a déssiné.
                    bouton[i].up()                          #Soulever le "crayon".
                    bouton[i].goto(x,y)                     #Aller à (x,y).
                    bouton[i].color(couleur_boutons)        #Couleur tortue.
                    bouton[i].st()                          #Afficher la tortue.
                    update()                                #Réafficher les mouv. de la tortue. 

        #Le jeu était bloqué en attendant que la vérification des cases ouvertes se termine, on réactive ici le jeu:
        n_false=0
    
    
    #Cas où nous n'avons plus de vie:
    if vies == 0:
        fin(2)

    #Toutes les paires sont trouvées:
    if cache == ["bon"] * n:                    
        fin(1)

#~~~~~~~~~~#  4) Fonction(s) en rapport avec la pression d'une touche:  #~~~~~~~~~~#

#Activer la pression des touches clavier:
def press():
    
    #Quitter en appuyant sur "échap":
    onkeypress(bye,"Escape")

    ##### Choix de la difficulté en fonction de la touche pressée #####
    
    def reglage_1():            #Touche "1"
        jeu(1)
    onkeypress(reglage_1,"1")
    
    def reglage_2():            #Touche "2"
        jeu(2)
    onkeypress(reglage_2,"2")

    def reglage_3():            #Touche "3"
        jeu(3)
    onkeypress(reglage_3,"3")   

    def reglage_4():            #Touche "4"
        jeu(4)
    onkeypress(reglage_4,"4")

    def reglage_5():            #Touche "5"
        jeu(5)
    onkeypress(reglage_5,"5")

    def reglage_6():            #Touche "6"
        jeu(6)
    onkeypress(reglage_6,"6")
    
    def reglage_7():            #Touche "7"
        jeu(7)
    onkeypress(reglage_7,"7")

#Désactiver la pression des touches clavier sauf Escape:
def unpress():
    onkeypress(None,"1")
    onkeypress(None,"2")
    onkeypress(None,"3")
    onkeypress(None,"4")
    onkeypress(None,"5")
    onkeypress(None,"6")
    onkeypress(None,"7")

#~~~~~~~~~~#  5) Affichage:  #~~~~~~~~~~#

def fullscreen():
    screensize(canvwidth=1920, canvheight=1080,bg='black')
    Screen().setup(width=1.0, height=1.0, startx=None, starty=None)   #Fenêtre Turtle équivalente à un plein écran fenêtré.

#Récupère la postion d'un click (utile pour placer les symboles):
def getpos(x,y):
    print(x,y)

#~~~~~~~~~~#  6) Autre(s):  #~~~~~~~~~~#

#symboles des paires
def liste_symbole(n):

    if n==6:
        output = [1.1,1.2,2.1,2.2,3.1,3.2]
    
    if n==8:
        output = [1.1,1.2,2.1,2.2,3.1,3.2,4.1,4.2]

    if n==10:
        output = [1.1,1.2,2.1,2.2,3.1,3.2,4.1,4.2,5.1,5.2]
    
    if n==12:
        output = [1.1,1.2,2.1,2.2,3.1,3.2,4.1,4.2,5.1,5.2,6.1,6.2]

    random.shuffle(output)
    return output

#Afficher le nombre de vies restantes:
def afficher_vies(nb_vies):

    for i in range(nb_vies):
        x_vie, y_vie = Coordonnees_vies(i) 
        #skull(x_vie,y_vie,2,life[i])
        Hippocampe(1,x_vie,y_vie,2,life[i])

#Jeu terminé:
def fin(resultat):

    #Attendre x secondes:
    time.sleep(1)
    
    #Gagner ou perdu?
    if resultat==1:
        output = "You win!"
    else:
        output = "You lose!"

    tracer(0,0)
    
    #Effacer tout:
    effacer()
    
    #Déssiner décor fin:
    decor_fin(resultat)
    
    t = Turtle()
    td.color("white")
    td.ht()
    aller(-80,0,td)
    td.write(output,font=('Arial',30,'normal'))
    
    update()

    time.sleep(4)
    
    #Rejouer
    effacer()
    decor_debut()
    press()

#Régler les paramètres en fonction de la difficulté:        #Plancton / Dauphin / Requin / Mobidick / Leviathan / Kraken / Cthulhu
def difficulty(choix):

    if choix==1:        #Plancton
        
        vies = 6        #Nombre d'erreurs max autorisées.
        duree = 1.5     #Durée durant laquelle les cases restent découvertes avant de se retourner. (En secondes)
        n = 6           #Nombre de case.

    elif choix==2:      #Dauphin
        
        vies = 5
        duree = 1.5
        n = 8

    elif choix==3:      #Requin
    
        vies = 4
        duree = 1.5
        n = 8
    
    elif choix==4:      #Mobidick
        
        vies = 6
        duree = 1.5
        n = 10

    elif choix==5:      #Leviathan
    
        vies = 5
        duree = 1.5
        n = 10

    elif choix==6:      #Kraken
        
        vies = 6
        duree = 0.5
        n = 12
    
    elif choix==7:      #Cthulhu

        vies = 5
        duree = 0.05
        n = 12


    output = (vies,duree,n)
    return output

##################################################################################################################

'''Le jeu:'''

def jeu(difficulte):

    #Pourquoi utiliser global? Le jeu se base sur la fonction clique, étant donné que la fonction clique est executée lors d'un clic elle ne peut prendre que deux arguments (x,y) qui correspondent aux coordonées du clic de la souris.
    #Cependant il faut que la fonction clique dispose d'autres valeurs/arguments comme le nb de vies par exemple. On pourrait définir ces variables en dehors d'une fonction mais cela n'est pas compatible avec le menu qui utilise la pression d'une touche pour sélectionner la difficulté.
    #Voilà pourquoi on utilise un global même si ce n'est pas conseillé.
    global vies, duree, n, choix, numero_liste, cache, facteur, couleur_boutons, td, t_sonar, bouton, liste_symboles, life, n_false
    
    
    #Désactiver les touches qui permetent de choisir la difficulté:
    unpress()
    
    #Effacer décor début:
    tb.clear()

    #Choix difficulté: 
    vies, duree, n = difficulty(difficulte)

    choix = []                                  #Liste qui nous servira à retenir les choix que fait l'utilisateur.
    numero_liste = [i for i in range(1,n+1)]    #Liste qui servira au bot pour tirer aléatoirement deux cases. 
    cache = [True] * n                          #Liste indiquant les cases ouvertes et fermées. ouverte --> False ; fermée --> True ; Au début du jeu toutes les cases sont fermées. 
    facteur = 3                                 #Taille des dessins.
    couleur_boutons = "red"                     #Couleur des boutons.

    #Créer la tortue du décor:
    td = Turtle()
    td.ht()

    #Créer la tortue du sonar:
    t_sonar = Turtle()

    #Créer n boutons:
    bouton = []         
    tracer(0,0)                                   #Ne pas montrer les mouv. de la tortue.
    for i in range(n):
    
        #Coordonnées de chaque bouton.
        coo = Coordonnees(i+1,n)

        bouton.append("b" + str(i))                 #Associer à chaque variable: "bouton[i]", la chaîne de caractère: "bi".
        bouton[i] = Turtle()                        #Créer des tortues nommées "bi". (Utiliser "bouton[i]" dans la suite du programme et non "bi" !!!).
        bouton[i].speed(0)                          #Changer la vitesse des boutons. (speed(0) --> le plus rapide)
        bouton[i].shape('circle')                   #Forme des boutons.
        bouton[i].fillcolor(couleur_boutons)        #Remplir le cercle.
        bouton[i].up()                              #Soulever le "crayon".
        bouton[i].goto(coo[0], coo[1])              #Aller à (x,y).
        bouton[i].onclick(clique)                   #Que se passe t'il en cliquant sur un bouton? On éxecute la fonction "clique" avec comme paramètres x,y (position de la souris au moment du clic)


    #Créer les tortues des vies
    life = []         
    for i in range(vies):
    
        #Coordonnées de chaque bouton.s
        x_v, y_v = Coordonnees_vies(i)

        life.append("l" + str(i))                 #Associer à chaque variable: "life[i]", la chaîne de caractère: "li".
        life[i] = Turtle()                        #Créer des tortues nommées "li". (Utiliser "life[i]" dans la suite du programme et non "li" !!!).
        life[i].speed(0)                          #Changer la vitesse des boutons. (speed(0) --> le plus rapide)
        life[i].ht()                              #Cacher la tortue.
        life[i].shape('circle')                   #Forme des boutons.
        life[i].fillcolor("lime")                 #Remplir le cercle.
        life[i].up()                              #Soulever le "crayon".
        life[i].goto(x_v, y_v)                    #Aller à (x,y).
    
    #Afficher les vies:
    afficher_vies(vies)
    
    #Déssiner le sonar:
    sonar("green")

    #Réafficher les mouv. de la tortue:
    update()                                        
    
    #Créer la liste qui nous servira à associer chaque case avec un symbole.
    liste_symboles = liste_symbole(n)

    #Le jeu débute avec toutes les cases caché:
    n_false = 0
    
##################################################################################################################

'''Débuter le jeu:'''

#Régler l'affichage:
fullscreen()

#Ecouter pour savoir si un événement arrive (ex: pression d'une touche):                          
listen()

#Ajouter les commandes au clavier:
press()

#Décor début:
decor_debut()

#test
#onscreenclick(getpos)

#Empêcher le programme de se fermer:
done()                                          
