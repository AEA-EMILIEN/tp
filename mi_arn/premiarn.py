import numpy as np

def Sub(x1,x2) :
	if x1 == x2 :
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
	Del = -2
	Ins = -2
	for cpt_u in range(1,len_u) :
		for cpt_v in range(1,len_v) :
			sub = matx[cpt_u-1,cpt_v-1] + Sub(u[cpt_u-1],v[cpt_v-1]) 
			dele = matx[cpt_u-1,cpt_v] + Del
			ins = matx[cpt_u,cpt_v-1] + Ins
			matx[cpt_u,cpt_v] = max(sub, ins, dele, 0)
			if matx[cpt_u,cpt_v] > max_val :
				max_val = matx[cpt_u,cpt_v]
				max_ind = (cpt_u,cpt_v)
	return max_val, max_ind, matx



