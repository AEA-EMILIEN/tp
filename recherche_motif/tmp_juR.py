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
            #occ,_ = algo.cherche_generique(motif,chaine_adn,algo_recherche,comp)
            occ,_ = func(motif,chaine_adn)
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
    len_chaine_adn = len(chaine_adn)
    connu = {}
    motif = ''
    
    for i in xrange(0,len_chaine_adn-n+1):
        motif = chaine_adn[i:i+n]
        
        if motif in connu:
            connu[motif] += 1 
        else:
            connu[motif] = 1
    #from operator import itemgetter
    return [(a,connu[a]) for a in connu]#sorted(connu,key=itemgetter(0))]

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
        f = util.open_fasta("test10millions.fasta")
        #f = util.open_fasta("../data/chromosome13_NT_009952.14.fasta")
        #l = cherche_mot_taille_N(f,int(sys.argv[1]),comp=util.complement_dic_arn)
        l2 = cherche_mot_taille_N_essai(f,int(sys.argv[1]))
        #print l2


 
