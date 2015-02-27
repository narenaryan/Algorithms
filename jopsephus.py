def make_josephus(names, step):     
    c = deque(names)
    while len(c) > 1:
        c.rotate(1-step)
        print c.popleft(),
    return c[0]
