
# Operator Precedence
print( 30 * 2 + 10 - (21  // 5) )
# ========================================================================================================

# Assignment Operator
x = int("12")
y = int(12.5)

print(type(x)) # type <class 'string'>
print(type(y)) # type <class 'int'>
# ========================================================================================================

# pow() function
x = pow(3, 3) # 3 pangkat 3
y = pow(3, -3) # 3 pangkat -3
z = pow(2,4,3) # 2 pangkat 4 modulo 3

print(x)
print(y)
print(z)
# ========================================================================================================

# convert to string
x = int("12")
y = str(12.5)

print(type(x))
print(x)
print(type(y))


# ========================================================================================================
# BMI Calculator
berat = float(input("Masukkan berat anda dalam kg: "))
tinggi = float(input("Masukkan tinggi anda dalam m: "))

bmi = (berat/(tinggi ** 2))
print("BMI Anda =",bmi)

#output
# Masukkan berat anda dalam kg: 70
# Masukkan tinggi anda dalam m: 1.75
# BMI Anda = 22.857142857142858

# ========================================================================================================

# Comparison Operator
# only return True or False
print('Result of 10 > 5: ', 10 > 5)
print('Result of 5 < 1: ', 5 < 1)
print('Result of 5 == 5', 5 == 5)
print('Result of 5 != 5', 5 != 5)
print("Result of 'a' > 'b': ", 'a' > 'b')

#output
# Result of 10 > 5: True
# Result of 5 < 1: False
# Result of 5 == 5: True
# Result of 5 != 5: False
# Result of 'a' > 'b': False

# Comparison Operator Is & In

# Is memeriksa bahwa kedua type object apakah sama atau tidak 
# In memeriksa apakah sebuah object ada di dalam object

# print("=====================================")

x = 5
y = 5.0

print(x == y) # True
print(x is y) # False

print("a" in "Hello") # False
print("e" in "Hello") # False



# ========================================================================================================
# Logical Operator
# and : if both condition is True
# or : if one of the condition is True
# not : if the condition is False


x = True
y = False
print(x and y)
print(x or y)
print(not x)
print(not y)
print(x or y) 


X = False
Y = True
Z = True

print( X or Y and Z or X ) # True
# decripstion why answer is True
# False or True and True or False
# True and True or False
# True or False
# True

#output
# False
# True
# False
# True
# ========================================================================================================


#Pass Keyword
# pass keyword is used to do nothing
# it is used when a statement is required syntactically but you do not want any command or code to execute

a = 10
b = 20

if a > b:
    pass
else:
    print("a is not greater than b")
    
#========================================================================================================