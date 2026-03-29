#Q1_ Check wheter the no. is prime or not?

n = int(input("Enter the number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Number is prime")
else:
    print("Not prime")
#Q2_Find the factorial of a number

num = int(input("Enter number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial:", fact)

#Q3 Palindrome numbe
num = int(input("Enter number: "))
original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Palindrome" if original == rev else "Not Palindrome")
#4 Sum of Digits
num = int(input("Enter number: "))
sum_digits = 0

while num > 0:
    sum_digits += num % 10
    num //= 10

print("Sum:", sum_digits)
#Q5 Divisors
num = int(input("Enter number: "))

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
#Q6  Armstrong Number
num = int(input("Enter number: "))
original = num
sum = 0
n = len(str(num))

while num > 0:
    digit = num % 10
    sum += digit ** n
    num //= 10

print("Armstrong" if sum == original else "Not Armstrong")
#Q7  Prime Numbers in Range
start = int(input("Start: "))
end = int(input("End: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
#Q8 GCD and LCM
a = int(input("Enter a: "))
b = int(input("Enter b: "))

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

lcm = (a * b) // gcd

print("GCD:", gcd)
print("LCM:", lcm)
#Q9 Decimal to Binary (without built-in)

num = int(input("Enter number: "))
binary = ""

while num > 0:
    binary = str(num % 2) + binary
    num //= 2

print("Binary:", binary)
#10 Perfect number
num = int(input("Enter number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

print("Perfect" if sum == num else "Not Perfect")