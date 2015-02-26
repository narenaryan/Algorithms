def pascalize(i):
    if i == 1:
        return [1]
    else:
        L = pascalize(i-1)
        ret = [1]
        for i in xrange(len(L)-1):
            ret.append(L[i] + L[i+1])
        ret.append(1)
        return ret
