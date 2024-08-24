# reverse list without the built in reverse()

n1 = int(input("Enter the size of yiur list"))
numbers = list()

for i in range(n1):
    numbers.append(int(input(f"Enter any number {i+1}:")))

print("Your list is", numbers)

numbers1 = list()

for i in range(len(numbers) -1, -1, -1):
    numbers1.append(numbers[i])
    
print("the reversed list is:", numbers1)