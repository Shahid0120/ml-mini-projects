def countValidWords(sentence):
    overall_count = 0
    counter_check = 0 
    for word in sentence:
        idx = 0
        for c in word:
            # checks all lower case
            if c >= 'A' or c >= 'Z':
                counter_check = 1

            # checks only one exclamation mark 
            if c == '-':
                # checks position 
                if idx > 0 and idx + 1 <= len(word) - 1 and (word[idx - 1] == " " or word[idx + 1] == ' '):
                    counter_check = 1
        
            # checks only one punctuation mark
            if c in ['.', ',', '!', '?']:
                #$ checks position
                if idx + 1 <= len(word) - 1 and word[idx + 1] != ' ':
                    counter_check = 1 
            idx += 1  
        if counter_check != 1:
            overall_count += 1

    return overall_count


sentence = 'he bought 2 pencils, 3 erasers, and 1  pencil-sharpener.!'
p = countValidWords(sentence)
print(p)