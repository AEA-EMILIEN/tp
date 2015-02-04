#!/usr/bin/env python
# -*- coding: utf-8 -*-

import algorithmes as algo
import numpy as np 

''' 
	recherche dans fasta toutes les occurences de mots de taille n
	retourne le tableau des occurences
'''

def rechercheN (fasta,n) :
	size = len(fasta)
	matrice = np.empty(size)
	matrice.fill(np.nan)
	i = 0
	old_i = 0
	occ = np.zeros(size)
	while (i <= size-n) :
		#print i
		#lance la recherche et met à 1 dans la matrice ce que l'on a déjà compté
		occ_alt,tab = algo.cherche_generique(fasta[i:i+n],fasta)
		#print "nb occurence de ",i," est ",occ_alt
		#print tab
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
	



