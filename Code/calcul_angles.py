import math
import numpy as np

def calcAngles(mimoB):
	"""[y][x]"""
	ls = mimoB[0]
	le = mimoB[2]
	lw = mimoB[4]
	rs = mimoB[1]
	re = mimoB[3]
	rw = mimoB[5]
	ls = np.array(ls)
	le = np.array(le)
	lw = np.array(lw)
	rs = np.array(rs)
	re = np.array(re)
	rw = np.array(rw)
	mimoPos = []

	
	#------Costat esquerra-----
	#print("----costat esquerra---")
	#-------colze-------
	b = np.linalg.norm(ls-le)
	#print("costat b: " + str(b))

	a = np.linalg.norm(le-lw)
	#print("costat a: " + str(a))

	c = np.linalg.norm(lw-ls)
	#print("costat c: " + str(c))

	alpha = ((b**2) + (c**2) - (a**2))/(2*b*c)
	alpha = math.acos(alpha)
	alpha = math.degrees(alpha) #convertim de radiants a graus
	#print("alpha : " + str(alpha) + " servo 6 ombro 2")

	beta = ((a**2) + (c**2) - (b**2))/(2*a*c)
	beta = math.acos(beta)
	beta = math.degrees(beta) #convertim de radiants a graus
	#print("beta : " + str(beta) )

	gamma = 180-alpha-beta
	#print("gamma : " + str(gamma) + " servo 4 colze")
	colze = gamma
	
	#--------ombro------- 
	b = np.linalg.norm(rs-ls)
	#print("costat b: " + str(b))

	a = np.linalg.norm(ls-le)
	#print("costat a: " + str(a))

	c = np.linalg.norm(le-rs)
	#print("costat c: " + str(c))

	alpha = ((b**2) + (c**2) - (a**2))/(2*b*c)
	alpha = math.acos(alpha)
	alpha = math.degrees(alpha) #convertim de radiants a graus
	#print("alpha : " + str(alpha) + " servo 6 ombro 2")

	beta = ((a**2) + (c**2) - (b**2))/(2*a*c)
	beta = math.acos(beta)
	beta = math.degrees(beta) #convertim de radiants a graus
	#print("beta : " + str(beta) )

	gamma = 180-alpha-beta
	#print("gamma : " + str(gamma) + " servo 4 colze")
	if le[0] < ls[0]:
		ombro = gamma - 90
		ombro = 180 - ombro
		cas0 = False
	else:
		ombro = gamma - 90
		cas0 = True
	
		
	#ombro, colze
	mimoPos.append(ombro)
	mimoPos.append(colze)
	
	#-------Costat dret-------
	#print("\n----costat dret---")
	#-------colze-------
	b = np.linalg.norm(re-rs)
	#print("costat b: " + str(b))

	a = np.linalg.norm(rs-rw)
	#print("costat a: " + str(a))

	c = np.linalg.norm(rw-re)
	#print("costat c: " + str(c))

	alpha = ((b**2) + (c**2) - (a**2))/(2*b*c)
	alpha = math.acos(alpha)
	alpha = math.degrees(alpha) #convertim de radiants a graus
	#print("alpha : " + str(alpha) + " servo 3 colze")

	beta = ((a**2) + (c**2) - (b**2))/(2*a*c)
	beta = math.acos(beta)
	beta = math.degrees(beta) #convertim de radiants a graus
	#print("beta : " + str(beta) )

	gamma = 180-alpha-beta
	#print("gamma : " + str(gamma) + " servo 5 hombro 2")
	colze = alpha
	
	#-------ombro-------
	b = np.linalg.norm(rs-ls)
	#print("costat b: " + str(b))

	a = np.linalg.norm(ls-re)
	#print("costat a: " + str(a))

	c = np.linalg.norm(re-rs)
	#print("costat c: " + str(c))

	alpha = ((b**2) + (c**2) - (a**2))/(2*b*c)
	alpha = math.acos(alpha)
	alpha = math.degrees(alpha) #convertim de radiants a graus
	#print("alpha : " + str(alpha) + " servo 3 colze")

	beta = ((a**2) + (c**2) - (b**2))/(2*a*c)
	beta = math.acos(beta)
	beta = math.degrees(beta) #convertim de radiants a graus
	#print("beta : " + str(beta) )

	gamma = 180-alpha-beta
	#print("gamma : " + str(gamma) + " servo 5 hombro 2")
	if re[0] < rs[0]:
		ombro = alpha - 90
		ombro = 180 - ombro
		cas1 = False		
	else:
		ombro = alpha - 90
		cas1 = True
	
	#ombro, colze
	mimoPos.append(ombro)
	mimoPos.append(colze)

	#------calcul estat-------
	if cas0 == False and cas1 == False:
		estat = 0
	if cas0 == True and cas1 == True:
		estat = 1
	if cas0 == True and cas1 == False:
		estat = 2
	if cas0 == False and cas1 == True:
		estat = 3

	#print("cas0 = " + str(cas0) + "cas1 = " + str(cas1))
	mimoPos.append(estat)

	#-------print result-------
	print("ombro esquerra: " + str(mimoPos[0]) + "\n")
	print("colze esquerra: " + str(mimoPos[1]) + "\n")
	print("ombro dret: " + str(mimoPos[2]) + "\n")
	print("colze dret: " + str(mimoPos[3]) + "\n")
	print("estat: " + str(mimoPos[4]) + "\n")
	
	return mimoPos

"""
if __name__ == "__main__":
	mimoPos = []
	print ("--pose bracos adalt--")
	ls = [199, 186]
	rs = [193, 121]
	le = [176, 223]
	re = [164, 89]
	lw = [138, 226]
	rw = [125, 95]
	mimoPos.append(ls)
	mimoPos.append(rs)
	mimoPos.append(le)
	mimoPos.append(re)
	mimoPos.append(lw)
	mimoPos.append(rw)
	print("mimoPos: " + str(mimoPos))
	calcAngles(mimoPos)

	print ("\n--pose bracos abaix--")
	mimoPos = []
	ls = [45, 216]
	rs = [45, 111]
	le = [118, 251]
	re = [130, 72]
	lw = [191, 264]
	rw = [217, 66]
	mimoPos.append(ls)
	mimoPos.append(rs)
	mimoPos.append(le)
	mimoPos.append(re)
	mimoPos.append(lw)
	mimoPos.append(rw)
	print("mimoPos: " + str(mimoPos))
	calcAngles(mimoPos)

	print ("\n--pose dret adalt esquerra abaix--")
	mimoPos = []
	ls = [45, 216]
	rs = [193, 121]
	le = [118, 251]
	re = [164, 89]
	lw = [191, 264]
	rw = [125, 95]
	mimoPos.append(ls)
	mimoPos.append(rs)
	mimoPos.append(le)
	mimoPos.append(re)
	mimoPos.append(lw)
	mimoPos.append(rw)
	print("mimoPos: " + str(mimoPos))
	calcAngles(mimoPos)

	print ("\n--pose dret abaix esquerra adalt--")
	mimoPos = []
	rs = [45, 111]
	re = [130, 72]
	rw = [217, 66]
	ls = [199, 186]
	le = [176, 223]
	lw = [138, 226]
	mimoPos.append(ls)
	mimoPos.append(rs)
	mimoPos.append(le)
	mimoPos.append(re)
	mimoPos.append(lw)
	mimoPos.append(rw)
	print("mimoPos: " + str(mimoPos))
	calcAngles(mimoPos)"""