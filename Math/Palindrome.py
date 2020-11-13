def is_palindrome(word):
    inverted_word = word[::-1]
    print(f'The word is {word} and the reverse is {inverted_word}')

    for index, letter in enumerate(inverted_word):
        print(f"{index}     {letter}     {word[index]}")

        if letter != word[index]:
            return False
    
    return True

    

print(is_palindrome('osso'))
print(is_palindrome('roma'))
print(is_palindrome('ana'))
print(is_palindrome('casa'))
print(is_palindrome('mom'))
print(is_palindrome('level'))
print(is_palindrome('true'))