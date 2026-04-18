for i in range(1,101):
    print(i)

fruits = ['mango','apple','berries']

print(fruits[0])
print(fruits[1])
print(fruits[2])

for fruit in fruits:
    print(fruit)


# i = 1

# while i < 10:
#     print(i)
#     i+=1


for i in range(5):
    if i == 3:
        break
    print(i)


for i in range(5):
    if i==3:
        continue
    print(i)


for i in range(5): # 0 -4
    for j in range(3): # 0 -2
        print(i,j)




# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2
# 3 0
# 3 1
# 3 2
# 4 0
# 4 1
# 4 2


try:
    x = 10 / 0
    print(x)
except :
    print("Invalid math operation")