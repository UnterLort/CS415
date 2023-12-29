def rephrase_sentence(text):
    # This above is defining a function. Below is five variables in this function

    # This will store the index of the first space character in the input
    space = text.index(" ")
    # This will store the first word of the sentence
    first_word = text[0:space]
    # This will store the index of the first character of the last word of the sentence
    last_word_index = text.rindex(" ")
    # This will store the last word of the sentence
    last_word = last_word_index + 1
    # This will store the original sentence without its first and last word
    mid_sentence = text[space: last_word]
    last = text[last_word:]
    print(last + mid_sentence + first_word)


# This prompts the user with an instruction to enter a line of text
user_input = str(input("Enter a line of text. No punctuation needed."))
rephrase_sentence(user_input)
