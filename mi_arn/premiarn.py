import numpy as np

# Dictionnaire utilisé pour les ARNs
complement_dic_arn_2 = {'A':'U',
    'U':('A','G'),
    'G':('C','U'),
    'C':'G'}
	 
# Dictionnaire utilisé pour l'ADN
complement_dic_adn = {'A':'T',
    'T':'A',
    'G':'C',
    'C':'G'}


def Sub(m1, m2,dic=complement_dic_adn) :
	comp = dic[m1]
	if len(comp)>1 :
		for c in comp :
			if c == m2 :
				return 2
	else :
		if comp == m2 :
			return 2
	return -1


def N_W(u,v) :
	'''
		Needleman-Wunsch .... resultat de l'hybridation de u et v 
	'''
	len_u = len(u)
	len_v = len(v)
	matx = np.zeros((len_u+1,len_v+1))
	max_val = -1
	max_ind = (-1,-1)
	Del = -1
	Ins = -1
	for app_u in range(1,len_u+1) :
		for app_v in range(1,len_v+1) :
			sub = matx[app_u-1,app_v-1] + Sub(u[app_u-1],v[app_v-1]) 
			dele = matx[app_u-1,app_v] + Del
			ins = matx[app_u,app_v-1] + Ins
			matx[app_u,app_v] = max(sub, ins, dele, 0)
			if matx[app_u,app_v] > max_val :
				max_val = matx[app_u,app_v]
				max_ind = (app_u,app_v)
	return max_val, max_ind, matx


def recherche_premiarn(chr, size=70) :
	'''
		Fait la recherche de premiarn uniquement de taille 70.
		Sinon il faudrait le faire de 70 à 100
		Retourne la liste des premiarns trouvés
	'''
	max_val = -1
	max_ind = (-1,-1)
	matx = []
	p = -1
	l = []
	for i in range(len(chr)-size) :
		part = chr[i:i+size]
		for j in range(23) :
			max_p, max_ind_p, matx_p = N_W(part[0:24+j], part[24+j+1:size])
			# teste où se situe la grande boucle de la portion du chromosme en cherchant la meilleur complémentarité
			
			if (max_p > max_val) and (test(max_ind_p,matx_p)) :
			# si on obtient un meilleur score qu'auparavant et qu'il correspond au critère d'un premiARN
				p = i
				max_val = max_p
				max_ind = max_ind_p
				matx = matx_p
		if (max_val != -1) :
			l.append(chr[p:p+size])
	return l

def test(max_ind, matx) :
	'''
		Fait la remonter de la matrice obtenue par N_W pour voir si c'est bien un premiARN ou non
	'''
	cpt_app = 0
	app_u = 0
	app_v = 0
	cpt_del = 0
	cpt_ins = 0
	gde_boucle = false
	gde_b_courante = false

	tmp = max_ind
	
	while (tmp[1] != 0 or tmp[2] != 0) :
		try :
			maxi = max(matx[tmp[1],tmp[2]-1], matx[tmp[1]-1,tmp[2]], matx[tmp[1]-1,tmp[2]-1])
			
			if maxi == matx[tmp[1]-1,tmp[2]-1] : # sub
				if  matx[tmp[1],tmp[2]] - matx[tmp[1]-1,tmp[2]-1] == 2 : # MATCH
					cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante = match(cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante)
				else : #MISMATCH
					cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante = ins(cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante)
					cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante = dele(cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante)
			elif maxi == matx[tmp[1]-1,tmp[2]] : #ins
				cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante = ins(cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante)
		
			elif maxi == matx[tmp[1],tmp[2]-1] : #del
				cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante = dele(cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante)
		
		except MyException :
			return False
	return True

class MyException(Exception):
	pass

def dele( cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante) :
	if app_v >= 3 :
		cpt_del += 1
		app_v = 0
		return cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante
	else :
		if cpt_del == 0 :
			raise MyException()
		else : 
			if cpt_del < 3 :
				cpt_del += 1
				return cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante
			else : 
				if not gde_boucle :
					if not gde_b_courante :
						raise MyException()
					else :
						cpt_del += 1
				else : 
					if cpt_app < 24 :
						raise MyException()
					else :
						gde_boucle = True
						gde_b_courante = True
						cpt_del += 1
						return cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante

def ins( cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante) :
	if app_u >= 3 :
		cpt_ins += 1
		app_u = 0
		return cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante
	else :
		if cpt_ins == 0 :
			raise MyException()
		else : 
			if cpt_ins < 3 :
				cpt_ins += 1
				return cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante
			else : 
				if not gde_boucle :
					if not gde_b_courante :
						raise MyException()
					else :
						cpt_ins += 1
				else : 
					if cpt_app < 24 :
						raise MyException()
					else :
						gde_boucle = True
						gde_b_courante = True
						cpt_ins += 1
						return cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante

def match (cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante) :
	if gde_b_courante :
		gde_b_courante = False
	if app_u>0 and app_v>0 :
		app_u += 1
		app_v += 1
		cpt_app += 1
	elif app_u>0 and app_v==0 :
		cpt_del = 0
		app_u += 1
		app_v =+ 1
		cpt_app += 1
	elif app_u==0 and app_v>0 :
		cpt_ins = 0
		app_u += 1
		app_v += 1
	else :
		cpt_ins = 0
		cpt_del = 0
		app_u += 1
		app_v += 1
	return cpt_app,app_u,app_v,cpt_ins,cpt_del,gde_boucle,gde_b_courante
