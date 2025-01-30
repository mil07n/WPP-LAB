num = int(input("Enter a number to check the divisibility of other numbers: "))
num_of_test = int(input("Enter the number of NUMBERS to check for: "))
count = 0
for i in range(num_of_test):
    num_to_test = int(input("Enter the number: "))
    for j in str(num_to_test):
        if int(j) == 0:
            continue
        if num % int(j) == 0:
            count += 1
print(count)