num = int(input("Enter the 4 digit number"))
sum = 0;
for digit in str(num):
    print(digit)
    sum += int(digit) ** 4
    print(sum)

if sum == num:
    print(num, "is the armstrong number")
else:
    print(num,"is not an armstrong number")
