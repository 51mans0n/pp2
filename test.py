MyArray = []
while True:
    number = int(input())
    if number == 0:
        break
    MyArray.append(number)
max = MyArray[0]
min = MyArray[0]
sum = 0
for i in range(0, len(MyArray)):
    if max < MyArray[i]:
        max = MyArray[i]
    if min > MyArray[i]:
        min = MyArray[i]
    sum += MyArray[i]
average = sum/len(MyArray)
maximum = "Maximum = {}"
print(maximum.format(max))
minimum = "Minimum = {}"
print(minimum.format(min))
summary = "Summary = {}"  
print(summary.format(sum)) 
AverageValue = "Average Value = {}"
print(AverageValue.format(average))
def unique_values(MyArray):
    unique = []
    for number in MyArray:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique
print(unique_values(number))
        