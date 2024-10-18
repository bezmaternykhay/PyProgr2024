from operator import length_hint

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

length = len(numbers)
for i in range(length):
    if (numbers[i] == None):
        index = i

slice1 = numbers[:index]
slice2 = numbers[index+1:]
total_sum = sum(slice1) + sum(slice2)
average = total_sum/length
numbers[index] = average
print("Измененный список:", numbers)