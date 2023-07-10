def capitalize_first_letter(string):
    words = string.split()
    capitalized_words = [word[0].upper() + word[1:] for word in words]
    capitalized_string = ' '.join(capitalized_words)
    return capitalized_string

input_string = input("Enter a string: ")
result = capitalize_first_letter("Enter a string")
print(result)
