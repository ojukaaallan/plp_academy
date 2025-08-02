print("Enter your text (type 'END' on a new line to finish):")

user_input = ""
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    user_input += line + "\n"

print("\nYou typed:\n")
print(user_input)
