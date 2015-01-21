#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 Util module
=============

Contient les fonctions utiles à toutes les fonctions de recherches ou 
à la lecture des fichiers fasta
'''

#marqueur pour savoir si on a déja load random dans generate_fasta
RANDOM = None 

#dictionnaire non exhaustif des complements pour des 
#bases azotees.
#Contient les complements pour A,C,T et G
complement_dic = {'A':'T',
    'T':'A',
    'G':'C',
    'C':'G'}


def inverse(motif):
    '''
    Inverse une chaine de charactere passe en parametre 

    :param motif: une string a inverser
    :type motif: string
    :return: la string resultante des transformations sur motif
    :rtype: string

    :Example:

    >>> inverse('A') 
    'A'
    >>> inverse('AC') 
    'CA'
    >>> inverse('GATACA') 
    'ACATAG'
    
    .. seealso:: complement(), complement_inverse()
    .. warning:: void
    .. note:: Vous pourriez utilisez directement motif[::-1] pour éviter 
              l'overhead de l'appel de fonction mais ça perd en lisibilité
    '''
    return motif[::-1] 
    #slice operator 
    #http://stackoverflow.com/questions/931092/reverse-a-string-in-python

def complement(motif,dic=complement_dic):
    '''
    Remplace chaque lettre par son complément

    :param motif: La string à modifié
    :param [dic]: Un dictionnaire des compléments de chaque lettre du motif.
                Par défaut, prend le dictionnaire fourni @see complement_dic.
                Mais peut être fourni en paramètre.
    :type motif: string
    :type [dic]: dict
    :return: la string resultante des transformations sur motif
    :rtype: string
    
    :Example:
    
    >>> complement('ACTG')
    'TGAC'

    .. seealso:: inverse(), complement_inverse()
    .. warning:: Chaque lettre du motif doit avoir un complément défini dans dic.

    '''
    return "".join([dic[c] for c in motif]) 
    #construit une liste des complements de motif, puis la cast en string
    
def complement_inverse(motif,dic=complement_dic):
    '''
    Remplace chaque lettre du motif par son inverse, puis par le complément 
    du nouveau motif obtenu.
    
    :param motif: La string à modifié.
    :param [dic]: Un dictionnaire des compléments de chaque lettre du motif.
                Par défaut, prend le dictionnaire fourni @see complement_dic.
                Mais peut être fourni en paramètre.
    :type motif: string
    :type [dic]: dict
    :return: La string résultante des transformations sur motif.
    :rtype: string

    :Example: 
    
    >>> complement_inverse('GATACA')
    'TGTATC'

    .. seealso:: inverse(), complement()
    .. warning:: Chaque lettre du motif doit avoir un complément défini dans dic.
    '''
    return complement(inverse(motif),dic)



def open_fasta (filename):
    '''
    Ouvre un fichier au format fasta(pas de fasta multi-séquence), enleve la ligne 
    de commentaire et les caractères de saut de ligne et charge les données dans une string

    :param filename: Le fichier fasta dans lequel on extrait des données.
    :type filename: file
    :return: Une chaine de caractère contenant les données du fichier fasta
    :rtype: string
    
    
    
    .. seealso:: generate_fasta()
    .. warning:: ne traite pas les fichiers fasta multi-séquences
    '''
    with open(filename,'r') as fasta:
        fasta.readline()
        tab = fasta.readlines()

    fasta.closed
    #res = ''
    for x in tab :
        x.strip('\n')
    res = "".join(tab) #tentative d'optimisation, ça n'a pas l'air d'impacter grand chose
    return res

#ATTENTION commence a ramer audela de taille 10^7
def generate_fasta(filename='test.fasta',taille=1000000,desc='''>Un fichier fasta pour tester les algorithmes implementés \n'''):
    '''
    Génére un fichier fasta
    
    :param [filename]: Nom du fichier dans lequel écrire.
    :param [taille]: Nombre de charactère dans la chaine fasta.
                   (en pratique, si cette valeur est >10^7,
                    la fonction commence à être longue)
    :param [desc]: Une description pour la première ligne 
                   du fichier
    :type [filename]: file
    :type [taille]: int
    :type [desc]: string
 
    :Exemple:
    
    >>> generate_fasta()

    >>> generate_fasta('test10millions.fasta',taille=10000000)
    
    
    .. seealso:: open_fasta()
    .. warning:: restreindre l'ordre de grandeur de taille pour
                 ne pas avoir le programme bloqué trop longtemps
    
    '''

    sample = ['A','T','G','C','\n']
    global RANDOM
    if RANDOM is None:
        import random as r
        RANDOM = True
    data = [r.choice(sample) for _ in xrange(taille) ]
    data =  desc + "".join(data)

    with open(filename,"w") as f:
        f.write(data)
        f.closed
    
    return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
