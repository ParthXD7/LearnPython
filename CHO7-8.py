def validate_name(name):
    if name.isalpha():
        return True
    else:
        return False

def validate_pan(pan):
    return len(pan) == 10 and pan[:5].isalpha() and pan[5:9].isdigit() and pan[9].isalpha()


def generate_abecedarian():
    abecedarian_series = ""
    for char in range(ord('a'), ord('z')+1):
        abecedarian_series += chr(char)
        print(abecedarian_series)


def find_character_index(string, char):
    for i in range(len(string)):
        if string[i] == char:
            return i
    return -1

def draw_triangle(string):
    for i in range(len(string)):
        print(string[:i+1])

# Experiment 1
name = input("Enter your name: ")
pan = input("Enter your PAN card number: ")
if validate_name(name) and validate_pan(pan):
    print("Name:", name)
    print("PAN card number:", pan)
else:
    print("Invalid input.")

# Experiment 2
print("\nAbecedarian Series:")
generate_abecedarian()

# Experiment 3
given_string = input("\nEnter a string: ")
character = input("Enter a character to search: ")
index = find_character_index(given_string, character)
if index != -1:
    print(f"Character '{character}' is present at index:", index)
else:
    print(f"Character '{character}' is not present in the given string.")

# Experiment 4
print("\nTriangle based on string 'PYTHON':")
draw_triangle("PYTHON")
