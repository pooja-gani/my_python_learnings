x = str(input("Enter a word: "))
l = len(x)
i = 0
j = l-1

pallindrome = True

while i <= l/2:
    if x[i] != x[j]:
       pallindrome = False
       break
    i += 1
    j -= 1

if pallindrome:
    print(f"{x} is a palindrome.")
else:
    print(f"{x} is not a palindrome.")



