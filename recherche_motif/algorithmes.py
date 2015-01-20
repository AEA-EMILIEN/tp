#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .util import *



def brute_force(motif,chaine_adn):
    '''
    algorithme de recherche de motif en brute force
    @param string,string , le motif et la chaine dans laquelle chercher
    '''
    occ = 0 
    for c1 in xrange(0,len(chaine_adn)-len(motif)+1):  
        for c2 in xrange(0,len(motif)):
            if (chaine_adn[c1+c2]!=motif[c2]):
                break
            else :
                if (c2==len(motif)-1):
                    occ+=1
    return occ





def hachage_rabin_karp(motif):
	
	#effectue un hachage defini par l'algorithme de rabin-karp sur un motif passe en parametre
	
	base_azotee = { 'A':1 , 'C':2 , 'G':3 , 'T':4 }
	return sum([base_azotee[c] for c in motif])	
	
def rabin_karp(motif,chaine_adn):
	
	#recherche de motif avec l'algorithme de rabin_karp
	#@param string,string le motif et la chaine dans laquelle on cherche ce motif
	
	occ = 0
	hachage_motif = hachage_rabin_karp(motif)
	chaine_hachage = range(0,len(chaine_adn)+1)
	
	for i in xrange(0,len(chaine_adn)-len(motif)+1):
		chaine_hachage[i] = hachage_rabin_karp(chaine_adn[i:len(motif)])
		if (chaine_hachage[i]==hachage_motif):
			occ+=1
	
	return occ,chaine_hachage 

def cherche_generique(motif,chaine_adn,func=brute_force):
    '''
    fait une recherche de motif,inverse,complement,complement-inverse
    dans une chaine avec une fonction passe en parametre.
    si aucune fonction n'est precise, brute force est utilise
    '''
    occ_motif = func(motif,chaine_adn)
    occ_inv   = func(inverse(motif),chaine_adn)
    occ_comp  = func(complement(motif),chaine_adn)
    occ_comp_inv = func(complement_inverse(motif),chaine_adn)
    
    return occ_motif + occ_inv + occ_comp + occ_comp_inv
    
def boyer_moore(motif, chaine_adn) :
	dico = apprentissage_boyer_moore(motif)
	cpt = len(motif)-1
	occ = 0
	indice_occ = []
	while (cpt < len(chaine_adn)) :
		print cpt
		boolean, cpt = compare_boyer_moore(motif, chaine_adn, cpt) 
		if (boolean) :
			print cpt
			occ += 1
			indice_occ.append(cpt)
			cpt += len(motif)
		else :
			if (chaine_adn[cpt] in dico) :
				cpt += dico[chaine_adn[cpt]]
			else :
				cpt += len(motif)
	return occ,indice_occ


def apprentissage_boyer_moore(motif) : 
	list_key = []
	list_value = []
	fitom = inverse(motif) 
	for m in fitom[1:]: # tester avec ou sans slice operator
		if (m not in list_key and m != fitom[0]):
			list_key.append(m)
			list_value.append(fitom.index(m))
	return dict(zip(list_key, list_value))		

def compare_boyer_moore(motif, chaine_adn, cpt) :
	i = 0
	size = len(motif)-1
	while (i <= size) :
		print motif[size-i], chaine_adn[cpt-i]
		if (motif[size-i] == chaine_adn[cpt-i]) :
			i += 1
		else :
			return False,cpt-i
	return True,cpt-i+1
