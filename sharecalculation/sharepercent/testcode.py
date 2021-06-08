import datetime
num = 26575

init_num = 2

numbers = [i for i in range(init_num, num+1)]
one = datetime.datetime.now
for i in range(init_num, len(numbers)):
    for a in numbers:
        if a % i == 0:
            numbers.remove(a)
two = datetime.datetime.now
print(one)
print(two)
if num in numbers:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True
#             break

# if flag:
# print(num, "is not a prime number")
# else:
# print(num, "is a prime number")
