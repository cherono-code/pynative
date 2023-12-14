str1 = "JhonDipPeta"
str2 = "JaSonAy"
#Expected Output: Dip
#Output = Son
def get_middle_char(str1):
    print("The original string is", str1)
    #get the middle char
    mi = int(len(str1) / 2)
    res = str1[mi - 1:mi + 2]
    print("string after splicing")
    print(res)
get_middle_char("JhonDipPeta")
get_middle_char("JaSonAy")
