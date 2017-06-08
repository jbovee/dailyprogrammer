d = {
	'A': '4',
	'B': '6',
	'E': '3',
	'I': '1',
	'l': '1',
	'M': '(V)',
	'N': '(\)',
	'O': '0',
	'S': '5',
	'T': '7',
	'V': '\/',
	'W': '`//'
}

def l33tconvert(s):
	s = s.upper()
	isl33t = True if any(val in s for val in d.values()) else False
	for k, v in d.items():
		(match, swap) = (v,k) if isl33t else (k,v)
		s = s.replace(match,swap)
	s = s.lower().capitalize() if isl33t else s
	return(s)

for statement in ("I am elite.", "Da pain!", "Eye need help!", "3Y3 (\)33d j00 t0 g37 d4 d0c70r.", "1 n33d m4 p1llz!"):
	print(statement + " -> " + l33tconvert(statement))