#!/usr/bin/env python
# -*- coding: utf-8 -*-
from util import *
import algorithmes as algo

def test(motif,chaine_adn,func):
    #return func(motif,chaine_adn)
    _,_ = func('AA','AAAAAAAAAAAA')
    return
if __name__ == "__main__":
    import timeit
    
    
    file = ["'../data/chromosome13_NT_009952.14.fasta'","'test.fasta'","'test10millions.fasta'"]
    motif = ['"AAA"',"'GATACA'","'GATACAGATACAGACACACAC'"]
    
    func = ["brute_force","kmp","boyer_moore"]
    
    params = [(m,algo,filename) for filename in file for algo in func for m in motif ]

    for elem in params:
        param_func = elem[0]+",f,"+elem[1]
        param_setup = ("from __main__ import test;"
                   "from algorithmes import "+elem[1]+";"
                   "from util import open_fasta;"
                   "f = open_fasta("+elem[2]+");")
        print elem,(timeit.timeit("test("+param_func+")", setup=param_setup))

