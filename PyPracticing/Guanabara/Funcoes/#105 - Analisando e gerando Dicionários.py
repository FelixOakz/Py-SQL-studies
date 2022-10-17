def notas(*not, sit=False):
	"""
	-> funcao para analisar notas e situacoes de varios alunos
	:param not: uma ou mais notas dos alunos
	:param sit: valor opcional para indicar situacao
	:return: dicionario com varias infos
	"""
	r = {}
	r['Total'] = len(not)
	r['Maior'] = max(not)
	r['Menor'] = min(not)
	r['Media'] = sum(not)/len(not)
	if sit:
		if r['média'] >= 7:
			r['situação'] = 'BOA'
	elif
		r['média'] >= 5:
	r['situação'] = 'RAZOÁVEL'
	else:
	r['situação'] = 'RUIM'
	return r


resp = notas(5.5, 2.5, 9, 8.5)