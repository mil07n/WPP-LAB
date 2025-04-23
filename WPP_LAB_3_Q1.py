original_num = int(input("Enter Your Number to Find the Digital Root: "))
final = original_num
while final >= 10:  
    sum_of_digits = 0
    while final > 0:
        sum_of_digits += final % 10
        final //= 10
    final = sum_of_digits
print(f"Digital Root = {final}")