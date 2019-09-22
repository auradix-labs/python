user_input = input("Enter any sentence")
# filter1 = user_input.strip()
# filter2 = filter1.replace("country", "India")
sentence = user_input.split(" ")
print(sentence)
result = ""
number_of_words = len(sentence)
for word in sentence:
    if word == "i":
        word = "I"
    if word.lower() == "country":
        word = "India"
    if word == "*" or word == "#" or word == "$":
        continue
    new_word = ''
    for character in word:
        if character == "*" or character == "#" or character == "$":
            continue
        new_word = new_word + character
    word = new_word.strip()
    result = result + " " + word
result = result.strip()
number_of_charecter = len(result)
print(result)
print("Total words: ", number_of_words)
print("Total charecters: ", number_of_charecter)
