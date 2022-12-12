def solution(data, n):
	ndata = []
	for i in data:
		c = data.count(i)
		if c <= n:
			ndata.append(i)
	return ndata
