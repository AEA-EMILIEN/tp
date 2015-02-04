#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,getopt

import algorithmes as algo
import util 
import algorithmesT as algoT


def main(argv):
    #les algos que l'utilisateur peut demander d'utiliser
    algos = {"boyer_moore":algo.boyer_moore,
             "brute_force":algo.brute_force,
	     "rabin_karp":algo.rabin_karp,
             "kmp":algo.kmp} 
    
    algo_choisi = algo.brute_force
    
    #les complements a utiliser, en fonction qu'on lit de l'ARN, de l'ADN
    comp = {"adn":util.complement_dic_adn,
            "arn":util.complement_dic_arn}
    
    comp_choisi = comp['arn']
    
    #fichier fasta à utiliser
    inputfile = '../data/chromosome13_NT_009952.14.fasta'
    #si fichier fasta non spécifié
    outputfile = '' 
    #si output file spécifié, nombre de char à généré
    taille = 1000000
    #Si spécifié impromme les occurences
    print_occ = False

    motif = "GAUACA"
    chaine_adn = '' 

    #chaine d'usage a afficher qd l'utilisateur se trompe/demande l'aide
    usage = sys.argv[0]+''' -l : Affiche la liste des algos utilisables \n'''+sys.argv[0]+''' -i <inputfile> -o <outputfile> -a <algorithme> -m <motif> -p <print occurence>'''
   
    
    ###################################################
    #traitement des arguments d'appel du script#
    ###################################################
   
    
    try:
        opts, args = getopt.getopt(argv,"lhi:o:a:t:m:c:",["ifile=","ofile=","listeAlgo=","algo=","motif=","taille=","complement_dic="])
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
                algo_choisi = algos[arg]
        elif opt in ("-m","--motif"):
            motif = arg
        elif opt in ("-t","--taille"):
            taille = int(arg)
        elif opt in ("-c","--complement_dic"):
            comp_choisi = comp.get(arg,util.complement_dic_adn)
        elif opt in ("-p"):
            print_occ=True
    ####################################################
    #fin du traitement des arguments d'appel du script#
    ###################################################
    if (outputfile!=''):
        util.generate_fasta(outputfile,taille)
        inputfile=outputfile
    chaine_adn = util.open_fasta(inputfile)
    
    occ,indice_occ = algo.cherche_generique(motif,chaine_adn,algo_choisi,comp_choisi)
    if print_occ :    
        print occ,indice_occ
    else:
        print occ
if __name__ == "__main__":
    main(sys.argv[1:])
