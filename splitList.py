# split a list into two (halves) parts

n1 = int(input("Enter the size of your list: "))
words = []

for i in range(n1):
    words.append(input(f"Enter any word {i+1}: "))

print("Your original word list is:", words)

# Find the middle index
middle_index = len(words) // 2

# Split the list into two halves
first_half = words[:middle_index]
second_half = words[middle_index:]

# Print both halves
print("First half of the list:", first_half)
print("Second half of the list:", second_half)
