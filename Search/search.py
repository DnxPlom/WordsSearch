import re, time

################# Search input ##################
search_word = input('Enter search word:  ')
word_length = int(input('Enter word length:  '))
search_word = search_word.lower()

start_time = time.time()

############# Open Dictionary File ##############
with open('dict.txt', 'r') as f:
   file = f.read()
   words = file.split()

################ Search Function ################
def search(words, word_length):
    found = []
    for word in words:
        if len(word) != word_length:
            continue

        check = []
        for letter in word:
            if letter not in search_word:
                check.append(0)
                break
            elif len(re.findall(letter, word)) > len(re.findall(letter, search_word)):
                check.append(0)
                break
            else:
                check.append(1)
        if 0 not in check:
            found.append(word)

    for i in found: print(i)
    if found: print(f'{len(words)} words searched. \n{len(found)} Words Found!!! Completed in {time.time() - start_time} s')
    else: print(f'{len(words)} words searched. \nFOUND NO WORDS!!!')

####################################################
search(words, word_length)
