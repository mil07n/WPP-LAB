#Program to swap two variables without using third variable
a=int(input('a = '))
b=int(input('b = '))
a=a+b # a = 10 + 5 = 15
b=a-b # b = 15 - 5 = 10
a=a-b # a = 15-10 = 5
print('a = ',a)
print('b = ',b)