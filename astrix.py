def censor(text, word):
    wordlist = text.split()
    # print(wordlist)
    result = ''
    stars = '*' * len(word)
    index = 0
    for i in wordlist:
        if i == word:
            wordlist[index] = stars
        index += 1
    result = ' '.join(wordlist)
    return result


if __name__ == '__main__':
    exct = "Geeks forGeeks is a computer science portal for geeks.\
               I am pursuing my major in computer science . "
    cen = "science"
    print(censor(exct, cen))
