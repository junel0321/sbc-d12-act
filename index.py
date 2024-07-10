text = input("Enter a sentence: ")
str = []
current_str = ""

for char in text:
    if char == " ":
        if current_str:
            str.append(current_str)
            current_str = ""
    else:
        current_str += char

if current_str:
    str.append(current_str)

output = ""
for strcurrent_str in str:
    if output:
        output += ", "
    output += '"' + strcurrent_str + '"'

print(output)
