s = input(("Enter a sentence: "))
r = ''
i = len(s) - 1
while i >= 0 :
    r += s[i]
    i -= 1
print("The Reversed String is : ", r)