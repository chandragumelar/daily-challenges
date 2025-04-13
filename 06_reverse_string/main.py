text = input("Enter a word: ").strip()
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text  # prepend each character

print(f"Reversed: {reversed_text}")
