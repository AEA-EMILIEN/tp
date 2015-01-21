#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import algorithmes as algo
import util 


adn = "GATACATTCATAGCTATGTGATACAGTATC"    
m = 'GATACA'   


if __name__ == "__main__" :
    
    narg = len(sys.argv) #nombre d'argument sur la ligne de commande
    if (narg<2): #0arg supplementaire
        adn = util.open_fasta('test.fasta')
        occ = algo.brute_force(m,adn)
        print occ
    if (narg==2) :
        filename = sys.argv[1]
        adn = util.open_fasta(filename)
        occ = algo.cherche_generique(m,adn)
        print occ
