def generate_hashtag(s):
    x = s.strip().title().replace(" ", "")
    if len(x) > 1"ç or len(x) < 1:
        return False
    else:
        return "#" + x