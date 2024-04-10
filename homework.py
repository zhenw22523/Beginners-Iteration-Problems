print(f"============ Starters ============")
correct = False
flag = 1
while not correct:
    if flag > 3:
        print("Locked")
        break
    pwd = input("Enter password\n>> ")
    if pwd == "114514":
        print("Correct Password")
        correct = True
        break
    flag += 1
   

times = int(input("Enter a number\n>> "))
name = input("Input your name\n>> ")
for i in range(times):
    print(name)


print("============ Multiplication ============")
num = int(input("Enter a positive integer\n>> "))
while num <= 0:
    print("Not a positive integer")
    num = int(input("Enter a positive integer\n>> "))

for i in range(1, num+1):
    for j in range(i, num+1):
        print(f"{i}*{j}={i*j}", end=" ")
    print()


print("============ Prime Number ============")
is_prime = True
num = int(input("Input an integer\n>> "))
for i in range(2, int(num ** 0.5) + 1):
    # Use range [2, num^0.5] because the number of factors of a number (other than 1 and itself) is limited to its square root.
    if num % i == 0:
        is_prime = False

if is_prime:
    print("Is a prime")
else:
    print("Not a prime")


print("============ FizzBuzz ============")
for i in range(1, 101):
    print(i, end=" ")
    if i % 3 == 0:
        print("Fizz", end="")
    if i % 5 == 0:
        print("Buzz", end="")
    print()
