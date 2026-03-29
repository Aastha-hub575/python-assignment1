#Q1 Reverse string

s = input("Enter string: ")
print(s[::-1])
#Q2 Palindrome String

s = input("Enter string: ")
print("Palindrome" if s == s[::-1] else "Not Palindrome")
#Q3 Count Vowels & Consonants

s = input("Enter string: ")
vowels = "aeiouAEIOU"
v, c = 0, 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

print("Vowels:", v)
print("Consonants:", c)
#Q4 Uppercase without built-in

s = input("Enter string: ")
result = ""

for ch in s:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)
#Q5 Length without len()

s = input("Enter string: ")
count = 0

for _ in s:
    count += 1

print("Length:", count)
#Q6 Anagram

s1 = input("Enter string1: ")
s2 = input("Enter string2: ")

print("Anagram" if sorted(s1) == sorted(s2) else "Not Anagram")
#Q7 First Non-Repeating Character

s = input("Enter string: ")

for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break
#Q8 Frequency of Characters

s = input("Enter string: ")
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
#Q9 Remove Duplicates

s = input("Enter string: ")
result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)
#Q10 Longest Word

s = input("Enter sentence: ")
words = s.split()
longest = ""

for w in words:
    if len(w) > len(longest):
        longest = w

print(longest)