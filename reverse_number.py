
number = []

num = input("Enter A Number: ")
for i in range(len(num)):
    number.append(num[i])
new_num = num[::-1]
print("The reversed number is: " , new_num)
