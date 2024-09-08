import re
def alphanumeric(password):
    x = re.findall("[^a-zA-Z0-9]+", password)
    if x or password == "":
        return False
    else:
        return True