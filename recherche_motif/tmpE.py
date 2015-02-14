#!/usr/bin/env python
# -*- coding: utf-8 -*-

import algorithmes as algo
import numpy as np 
import util

''' 
	recherche dans fasta toutes les occurences de mots de taille n
	retourne le tableau des occurences
'''

def rechercheN (fasta,n,dic = util.complement_dic_adn) :
	size = len(fasta)
	matrice = np.empty(size)
	matrice.fill(np.nan)
	i = 0
	old_i = 0
	occ = np.zeros(size)
	while (i <= size-n) :
		#lance la recherche et met à 1 dans la matrice ce que l'on a déjà compté
		occ_alt,tab = algo.cherche_generiqueT(fasta[i:i+n],fasta,comp=dic)
		for t in tab :
			matrice[t] = 1
		#print matrice
		occ[i] = occ_alt
		old_i = i
		i = first(matrice,old_i+1,size-n+1)
		
	return occ

def first (matrice,indice,end) :
	for i in range(indice,end):
		if np.isnan(matrice[i]) :
			return i
	return end
	
if __name__ == "__main__" :
	fasta = util.open_fasta("test10millions.fasta")
	occ = rechercheN(fasta,4)

