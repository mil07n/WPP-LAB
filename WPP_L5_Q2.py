def cutchocolate(k):
    half=k//2
    return(half*(k-half))
input=int(input("max no. of cuts to make: "))
print(f"Max No. of pieces that can be made with {input} cuts is",cutchocolate(input))