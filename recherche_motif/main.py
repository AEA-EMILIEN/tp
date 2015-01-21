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
    #les algos que l'utilisateur peut demander d'utiliser
    algos = ["boyer_moore","brute_force"] 
    algo_choisi = "brute_force"
    #fichier fasta à utiliser
    inputfile = 'test10millions.fasta'
    #si fichier fasta non spécifié
    outputfile = 'out.fasta' 
    #si output file spécifié, nombre de char à généré
    taille = 1000000
    
   

    #chaine d'usage a afficher qd l'utilisateur se trompe/demande l'aide
    usage = sys.argv[0]+''' -l : Affiche la liste des algos utilisables \n'''+sys.argv[0]+''' -i <inputfile> -o <outputfile> -a <algorithme>'''
    try:
        opts, args = getopt.getopt(argv,"lhi:o:a:t:",["ifile=","ofile=","listeAlgo=","algo="])
    except getopt.GetoptError:
        print usage
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print usage
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-l", "--listeAlgo"):
            for a in algos:
                print a
            sys.exit(2)
        elif opt in ("-a","--algo"):
            if arg not in algos:
                print "erreur d'algorithme, -l pour voir la liste des algorithmes implémentés"
            else:
                algo_choisi = arg
        
        
if __name__ == "__main__":
    main(sys.argv[1:])
