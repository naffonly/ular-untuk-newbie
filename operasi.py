
# Operator Precedence
print( 30 * 2 + 10 - (21  // 5) )

# Assignment Operator
x = int("12")
y = int(12.5)

print(type(x)) # type <class 'string'>
print(type(y)) # type <class 'int'>

# pow() function
x = pow(3, 3) # 3 pangkat 3
y = pow(3, -3) # 3 pangkat -3
z = pow(2,4,3) # 2 pangkat 4 modulo 3

print(x)
print(y)
print(z)

# convert to string
x = int("12")
y = str(12.5)

print(type(x))
print(x)
print(type(y))

# BMI Calculator
berat = float(input("Masukkan berat anda dalam kg: "))
tinggi = float(input("Masukkan tinggi anda dalam m: "))

bmi = (berat/(tinggi ** 2))
print("BMI Anda =",bmi)

#output
# Masukkan berat anda dalam kg: 70
# Masukkan tinggi anda dalam m: 1.75
# BMI Anda = 22.857142857142858