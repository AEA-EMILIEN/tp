import numpy as np

complement_dic_arn_2 = {'A':'U',
    'U':('A','G'),
    'G':('C','U'),
    'C':'G'}
	 
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
	for cpt_u in range(1,len_u+1) :
		for cpt_v in range(1,len_v+1) :
			sub = matx[cpt_u-1,cpt_v-1] + Sub(u[cpt_u-1],v[cpt_v-1]) 
			dele = matx[cpt_u-1,cpt_v] + Del
			ins = matx[cpt_u,cpt_v-1] + Ins
			matx[cpt_u,cpt_v] = max(sub, ins, dele, 0)
			if matx[cpt_u,cpt_v] > max_val :
				max_val = matx[cpt_u,cpt_v]
				max_ind = (cpt_u,cpt_v)
	return max_val, max_ind, matx



