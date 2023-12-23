#create a new string s3 
#made of the first char of s1, then the last char of s2, 
#Next, the second char of s1
#second last char of s2, and so on. 
#Any leftover chars go at the end of the result.

s1 = "Abc"
s2 = "Xyz"
print("The original string is:", "\n",s1, "\n",s2)
#find the first char of the new string
f_char = s1[0] + s2[- 1]
#find the middle char of the new string
mi_s1 = int(len(s1) / 2)
mi_s2 = int(len(s2) / 2)
middle = s1[mi_s1] + s2[mi_s2]
#find the last char of the new string
l_char = s1[- 1] + s2[0]
#addiing up the char to make the neew sttring
res = f_char + middle + l_char
print("The new s3 string is:", res)
