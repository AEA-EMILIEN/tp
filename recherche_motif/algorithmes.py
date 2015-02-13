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
    (3, [0, 5, 7])


    .. seealso:: boyer_moore(),kmp()

    '''
    occ = 0 
    len_chaine_adn = len(chaine_adn) 
    len_motif = len(motif)
    indice_occ = []
    for c1 in xrange(0,len_chaine_adn-len_motif+1):  
        if (chaine_adn[c1:c1+len_motif] == motif):
            occ+=1
            indice_occ.append(c1)
    return occ,indice_occ





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
        chaine_hachage[i] = hachage_rabin_karp(chaine_adn[i:i+len_motif])
        if (chaine_hachage[i]==hachage_motif and
            chaine_adn[i:i+len_motif]==motif):
            occ+=1
            indice_occ.append(i)
	
    return occ,indice_occ

def cherche_generique(motif,chaine_adn,func=brute_force,comp=util.complement_dic_adn):
    '''
    Fait une recherche de motif,inverse,complement,complement-inverse
    dans une chaine avec une fonction passe en parametre.
    Si aucune fonction n'est précisé, brute force est utilisé.
 
    '''
    occ_motif,indice_motif = func(motif,chaine_adn)
    occ_inv,indice_inv   = func(util.inverse(motif),chaine_adn)
    occ_comp,indice_comp  = func(util.complement(motif,comp),chaine_adn)
    occ_comp_inv,indice_comp_inv = func(util.complement_inverse(motif,comp),chaine_adn)
    
    occ = occ_motif + occ_inv + occ_comp + occ_comp_inv
    indice_occ = indice_motif + indice_inv + indice_comp + indice_comp_inv
    return occ, sorted(indice_occ)
    


    '''
    Implémentation de l'algorithme de Boyer-Moore
   
    '''

def generateBC(motif,size) :
	'''
	Initialise la table des "bad characters" avec le motif de taille size

	:param motif: Le motif que l'on veut trier
	 :param size: la taille du motif
	:type motif: string
	 :type size: int
<<<<<<< HEAD
	:return: Le tableau BC
	:rtype: dict


	:Example:

	>>> generateBC('GATACA',6)
	{'A': 2, 'C': 1, 'T': 3, 'G': 5}

	'''
	listBC = {}
	for i in range(0, size-1) :
		listBC[motif[i]] = size-i-1
	return listBC

  
def generateGS(motif,size) :
	'''
	Initialise la table des "good suffix" avec le motif de taille size
	    
	:param motif: Le motif que l'on veut trier
	:param size: la taille du motif
	:type motif: string
	:type size: int
	:return: Le tableau GS
	:rtype: dict
	    
	:Example:
	  
	>>> generateGS('GATAGATACA',10)
	{0: 1, 1: 2, 2: 10, 3: 10, 4: 10, 5: 10, 6: 10, 7: 10, 8: 10, 9: 10}

	'''
	listGS = {}
	sub = ""
	for i in range(0, size) :
		listGS[len(sub)] = findSuffixPos(motif[size-i-1],sub,motif,size)
		sub = motif[size-1-i] + sub
	return listGS

def findSuffixPos(bc,suffix, motif,size) : 
	'''
	Effectue la recherche du meilleur suffixe dans le motif de taille size, à partir du caractère bc

	:param motif: Le motif que l'on veut trier
	:param size: la taille du motif
	:param suffix: la sous-chaine que l'on recherche 
	:param bc: le caractère qui n'a pas était reconnu
	:type motif: string
	:type size: int
	:type suffix: string
	:type bc: string
	:return: Le décalage à faire pour retomber sur une repetition de la sous-chaine (entière ou en partie)
	:rtype: int

	:Example:

	>>> findSuffixPos('T',"GAT","GATAGATACA",10)
	3

	'''
	len_suffix = len(suffix)
	for i in range(1,size+1)[::-1] :
		find = True
		for j in range(0,len_suffix) :
				end = i-len_suffix-1+j
				if (end<0 or suffix[j]==motif[end]) :
					pass
				else :
					find = False
		end = i-len_suffix-1
		if find and (end<=0 or motif[end-1]!=bc) :
			return size-i+1

def boyer_moore(motif, chaine) :
	'''
	Algorithme Boyer-Moore.
	    
	:param motif: Le motif qu'on veut retrouver dans la chaine.
	:param chaine_adn: La chaine dans laquelle on fait la recherche de motif.
	:type motif: string
	:type chaine: string
	:return: Le nombre d'occurence du motif et le tableau d'indice des occurences
	    
	:Exemple:
	    
	>>> boyer_moore('AT','ATTTTATATTTA')
	(3, [0, 5, 7])


	... seealso:: brute_force(),kmp()

	'''
	sizeC = len(chaine)
	sizeM = len(motif)
	GS = generateGS(motif,sizeM)
	BC = generateBC(motif,sizeM)
	indice_occ = []
	nb_occ = 0
	i=0
	while i<sizeC-sizeM+1 :
		j = sizeM
		while j>0 and motif[j-1]==chaine[i+j-1] :
			j = j-1
		if j>0 :
			if chaine[i+j-1] not in BC :
				i = i + j
			else :
				BCShift = BC[chaine[i+j-1]]-(sizeM-j)
				GSShift = GS[sizeM-j]
				if BCShift > GSShift :
					i = i + BCShift
				else :
					i = i + GSShift
		else :
			GSshift = GS[sizeM-1]
			nb_occ = nb_occ + 1
			indice_occ.append(i)
			i = i + GSshift
	return nb_occ, indice_occ
=======
    :return: Le tableau BC
    :rtype: dict
    
    
    :Example:
    
    >>> generateBC('GATACA',6)
    {'A': 2, 'C': 1, 'T': 3, 'G': 5}
    
    '''
    listBC = {}
    for i in range(0, size-1) :
        listBC[motif[i]] = size-i-1
    return listBC
        
  
def generateGS(motif,size) :
    '''
    Initialise la table des "good suffix" avec le motif de taille size
    
    :param motif: Le motif que l'on veut trier
	 :param size: la taille du motif
    :type motif: string
	 :type size: int
    :return: Le tableau GS
    :rtype: dict
    
    :Example:
    
    >>> generateGS('GATAGATACA',10)
    {0: 1, 1: 2, 2: 10, 3: 10, 4: 10, 5: 10, 6: 10, 7: 10, 8: 10, 9: 10}

    '''
    listGS = {}
    sub = ""
    for i in range(0, size) :
        listGS[len(sub)] = findSuffixPos(motif[size-i-1],sub,motif,size)
        sub = motif[size-1-i] + sub
    return listGS

def findSuffixPos(bc,suffix, motif,size) : 
    '''
    Effectue la recherche du meilleur suffixe dans le motif de taille size, à partir du caractère bc
    
    :param motif: Le motif que l'on veut trier
	 :param size: la taille du motif
	 :param suffix: la sous-chaine que l'on recherche 
	 :param bc: le caractère qui n'a pas était reconnu
    :type motif: string
	 :type size: int
	 :type suffix: string
	 :type bc: string
    :return: Le décalage à faire pour retomber sur une repetition de la sous-chaine (entière ou en partie)
    :rtype: int
    
    :Example:
    
    >>> findSuffixPos('T',"GAT","GATAGATACA",10)
    3

    '''
    len_suffix = len(suffix)
    for i in range(1,size+1)[::-1] :
        find = True
        for j in range(0,len_suffix) :
            end = i-len_suffix-1+j
            if (end<0 or suffix[j]==motif[end]) :
                pass
            else :
                find = False
        end = i-len_suffix-1
        if find and (end<=0 or motif[end-1]!=bc) :
            return size-i+1

def boyer_moore(motif, chaine) :
    '''
    Algorithme Boyer-Moore.
    
    :param motif: Le motif qu'on veut retrouver dans la chaine.
    :param chaine_adn: La chaine dans laquelle on fait la recherche de motif.
    :type motif: string
    :type chaine: string
    :return: Le nombre d'occurence du motif et le tableau d'indice des occurences
    
    :Exemple:
    
    >>> boyer_moore('AT','ATTTTATATTTA')
    (3, [0, 5, 7])


    .. seealso:: brute_force(),kmp()
    
    '''
    sizeC = len(chaine)
    sizeM = len(motif)
    GS = generateGS(motif,sizeM)
    BC = generateBC(motif,sizeM)
    indice_occ = []
    nb_occ = 0
    i=0
    while i<sizeC-sizeM+1 :
        j = sizeM
        while j>0 and motif[j-1]==chaine[i+j-1] :
            j = j-1
        if j>0 :
            if chaine[i+j-1] not in BC :
                i = i + j
            else :
                BCShift = BC[chaine[i+j-1]]-(sizeM-j)
                GSShift = GS[sizeM-j]
                if BCShift > GSShift :
                    i = i + BCShift
                else :
                    i = i + GSShift
        else :
            GSshift = GS[sizeM-1]
            nb_occ = nb_occ + 1
            indice_occ.append(i)
            i = i + GSshift
    return nb_occ, indice_occ


def kmp(motif,chaine_adn):
    '''
    Knuth-Morris-Prat algorithme.
    
    :param motif: Le motif à trouver dans la chaine_adn
    :param chaine_adn: Chaine de caractère representant un séquence d'AA
    :type motif: string
    :type chaine_adn: string
    :return: nombre d'occurence du motif dans la chaine,
             les indices de ces occurences dans la chaine
    :rtype: int,[int]

    :Exemple:
    
    >>> kmp('ABCAB','ABCA AB ABCAB')
    (1, [8])
    
    
    
    ..seealso:: boyer_moore(),brute_force(), rabin_karp()
    
    '''
    len_chaine_adn = len(chaine_adn)
    len_motif = len(motif)
    #debut du match courant
    m = 0
    #indice du caractere courant ds motif
    i = 0 
    #LA table
    tab = prepare_table_kmp(motif)
    
    occ = 0
    indice_occ = []
    
    while(m+i<len_chaine_adn):
        if (motif[i] == chaine_adn[m + i]):
            if (i == len_motif - 1 ):
                occ +=1
                indice_occ.append(m)
                i = 0
                m += 1
            else :
                i += 1
        else:
            if (tab[i] > -1):
                m += i - tab[i]
                i = tab[i]
            else:
                i = 0
                m += 1
                
    return occ,indice_occ


def prepare_table_kmp(motif):
    '''
    Rempli la table utilisé par l'algorithme KMP
    
    :param motif: Le motif à prétraiter
    :type motif: string
    :return: Une liste résultant du traitement du motif, en conformité avec l'algo KMP
    :rtype: int[]
    
    :Exemple:
    
    
    '''
    len_motif = len(motif)
    #la position a calculé dans le tableau
    pos = 2
    #index dans motif du prochain caractere, de la sous chaine actuelle
    cnd = 0
    
    #le tableau des résultats
    tab = [-2] * len_motif
    tab[0] = -1
    tab[1] = 0
    
    while( pos<len_motif):
        #cas où la sous chaine continue
        if (motif[pos-1] == motif[cnd]):
            cnd +=1
            tab[pos] = cnd
            pos +=1
        #cas ou la souschaine ne continue pas mais on peut revenir en arriere
        elif (cnd>0):
            cnd = tab[cnd]
        #plus de candidat pour une souschaine (cnd==0)
        else:
            tab[pos] = 0
            pos += 1
    
    return tab



if __name__ == "__main__":
    import doctest
    doctest.testmod()
