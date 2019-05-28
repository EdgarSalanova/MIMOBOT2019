def convert(s):
	s = s.replace("[","")
	s = s.replace("]","")
	#print("str = " + s)
	s = s.split(",")
	res = []
	for i in s:
		aux = float(i)
		res.append(aux)
	#print("resultat = " + str(res))
	return res