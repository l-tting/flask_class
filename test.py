numbers = [1,2,3,4,5,6,7,8,9,10]


# even = []
# for i in numbers:
#     if i%2 == 0:
#         even.append(i)
# print(even)


even = [i for i in range(1,11) if i%2 == 0 ]
print(even)


odd = [i for i in numbers if i%3 == 0]
print(odd)


