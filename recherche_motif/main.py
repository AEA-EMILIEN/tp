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
    algos = {"boyer-moore":algo.boyer_moore,
             "brute_force":algo.brute_force} 
    algo_choisi = algo.brute_force
    #fichier fasta à utiliser
    inputfile = 'test10millions.fasta'
    #si fichier fasta non spécifié
    outputfile = '' 
    #si output file spécifié, nombre de char à généré
    taille = 1000000
   
    motif = "GATACA"
    chaine_adn = '' 

    #chaine d'usage a afficher qd l'utilisateur se trompe/demande l'aide
    usage = sys.argv[0]+''' -l : Affiche la liste des algos utilisables \n'''+sys.argv[0]+''' -i <inputfile> -o <outputfile> -a <algorithme> -m <motif>'''
   
    
    ###################################################
    #traitement des arguments d'appel du script#
    ###################################################
   
    
    try:
        opts, args = getopt.getopt(argv,"lhi:o:a:t:m:",["ifile=","ofile=","listeAlgo=","algo=","motif=","taille="])
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
    ####################################################
    #fin du traitement des arguments d'appel du script#
    ###################################################
    if (outputfile!=''):
        util.generate_fasta(outputfile,taille)
        inputfile=outputfile
    chaine_adn = util.open_fasta(inputfile)
    
        
    occ,indice_occ = algo.cherche_generique(motif,chaine_adn,algo_choisi)
    print occ,indice_occ    
if __name__ == "__main__":
    main(sys.argv[1:])
