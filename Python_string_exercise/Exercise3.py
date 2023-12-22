#Enter Python code here and hit the Run button.
#Given two strings, s1 and s2, 
#write a program to return a new string
#made of s1 and s2’s first, middle, and last characters.
#Expected Output: AJrpan

s1 = "America"
s2 = "Japan"
#print out the original string
print("The original strings are:", "\n\t",s1, s2)
#first chars for both s1 and s2
first = s1[0] + s2[0]
#the middle chars both s1 and s2
mi_s1 = s1[int(len(s1) / 2)]
mi_s2 = s2[int(len(s2) / 2)]
middle = mi_s1 + mi_s2
#last characters s1 and s2
la_s1 = s1[- 1]
la_s2 = s2[- 1]
last = la_s1 + la_s2
#new string
res = first + middle + last
print("The new string result is:", res)
