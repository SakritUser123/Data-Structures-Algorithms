
individual_char = []

text = input("Enter A Text: ")
    

for char in range(len(text)) :
    individual_char.append(text[char])
    
print(individual_char)
vowels = ['a','e','i','o','u']
count = 0
for letter in range(len(individual_char)):
    if individual_char[letter] in vowels or str(individual_char[letter]).lower() in vowels:
        count += 1
        print(letter)

print("Vowels: ", count)
    
