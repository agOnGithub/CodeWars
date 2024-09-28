def duplicate_count(text):
    text = text.casefold()
    l = {}
    for x in range(0, len(text)):
        if text.count(text[x]) > 1:
            l[text[x]] = text.count(text[x])            
    return len(l)