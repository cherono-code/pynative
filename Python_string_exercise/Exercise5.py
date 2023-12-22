#Count all letters, digits, and special symbols from a given string
#Expected Outcome:
#Total counts of chars, digits, and symbols 
#Chars = 8 
#Digits = 3 
#Symbol = 4
str1 = "P@#yn26at^&i5ve"

def find_char_digit_symbol(str1):
    #iterate the string
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in str1:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1
    print("Total counts of chars, digits, and symbols")
    print("char =", char_count, "Digits =", digit_count, "Symbol = ", symbol_count)
find_char_digit_symbol(str1)
