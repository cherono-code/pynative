#Enter Python code here and hit the Run button.
#arrange the characters of a string
#all lowercase letters should come first.
#output: yaivePNT

str1 = "PyNaTive"
print("The original string is:", str1)
lower = []
upper = []

#go through the string to find lowercase letters
for char in str1:
    if char.islower():
        lower.append(char)
#when upper
    else:
        upper.append(char)
#joining both strings
res = ''.join(lower + upper)
print("New string is:", res)
