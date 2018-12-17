def fibs(n):                                                                                                 
    fibs = [0, 1, 1]                                                                                           
    for f in range(2, n):                                                                                      
        fibs.append(fibs[f] + fibs[f-1])                                                                         
    return fibs[n]

print(fibs(5))