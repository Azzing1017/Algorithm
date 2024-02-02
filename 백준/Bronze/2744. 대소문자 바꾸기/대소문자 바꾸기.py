string_input = list(str(input()))

for i in range(len(string_input)):
    if string_input[i].isupper():
        string_input[i] = string_input[i].lower()
    elif string_input[i].islower():
        string_input[i] = string_input[i].upper()
        
print(''.join(map(str, string_input)))