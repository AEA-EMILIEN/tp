#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import *
import algorithmes as algo
from multiprocessing.pool import Pool
from joblib import Parallel, delayed

 

def unwrap(a_b):
    '''
    unpack args
    
    :Example:
    
    >>> unwrap([
    '''
    return algo.brute_force(*a_b)

def cherche_generiqueT(motif,chaine_adn,func=algo.brute_force,comp_dic=complement_dic_adn):
    '''
    Fait une recherche de motif,inverse,complement,complement-inverse
    dans une chaine avec une fonction passe en parametre.
    Si aucune fonction n'est précisé, brute force est utilisé.
 
    '''
    p = Pool(processes=16)


    indice_occ = []
    inv = inverse(motif)
    comp = complement(motif,comp_dic)
    comp_inv = complement_inverse(motif,comp_dic)
    c = chaine_adn
    #version ac map
    res= p.map(unwrap, [(motif,c),(inv,c),(comp,c),(comp_inv,c)])
    p.close
    p.join()
    
    #version ac apply_async
    #res_intermediaire = [p.apply_async(func,args=x) for x in [(motif,c),(inv,c),(comp,c),(comp_inv,c)]]
    #p.close()
    #p.join()
    #res = [p.get() for p in res_intermediaire]
    occ = res[0][0] + res[1][0] + res[2][0] + res[3][0]
    indice_occ =  res[0][1] + res[1][1] + res[2][1] + res[3][1]
    return occ, sorted(indice_occ)
    



def cherche_generiqueP(motif,chaine_adn,func=algo.brute_force,comp_dic=complement_dic_adn):
    '''
    Recherche un motif, son complément, son inverse et son complément_inverse et additione leurs occurences en
    utilisant plusieurs processus pour essayer d'améliorer les performances de recherche_generique().
    
    :param motif: Le motif dont on cherche l'indice et le nombre d'occurence.
    :param chaine_adn: La chaine dans laquelle on fait la recherche.
    :param func: L'algorithme de recherche de motif à utiliser. Par défaut, utilise brute_force défini dans algorithmes.py
    :param comp_dic: Le dictionnaire définissant les complémentaires en fonction des AA présent dans la chaine_adn. Par défaut, utilise complement_dic_adn défini dans util
    :type motif: string
    :type chaine_adn: string
    :type func: func(string,string)
    :type comp_dic: dic(char,char)
    :return: Un tuple contenant :
             -La somme des occurence d'un motif, de son inverse, de son complément, et de son complément inverse.
             -La liste des indices des occurences du motif, de son inverse, de son complément, et de son complément inverse.
    :rtype: (int,[int])
    
    :Exemples:
    
    TODO
    

    ..seealso::cherche_generique(), cherche_generiqueT()


    '''

    indice_occ = []
    inv = inverse(motif)
    comp = complement(motif,comp_dic)
    comp_inv = complement_inverse(motif,comp_dic)
    c = chaine_adn
    
    res = Parallel(n_jobs=4)(delayed(func)(m,c) for m in [motif,inv,comp,comp_inv])
    occ = res[0][0] + res[1][0] + res[2][0] + res[3][0]
    indice_occ =  res[0][1] + res[1][1] + res[2][1] + res[3][1]
    return occ, sorted(indice_occ)
    
    



