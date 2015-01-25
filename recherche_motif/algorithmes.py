#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
module Algorithmes
==================



Modules contenant nos implémentations des algorithmes de recherche de motifs dans une chaine.
'''

import util 



def brute_force(motif,chaine_adn):
    '''
    Algorithme de recherche de motif en brute force
    
    :param motif: Le motif qu'on veut retrouver dans la chaine.
    :param chaine_adn: La chaine dans laquelle on fait la recherche de motif.
    :type motif: string
    :type chaine_adn: string
    :return: Le nombre d'occurence du motif.
    
    :Exemple:
    
    >>> brute_force('AT','ATTTTATATTTA')
    3


    .. seealso:: boyer_moore()

    '''
    occ = 0 
    len_chaine_adn = len(chaine_adn) 
    len_motif = len(motif)
    for c1 in xrange(0,len_chaine_adn-len_motif+1):  
        for c2 in xrange(0,len_motif):
            if (chaine_adn[c1+c2]!=motif[c2]):
                break
            else :
                if (c2==len_motif-1):
                    occ+=1
    return occ,[]





def hachage_rabin_karp(motif):	
    '''
    Effectue un hachage sur un motif passé en paramêtre.
    
    :param motif: Le motif que l'on veut haché.
    :type motif: string
    :return: La valeur du hachage du motif
    :rtype: int
    
    
    :Example:
    
    >>> hachage_rabin_karp('GA')
    5
    
    >>> hachage_rabin_karp('CT')
    10
    
    .. seealso::
    .. warning:: Ne fonctionne qu'avec les caractères A,C,T et G
    .. note:: Voir si une autre fonction de hachage ne serait pas plus performante
    
    '''
	
    base_azotee = { 'A':1 , 'C':2 , 'G':3 , 'T':4 }
    chaine_hache = [base_azotee[c] for c in motif]
    for i in xrange(0,len(motif)):
        chaine_hache[i]= (i+1)*chaine_hache[i]
    return sum(chaine_hache)
	
def rabin_karp(motif,chaine_adn):
    '''
    recherche de motif avec l'algorithme de rabin_karp
   
    :param motif: Le motif à trouver dans la chaine_adn
    :param chaine_adn: Chaine de caractère representant un séquence d'AA
    :type motif: string
    :type chaine_adn: string
    :return: nombre d'occurence du motif dans la chaine,
             les indices de ces occurences dans la chaine
    :rtype: int,[int]
    
    :Exemple:
    
    >>> rabin_karp('GA', 'GATACA')
    (1, [0])
    
    >>> rabin_karp('GATACA', 'TAGATACATAGATAGATACA')
    (2, [2, 14])
    
    .. seealso::
    .. warning::
    .. notes ::

    '''
    occ = 0
    len_chaine_adn = len(chaine_adn)
    hachage_motif = hachage_rabin_karp(motif)
    chaine_hachage = range(0,len_chaine_adn+1)
    len_motif = len(motif)
    indice_occ = []
    

    for i in xrange(0,len_chaine_adn-len_motif+1):
        #print i
        chaine_hachage[i] = hachage_rabin_karp(chaine_adn[i:i+len_motif])
        if (chaine_hachage[i]==hachage_motif and
            chaine_adn[i:i+len_motif]==motif):
            occ+=1
            indice_occ.append(i)
	
    return occ,indice_occ

def cherche_generique(motif,chaine_adn,func=brute_force):
    '''
    fait une recherche de motif,inverse,complement,complement-inverse
    dans une chaine avec une fonction passe en parametre.
    si aucune fonction n'est precise, brute force est utilise
    '''
    occ_motif,_ = func(motif,chaine_adn)
    occ_inv,_   = func(util.inverse(motif),chaine_adn)
    occ_comp,_  = func(util.complement(motif),chaine_adn)
    occ_comp_inv,_ = func(util.complement_inverse(motif),chaine_adn)
    
    occ = occ_motif + occ_inv + occ_comp + occ_comp_inv
    indice_occ = []
    return occ, indice_occ
    
def boyer_moore(motif, chaine_adn) :
    '''
    Implémentation de l'algorithme de Boyer-Moore
    
    :param motif: Le motif à trouver dans la chaine_adn
    :param chaine_adn: Chaine de caractère representant un séquence d'AA
    :type motif: string
    :type chaine_adn: string
    :return: nombre d'occurence du motif dans la chaine,
             les indices de ces occurences dans la chaine
    :rtype: int,[int]

    :Exemple:
    
    >>> boyer_moore("GATACA","GATACAACACATACAGATACATATAG")
    2
    
    .. seealso:: brute_force()
    .. note:: Boyer-Moore est plus performant sur des long motifs et/ou sur des 
              alphabets étendus en théorie
    '''
    dico = apprentissage_boyer_moore(motif)
    cpt = len(motif)-1
    occ = 0
    indice_occ = []
    while (cpt < len(chaine_adn)) :
        boolean, cpt = compare_boyer_moore(motif, chaine_adn, cpt) 
        if (boolean) :
            occ += 1
            indice_occ.append(cpt)
            cpt += len(motif)
        else :
            if (chaine_adn[cpt] in dico) :
                    cpt += dico[chaine_adn[cpt]]
            else :
                cpt += len(motif)
    return occ,indice_occ


def apprentissage_boyer_moore(motif) : 
    '''
    Création de la table de saut pour le motif
    
    :param motif: Le motif pour lequel une table de saut va être créé
    :type motif: string
    :return: Un dictionnaire contenant la table des saut du motif
    :rtype: dic char->int
    
    :Exemple:
    
    #TODO
    
    '''
    list_key = []
    list_value = []
    fitom = util.inverse(motif) 
    for m in fitom[1:]:
        if (m not in list_key and m != fitom[0]):
            list_key.append(m)
            list_value.append(fitom.index(m))
    return dict(zip(list_key, list_value))		

def compare_boyer_moore(motif, chaine_adn, cpt) :
    i = 0
    size = len(motif)-1
    while (i <= size) :
        #print motif[size-i], chaine_adn[cpt-i]
        if (motif[size-i] == chaine_adn[cpt-i]) :
	       	i += 1
        else :
            return False,cpt-i
    return True,cpt-i+1



if __name__ == "__main__":
    import doctest
    doctest.testmod()
