"""Q2. A program to ask for a string as input and print a version with each word capitalized and a full stop added at the end """
def capitalize_and_add_full_stop(input_string):
    result = ""
    # Flag to check if a full stop is already present
    full_stop_present = False
    # Flag to indicate the first character of a word
    new_word = True
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a letter
        if char.isalpha():
            # Capitalize only the first letter of each word
            if new_word:
                result += chr(ord(char) & ~32)
                new_word = False
            else:
                result += char
        else:
            # If the character is not a letter, add it as is
            result += char
            # Check if the current character is a space
            if char.isspace():
                # Reset the full stop flag when a new word starts
                full_stop_present = False
                new_word = True
            # Check if the current character is a full stop
            elif char == '.':
                full_stop_present = True
    # Add a full stop at the end if not already present
    if not full_stop_present and result and result[-1] != '.':
        result += '.'
    return result

# Get input from the user
user_input = input("Enter a string: ")
# Process the input and print the result
output_string = capitalize_and_add_full_stop(user_input)
print("Result:", output_string)