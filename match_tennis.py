# -*- coding: utf-8 -*-
import os
os.system("cls")

import numpy as np

def augmente_score(tableau_score,gagnant):
    index_gagnant=gagnant
    index_perdant=int(not(index_gagnant)) 
    
    if tableau_score[2,index_gagnant]<40:
        tableau_score[2,index_gagnant]=augmente_point(tableau_score[2,index_gagnant])

    elif tableau_score[2,index_gagnant]==40:
        if tableau_score[2,index_perdant]<40:
            tableau_score[2,index_gagnant]=0
            tableau_score[2,index_perdant]=0
            tableau_score[1,index_gagnant]+=1
            if  (tableau_score[1,index_gagnant]==6 and tableau_score[1,index_perdant]<5) or (tableau_score[1,index_gagnant]==7):
                tableau_score[1,index_gagnant]=0
                tableau_score[1,index_perdant]=0
                tableau_score[0,index_gagnant]+=1
                
        elif  tableau_score[2,index_perdant]==40:
            tableau_score[2,index_gagnant]=augmente_point(tableau_score[2,index_gagnant])
        elif tableau_score[2,index_perdant]>40:
            tableau_score[2,index_perdant]=40
            
    elif tableau_score[2,index_gagnant]==41:
        tableau_score[2,index_gagnant]=0
        tableau_score[2,index_perdant]=0
        tableau_score[1,index_gagnant]+=1
    
def augmente_point(point):
    possible_points=[0,15,30,40,41]
    index=possible_points.index(point)
    return possible_points[index+1]



fichier = open("historique.txt", "r")
score= fichier.read()
tableau_points=score.split("\n")
print(tableau_points)
fichier.close()

score_init=np.zeros((3,2))
score=score_init[:]

joueur1='Nadal'
joueur2='Federer'

for i in tableau_points:
    if i==joueur1:
       augmente_score(score,0)
        
    elif i==joueur2:
        augmente_score(score,1)
    
    print(i)
    print(score)
    print("")

    
