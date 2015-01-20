#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 Util module
=============

Contient les fonctions utiles à toutes les fonctions de recherches ou 
à la lecture des fichiers fasta
'''


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
    
    :Example:
    
    >>> open_fasta('test.fasta')
    'AATTCCGG'
    
    .. seealso::
    .. warning:: ne traite pas les fichiers fasta multi-séquences
    '''
    with open(filename,'r') as fasta:
        fasta.readline()
        tab = fasta.readlines()

    fasta.closed
    res=""
    for x in tab :
        res+=x.strip('\n')
    return res

def generate_fasta(filename):
    '''
    '''



if __name__ == "__main__":
    import doctest
    doctest.testmod()
