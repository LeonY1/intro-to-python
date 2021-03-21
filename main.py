# Variable w/ Value
x = 1
# Variable w/ Variable
y = x

# Data Types
# int
int_num = 1000
# float
float_var = 3.141592
# str w/ "" or ''
str_var = "Hello World"
# bool
bool_var = False
# casting
str_var_2 = str(int_num)

# Operators
# Adding
int_num += 1   # 1001
int_num = int_num + 1 # 1002
# Subtracting
int_num -= 1 # 1001
int_num = int_num - 1 # 1000
# Multiplying / Dividing
int_num *= 10 # 10000
int_num /= 3 # 3333.3333333333335 (Slightly off because of rounding error)
# Modulus (Remainder)
remainder = 10000 % 3 # 1
# Floor Division
remainder = 10000 // 3 # 3333
# Concatenation
str_var += str_var_2
str_var = str_var + str_var_2

# Boolean Operator
# ==, >=, >, !=, <=, <
greater_than = 3 > 2 # True
equal_to = 3 == 2 # False
greater_than_or_equal_to = 3 >= 2 # True
not_equal_to = 3 != 2 # True
less_than = 3 < 2 # False
less_than_or_equal_to = 3 <= 2 # False
# and or not
and_bool = True and False # False
and_bool_2 = True and True # True
or_bool = True or False # True
or_bool_2 = False or False # False
not_bool = not True # False

# Lists
list_var = []
# Matrices
matrix_var = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]]
# Accessing
matrix_var[0][0] # 1
matrix_var[-1][0] # 10
matrix_var[-1][-1] # 12

# Slicing
matrix_var[0][0:2:1] # [1,2]
matrix_var[0][:2] # [1,2]
# Dictionaries
dict_var = {
    "Leon": "Presenter",
    "You": "Audience"
}

# Control Structures
# if...elif...else statements
if dict_var["Leon"] != "Presenter":
    print("Hi I am Leon!")
elif dict_var["You"] == "Audience":
    print("Hello Audience")
else:
    print("None of them matched")
# while statements
loop_var = 0
while loop_var < 16:
    loop_var += 1
# for statements
for i in range(10):
    print(i)
# Functions (args); Why?
def test_func(arg1, arg2, arg3):
    return arg1 + arg2 * 10 + arg3

# Importing
import random