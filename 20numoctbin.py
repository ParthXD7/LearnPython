# print first 20 natural numbers in octal, hexadecimal, and binary
for i in range(1, 21):
    print(f"{i}: {oct(i)=}, {hex(i)=}, {bin(i)[2:]=}")