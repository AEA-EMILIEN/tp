#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,getopt

import algorithmes as algo
import util 


adn = "GATACATTCATAGCTATGTGATACAGTATC"    
m = 'GATACA'   


'''
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
'''
def main(argv):
    algos = ["boyer_moore","brute_force"]
    inputfile = ''
    taille = 1000000
    outputfile = ''
   
    try:
        opts, args = getopt.getopt(argv,"lhi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print sys.argv[0]+' -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print sys.argv[0]+' -l : Affiche la liste des algos utilisables'  
            print sys.argv[0]+' -i <inputfile> -o <outputfile> -a <algorithme>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-l", "--listeAlgo"):
            for a in algos:
                print a

if __name__ == "__main__":
    main(sys.argv[1:])
