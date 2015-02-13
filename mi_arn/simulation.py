#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from math import floor

from recherche_motif import util

complement_dic_arn_2 = {'A':'U',
    'U':('A','G'),
    'G':('C','U'),
    'C':'G'}



def simule_premiARN(filename="random_premiARN",
                    len_min_boucle = 0,
                    len_max_boucle = 8,
                    len_min_premiARN = 70, 
                    len_max_premiARN = 100,
                    nb_min_appariement = 24,
                    nb_min_miniboucle = 0):
    '''
    Fonction simulant un pré_miARN
    
    :return: -Nom du fichier généré
    :return: -[Tous les indices des miARN présent, chaines_miARN]
    '''
    #24+ appariement, par groupe de 3+
    #70-100 pour la chaine totale du pré_miARN
    #mi_ARN commence entre l'indice 10-15 compris, et est de taille 20-23
    #boucle terminale 0-8 et les autres boucles 0-3
    
    chaine = []
    
    #============================
    #|étape 1: générer la boucle|
    #============================
    #on trouve une longueur de boucle
    len_boucle = random.randint(len_min_boucle,len_max_boucle)
    #on calcule la longueur de la moitié de la boucle
    len_mi_boucle = len_boucle / 2
    
    mi_boucle = [random.choice('AUGC') for i in xrange(len_mi_boucle)]
    pivot = [random.choice('AUGC')]
    mi_boucle2 = non_complement(mi_boucle[::-1])
    if not len_boucle % 2:
        chaine = mi_boucle + mi_boucle2
    else:
        chaine =  mi_boucle + pivot + mi_boucle2
    
    
    #==================================================
    #|étape 2: generer les deux moitiés complementaire|
    #==================================================
    #on trouve une longueur de chaine max 
    len_chaine = random.randint(len_min_premiARN,len_max_premiARN) - len_boucle    
    #on calcule la longueur de la chaine avant la boucle
    len_moitie = len_chaine / 2    

    moitie = [random.choice('AUGC') for i in xrange(len_moitie)]
    moitie2 = complement(moitie[::1])
    
    chaine2 = moitie+moitie2
    #=================================
    #|étape 3:inserer des miniboucles|
    #=================================
    nb_max_miniboucle = len_max_premiARN -(len_boucle + len_chaine)
    nb_max_miniboucle = int(floor(nb_max_miniboucle/3))
    
    nb_miniboucle = random.randin(nb_min_miniboucle,nb_max_miniboucle)
    
    
    
    return chaine,chaine2,len_chaine,moitie,moitie2

def complement(motif,dic=complement_dic_arn_2):
    aa = 'AUGC'
    res = []

    for c in motif:
        comp = dic[c]
        if len(comp)>1:
            comp = random.choice([comp[0],comp[1]])
        res.append(comp)
    return res

def non_complement(motif,dic=complement_dic_arn_2):
    aa = 'AUGC'
    res = []
    
    for c in motif:
        comp = dic[c]
        if len(comp)>1:
            comp = [comp[0],comp[1]]
        list_diff = util.diff(aa,comp)
        new_c = random.choice(list_diff)
        res.append(new_c)
    return res #une liste 
        

#print non_complement('UAGC',complement_dic_arn_2)
#print complement('UUUU')
c1,c2,l,m,m2  = simule_premiARN()
print c1,l
print m
print m2[::1]
print c2
