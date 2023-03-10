phrase = input("Введите строку: ")
x = phrase.replace(":", "%")
print(x)
count = 0
for i in x: 
    if i == '%': 
        count += 1
print(count)        
