age = 18 # diberikan kondisi bahwa age = 18

if age < 20: # result dari age < 20 adalah True
    print('youth discount')

#output
# youth discount

# ========================================================================================================
# Pass Keyword

# pass keyword is used to do nothing
num = 5
if num % 2 == 0:
    print('Nomor genap')
if num % 3 == 0:
    pass

# output
# when num = 5
# Nomor genap

def func():
    pass

func()

# ========================================================================================================
# Elif Statement
a = 22
b = 23

if a < b:
  print("b itu big brother")

elif a > b:
  print("a itu big brother")

else:
  print("ayo kenapa")
#========================================================================================================
# if Else Statement

a = "ABC"
b = "abc"
c = "ABC"
d = "CBA"

if a == b:
    print("123")
if c == d:
    print("456")
else:
    print("789")
# output
# ada 2 kondisi yang dijalankan


# ini kurang efisien lantaran ada 2 kondisi yang dijalankan
# kita bisa menggunakan elif untuk menggantikan else
# elif akan mengecek kondisi yang sama dengan if sebelumnya
# jika kondisi if sebelumnya tidak terpenuhi maka elif akan dijalankan
# jika kondisi elif terpenuhi maka else tidak akan dijalankan
# jika kondisi elif tidak terpenuhi maka else akan dijalankan
# ========================================================================================================
# Nested If Statement

num = -100
if num < 0:
    print(num, 'adalah bilangan negatif. ')
else:
    print(num, 'adalah bukan bilangan negatif ')
    if num % 2 == 0:
        print(num, 'adalah bilangan genap')
    else:
        print(num, 'adalah bilangan ganjil')

#output
# -100 adalah bilangan negatif


#========================================================================================================
