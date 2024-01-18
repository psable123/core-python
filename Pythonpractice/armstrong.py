n = int(input("Enter the number"))
num = len(str(n))
temp = n
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** num
    temp //= 10
if n == sum:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")


#n= 153
#num = 3
#sum = 0
#temp = n
#digit = temp % 100 --> 153 % 10 --> 15.3 means digit = 3 , decimal ke aage ki value consider krta hain.
#sum += digit ** num --> sum = sum +digit ** num -->0+3**3 --> 27
#temp //= 10  --> 153 //= 10 -->15.3 means temp == 15


