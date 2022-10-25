num = 5
for i in range(num):
    if i == 3:
        break
    print("Number is", i)

print("\nbreak syntax\n")
while num > 0:
    num -= 1
    if num == 3:
        break
    print("Number:", num)
    


print("\ncontinue syntax\n")


num = 5
for i in range(num):
    if i == 3:
        continue
    print("Number is", i)


while num > 0:
    num -= 1
    if num == 3:
        continue    
    print("Number:", num)