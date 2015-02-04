#!/usr/bin/env python
# -*- coding: utf-8 -*-


import algorithmesT as algoT
import util
import algorithmes as algo
import sys

def cherche_mot_taille_N(chaine_adn,n,func=algo.brute_force,comp=util.complement_dic_adn):
    '''
    >>> dic = (cherche_mot_taille_N('ATATAG', 5 ))
    >>> 
    [('ATATA', 2), ('ATATC', 1), ('CTATA', 1), ('GATAT', 1), ('TATAG', 1), ('TATAT', 2)]
      
    '''
    
    algo_recherche = func 
    len_chaine_adn = len(chaine_adn)
    connu = { }


    for i in xrange(0,len_chaine_adn-n+1):
        motif = chaine_adn[i:i+n]
        if (motif not in connu):
            occ,_ = algoT.cherche_generiqueP(motif,chaine_adn,algo_recherche,comp)
           # occ,_ = func(motif,chaine_adn)
            connu[motif] = occ
            #connu[(util.inverse(motif))] = occ
            #connu[(util.complement(motif,comp))] = occ
            #connu[util.complement_inverse(motif,comp)] = occ
    
            
    return [(a,connu[a]) for a in sorted(connu)]

def cherche_mot_taille_NT(chaine_adn,n,func=algo.brute_force,comp=util.complement_dic_adn):
    '''
    >>> dic = (cherche_mot_taille_NT('ATATAG', 5 ))
    >>> 
    [('ATATA', 2), ('ATATC', 1), ('CTATA', 1), ('GATAT', 1), ('TATAG', 1), ('TATAT', 2)]
      
    '''
    from multiprocessing.pool import Pool
    
    p = Pool(processes=64)

    algo_recherche = func 
    len_chaine_adn = len(chaine_adn)
    connu = { }
    
    
    for i in xrange(0,len_chaine_adn-n+1):
        motif = chaine_adn[i:i+n]
        if (motif not in connu):
            res = p.apply_async(algo.cherche_generique,(motif,chaine_adn,algo_recherche,comp))
            #occ,_ = algo.cherche_generique(motif,chaine_adn,algo_recherche,comp)
            occ,_ = res.get()
            connu[motif] = occ
            connu[(util.inverse(motif))] = occ
            connu[(util.complement(motif,comp))] = occ
            connu[util.complement_inverse(motif,comp)] = occ
    
            
    return [(a,connu[a]) for a in sorted(connu)]


def cherche_mot_taille_N_essai(chaine_adn,n):
    '''
    Calcule le nombre d'occurence de tous les mots de taille n présent dans chaine_adn.
    
    :param chaine_adn: La chaine dans laquelle on recherche les mots.
    :param n: La taille des mots que l'on souhaite chercher.
    :type chaine_adn: string
    :type n: int
    :return: Une liste de tuple contenant:
             -Le mot trouvé
             -Son nombre d'occurence.
    :rtype: [(string,int)]
    
    :Exemple:
    
    >>> sorted(cherche_mot_taille_N_essai('AGCTCCATC',2))
    [('AG', 1), ('AT', 1), ('CA', 1), ('CC', 1), ('CT', 1), ('GC', 1), ('TC', 2)]
   
 
    ..seealso:: 
    ..warning:: Le nombre de mot possible est (nombre_lettre_dans_lalphabet**n) qui est ici
                4**n. Le nombre de  mot possible augmente de manière exponentielle.
    ..performance:: d'après: https://wiki.python.org/moin/TimeComplexity
                    Soit M la taille de chaine_adn, N la taille des mots que l'on cherche,
                    P le nombre de mot partageant un hash dans le dictionnaire. 
                    (ici P=4**N dans le pire des cas, 1 le plus souvent)
                    O(1) + O(M-N) * (O(N) + (O(P)) + (O(4**N)) ?
    '''
    len_chaine_adn = len(chaine_adn) #O(1)
    connu = {} 
    motif = ''
    
    
    for i in xrange(0,len_chaine_adn-n+1): #O(M-N)
        motif = chaine_adn[i:i+n] #O(N) 
            if motif in connu:
            connu[motif] += 1  #O(1) en pratique, #O(P) dans le pire des cas.
        else:
            connu[motif] = 1 #O(1) en pratique, #O(P) dans le pire des cas.
    return [(a,connu[a]) for a in connu] #O(4**N) dans le pire des cas.

def cherche_mot_taille_N_essai2(chaine_adn,n):
    '''
    Calcule le nombre d'occurence de tous les mots de taille n présent dans chaine_adn.
    
    :param chaine_adn: La chaine dans laquelle on recherche les mots.
    :param n: La taille des mots que l'on souhaite chercher.
    :type chaine_adn: string
    :type n: int
    :return: Une liste de tuple contenant:
             -Le mot trouvé
             -Son nombre d'occurence.
    :rtype: [(string,int)]
    
    :Exemple:
    
    >>> sorted(cherche_mot_taille_N_essai('AGCTCCATC',2))
    [('AG', 1), ('AT', 1), ('CA', 1), ('CC', 1), ('CT', 1), ('GC', 1), ('TC', 2)]
   
 
    ..seealso:: 
    ..warning:: Le nombre de mot possible est (nombre_lettre_dans_lalphabet**n) qui est ici
                4**n. Le nombre de  mot possible augmente de manière exponentielle.
    ..performance:: d'après: https://wiki.python.org/moin/TimeComplexity
                    Soit M la taille de chaine_adn, N la taille des mots que l'on cherche,
                    P le nombre de mot partageant un hash dans le dictionnaire. 
                    (ici P=4**N dans le pire des cas, 1 le plus souvent)
                    O(1) + O(M-N) * (O(N) + (O(P)) + (O(4**N)) ?
    '''
    len_chaine_adn = len(chaine_adn) #O(1)
    connu = {} 
    motif = ''
    
    
    for i in xrange(0,len_chaine_adn-n+1): #O(M-N)
        motif = chaine_adn[i:i+n] #O(N) 
        try :
            connu[motif] += 1  #O(1) en pratique, #O(P) dans le pire des cas.
        except KeyError:
            connu[motif] = 1 #O(1) en pratique, #O(P) dans le pire des cas.
    return [(a,connu[a]) for a in connu] #O(4**N) dans le pire des cas.




def cherche_mot_taille_N_essai_counter(chaine_adn,n):
    from collections import Counter
    len_chaine_adn = len(chaine_adn)
    connu = Counter()
    motif = ''
    
    for i in xrange(0,len_chaine_adn-n+1):
        motif = chaine_adn[i:i+n]
        connu[motif] += 1 
    #from operator import itemgetter
    return connu.items()


if __name__ == '__main__':

    if (len(sys.argv)<2):
        import doctest
        doctest.testmod()
    else:

        #f = util.open_fasta("test10millions.fasta")
        f = util.open_fasta("../data/chromosome13_NT_009952.14.fasta")
        #l = cherche_mot_taille_N(f,int(sys.argv[1]),comp=util.complement_dic_arn)
        l2 = cherche_mot_taille_N_essai(f,int(sys.argv[1]))
        print l2



 
