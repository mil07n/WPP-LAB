#Program to find factorial of a number

n=int(input('Number = ')) #enter number whom to find factorial of
print("Number = ", n)
q=1
for i in range (1,n+1):
    q=q*i
print(q)