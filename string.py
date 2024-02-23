strings = input("Enter a String")

for s in range(len(strings)):
    for letter in range(s+1):
        print(strings[letter],end="")
    print()

str2 = "ate"

for x in strings:
    print(x+str2)