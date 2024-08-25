numbers = [3,1,2,4,5,6,7,8,9,10,11,16,12,13]
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

difference = largest - smallest

printfe("The largest number is:", largest)
print("The smallest number is:", smallest)
print("The difference between them is:", difference)

average = sum(numbers) / len(numbers)
print("The average of the numbers is:", average)
