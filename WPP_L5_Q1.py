def maxxor(num, check):
    for i in range(num, check + 1):
        for j in range(i, check + 1): 
            element = i ^ j
            print(f"{i} xor {j} =", element)
maxxor(10, 15)