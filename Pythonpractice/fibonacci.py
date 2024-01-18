# def fibonacci(n):
#     print(n)
#     if n < 0:
#         print("Incorret Number")
#     elif n == 1:
#         print("n=1")
#
#         return 0
#     elif n == 2:
#         print("n=2")
#         return 1
#     else:
#         print("pass")
#         return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(5))
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
