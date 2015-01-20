#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from . import algorithmes as algo
from .util import * 



adn = "GATACATTCATAGCTATGTGATACAGTATC"    
m = 'GATACA'   


if __name__ == "__main__" :
    
    #print inverse(m)
    #print complement(m,complement_dic)
    #print complement_inverse(m,complement_dic)
    #print cherche_brute_force(m,adn)
    #print cherche_generique(m,adn)
    #print cherche_rabin_karp(m,adn)
    print algo.apprentissage_boyer_moore(m) 
    occ,indice_occ = algo.boyer_moore(m,adn)
    print occ, indice_occ
