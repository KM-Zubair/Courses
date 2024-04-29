"""Q3. A Python program that asks for a string as input and determine 
whether it's a palindrome (reads the same backward as forward) or not. """

# Print statement indicating the purpose of the code
print("Checks if a string is a palindrome")

# Get input from the user
str_input = input("Please enter a string: ")

# Initialize indices for checking palindrome
left_index = 0
right_index = len(str_input) - 1

# Loop to check if the string is a palindrome
while left_index < right_index:
    # Compare characters at left and right indices
    if str_input[left_index] != str_input[right_index]:
        break
    # Move indices towards the center
    left_index += 1
    right_index -= 1

# Check if the loop was broken before reaching the center
if left_index < right_index:
    print("The word '", str_input, "' is not a palindrome")
else:
    print("The word '", str_input, "' is a palindrome")
