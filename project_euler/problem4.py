# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        n = i * j
        str_n = str(n)
        for k in range(len(str_n) // 2):
            if str_n[k] != str_n[-(k + 1)]:
                break
        else:
            if palindrome < n:
                palindrome = n

print("Palindrome:", palindrome)
    