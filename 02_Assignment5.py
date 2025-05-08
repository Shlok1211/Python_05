a = []
for i in range(1,11):
    a.append(i)
print('Original list:',a)

extractedList = a[0:5]
print('Extracted first five elements:',extractedList)

reversedList = extractedList[::-1]
print('Reversed extracted elements:',reversedList)