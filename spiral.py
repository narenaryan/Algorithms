def spiral_turn(m,n,back):
	k,l = 0,0
	while k<m and l<n:
		i = l
		while i<n:
			print(back[k][i],end=' ')
			i += 1
		k += 1
		i = k
		while i<m:
			print(back[i][n-1],end=' ')
			i += 1
		n -= 1
		if k < m:
			i = n-1
			while i >= l:
				print(back[m-1][i],end=' ')
				i -=1
			m -= 1
		if l < n:
			i = m-1
			while i >= k:
				print(back[i][l],end=' ')
				i -= 1
			l += 1
