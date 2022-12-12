def solution(data, n):
	ndata = []
	for i in data:
		c = data.count(i)
		if c < n:
			ndata.append(i)




solution([5, 10, 15, 10, 7], 1)
