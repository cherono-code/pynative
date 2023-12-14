s1 = "Ault"
s2 = "Kelly"
#new string s3 by appending s2 in the middle of s1.
# Expected output: AuKellylt
print("Original strings are:", s1, s2)
#find the middle of s1
mi = int(len(s1) / 2)
#first char to the middle char and last
f_chars = s1[:mi:]
last_chars = s1[mi:]
#add it to the s2
s3 = f_chars + s2 + last_chars
print("New string is: ")
print(s3)
