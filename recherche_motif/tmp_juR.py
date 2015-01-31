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
            occ,_ = algoT.cherche_generiqueT(motif,chaine_adn,algo_recherche,comp)
            connu[motif] = occ
            connu[(util.inverse(motif))] = occ
            connu[(util.complement(motif,comp))] = occ
            connu[util.complement_inverse(motif,comp)] = occ
    
            
    return [(a,connu[a]) for a in sorted(connu)]

def cherche_mot_taille_NT(chaine_adn,n,func=algo.brute_force,comp=util.complement_dic_adn):
    '''
    >>> dic = (cherche_mot_taille_N('ATATAG', 5 ))
    >>> 
    [('ATATA', 2), ('ATATC', 1), ('CTATA', 1), ('GATAT', 1), ('TATAG', 1), ('TATAT', 2)]
      
    '''
    from multiprocessing.pool import ThreadPool
    
    p = ThreadPool(processes=4)

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


def cherche_mot_N_essai(chaine_adn,n,func=algo.brute_force,comp=util.complement_dic_adn):
    
    
    len_chaine_adn = len(chaine_adn)

if __name__ == '__main__':

    if (len(sys.argv)<2):
        import doctest
        doctest.testmod()
    else:
        f = util.open_fasta("test.fasta")
        l = cherche_mot_taille_N(f,int(sys.argv[1]))
        print l


 
