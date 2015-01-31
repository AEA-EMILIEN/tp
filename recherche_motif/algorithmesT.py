#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import *
import algorithmes as algo
from multiprocessing.pool import ThreadPool


 

def unwrap(a_b):
    return algo.brute_force(*a_b)

def cherche_generiqueT(motif,chaine_adn,func=algo.brute_force,comp_dic=complement_dic_adn):
    '''
    Fait une recherche de motif,inverse,complement,complement-inverse
    dans une chaine avec une fonction passe en parametre.
    Si aucune fonction n'est précisé, brute force est utilisé.
 
    '''
    p = ThreadPool(processes=8)


    indice_occ = []
    inv = inverse(motif)
    comp = complement(motif,comp_dic)
    comp_inv = complement_inverse(motif,comp_dic)
    c = chaine_adn
    res= p.map(unwrap, [(motif,c),(inv,c),(comp,c),(comp_inv,c)])
    #p.close()
    #p.join()
    occ = res[0][0] + res[1][0] + res[2][0] + res[3][0]
    indice_occ =  res[0][1] + res[1][1] + res[2][1] + res[3][1]
    return occ, sorted(indice_occ)
    


print cherche_generiqueT('GAGA','GATATAGATAGAGAGGAATATGATAGATAGTAGAGACCCC')



