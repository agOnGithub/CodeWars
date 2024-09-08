def pig_it(text):
    txt = text.split(' ')
    
    for i in range(len(txt)):
        if txt[i] == "." or txt[i] == "!" or txt[i] == "?":
            pass
        else:
            word = txt[i]
            start = word[0]
            end = word[1:]
            word = end + start + "ay"
            txt[i] = word
        i += 1
    return " ".join(txt)