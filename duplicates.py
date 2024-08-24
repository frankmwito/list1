# remove duplicates from a list while maintaining the original order

n1 = int(input("Enter the size of your list:"))
numbers = list()

for i in range(n1):
    numbers.append(int(input(f"Enter any number {i+1}:")))

print("Your list is:", numbers)

unique_numbers = list()
seen = set()

for number in numbers:
    if number not in seen:
        unique_numbers.append(number)
        seen.add(number)
        
print(f"The list without duplicates (maintaining order): {unique_numbers}")