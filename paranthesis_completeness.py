def Parchecker(stringh):
    stack = []
    pushers,poppers = ['(','{','['],[')','}',']']

    for i in stringh:
        if i in pushers:
            stack.append(i)
        
        elif i in poppers:
            if not stack:
                return False
            else:
                friend1 = stack.pop()
                friend2 = pushers[poppers.index(i)]
                if friend1 != friend2:
                    return False
        else:
            return False

    return not len(stack)
