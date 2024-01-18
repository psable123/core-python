#num = 5 ;
num = int(input("Enter the number"))
def factorial(num):
    if (num==1 or num==0):
        return 1
    else:
        return(num*factorial(num-1));

#num = 5;
print("factorial of",num,"is :",factorial(num))
