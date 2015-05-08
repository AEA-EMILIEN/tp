#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Module dotplot
==============

	Crée un dotplot à partir d'un algorithme de recherche de motif à n taille dans une chaine
'''

import tmp_juR as tmp
import matplotlib.pyplot as plt
import util

def generate_plot(chaine,n) :
	'''
	génère un dot plot sur la répétition de motif d'après l'algo tmp_juR pour les motif de taille n	
	'''
	v1 = []
	v2 = []
	dic = tmp.cherche_mot_taille_N_essai(chaine,n)
	for d in dic :
		for p1 in dic[d][1] :
			for p2 in dic[d][1] :
				v1.append(p1)
				v2.append(p2)
	plt.plot(v1,v2,'b.')
	plt.xlabel(chaine)
	plt.ylabel(chaine)
	plt.title('Dotplot'+`n`)
	plt.show()

if __name__ == "__main__" :
	fasta = util.open_fasta('../data/chromosome13_NT_009952.14.fasta')
	generate_plot(fasta,5)
