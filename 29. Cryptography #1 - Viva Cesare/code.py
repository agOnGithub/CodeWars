def caesar_crypto_encode(text, shift):
    if text == None or text.isspace() or text == "": return ""
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join([abc[(abc.index(c) + shift) % len(abc)] if c.isalpha() else c for c in text])