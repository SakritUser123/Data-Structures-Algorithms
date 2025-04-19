numbers=[]
inp = True
while inp == True:
    text = input("type in stop when you are done , Enter A Number: ")
    
    if text == 'stop':
        inp = False
    if text != 'stop':
        
        numbers.append(text)  
        
    
red_bin = []
blue_bin = []
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        blue_bin.append(numbers[i])
    else:
        red_bin.append(numbers[i])
        
print("Even: ",blue_bin,"Odd : ",red_bin)
