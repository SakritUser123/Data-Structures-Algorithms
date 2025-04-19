numbers=[]
inp = True
while inp == True:
    text = input("type in stop when you are done , Enter A Number: ")
    
    if text == 'stop':
        inp = False
    if text != 'stop':
        text = int(text)
        numbers.append(text)  
        
swapped = True
while swapped == True:
    swapped = False
    for i in range(len(numbers)-1):
        
        if numbers[i] > numbers[i+1]:
            
            print('ok')
            numbers[i] , numbers[i+1] = numbers[i+1], numbers[i]
            swapped = True
            
        
   
print('The Largest number is: ', numbers[-2])
