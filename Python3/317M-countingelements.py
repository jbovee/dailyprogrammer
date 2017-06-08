import re
from collections import Counter

def main():
	tests = ['V(W((En5)2XY)2)3', 'CCl2F2', 'NaHCO3', 'C4H8(OH)2', 'PbCl(NH3)2(COOH)2', 'V(XY(Zn3)4C(CN(SO4)2)N)4HK6(H2SO4)2']
	for test in tests:
		results = get_groups(test)
		print(test)
		[print('{} :\t{}'.format(k, results[k])) for k in results]
		print()

def get_groups(input):
	frm = re.compile(r'[A-Z][a-z]?[0-9]*|\([A-Za-z0-9()]*\)[0-9]*')
	elements = frm.findall(input)
	counts = Counter({})
	for el in elements:
		counts += count_formula(el)
	return counts

def count_formula(formula):
	if '(' not in formula:
		return Counter(count_elements(formula))
	else:
		frm = re.compile(r'[A-Z][a-z]?[0-9]*|\([A-Za-z0-9()]*\)[0-9]*')
		l = frm.findall(re.search(r'\([A-Za-z0-9()]+\)', formula).group(0)[1:-1])
		e = Counter({})
		for el in l:
			e += count_formula(el)
		n = 1 if re.search(r'[0-9]+$', formula) == None else int(re.search(r'[0-9]+$', formula).group(0))
		for k in e:
			e[k] *= n
		return e

def count_elements(elements):
	el = re.compile(r'[A-Z][a-z]?[0-9]*')
	counts = {}
	for e in el.findall(elements):
		c = re.search(r'[A-Z][a-z]?', e).group(0)
		n = 1 if re.search(r'[0-9]+', e) == None else int(re.search(r'[0-9]+', e).group(0))
		if c in counts:
			counts[c] = counts[c] + n
		else:
			counts[c] = n
	return counts

if __name__ == "__main__":
	main()