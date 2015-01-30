import algorithmes as algo
import util



def cherche_mot_taille_N(chaine_adn,n,func=algo.brute_force,comp=util.complement_dic_adn):
    '''
    >>> dic = (cherche_mot_taille_N('ATATAG', 5 ))
    >>> [(a,dic[a]) for a in sorted(dic)]
    [('ATATA', 2), ('ATATC', 1), ('CTATA', 1), ('GATAT', 1), ('TATAG', 1), ('TATAT', 2)]
      
    '''
    
    len_chaine_adn = len(chaine_adn)
    connu = { }


    for i in xrange(0,len_chaine_adn-n+1):
        motif = chaine_adn[i:i+n]
        if (motif not in connu):
            occ,_ = algo.cherche_generique(motif,chaine_adn,func,comp)
            connu[motif] = occ
            connu[(util.inverse(motif))] = occ
            connu[(util.complement(motif,comp))] = occ
            connu[util.complement_inverse(motif,comp)] = occ
    
    return connu


if __name__ == '__main__':
    import doctest
    doctest.testmod()



 
