def testit(act, s):
    t = ""
    for i1, i2 in zip(act, s):
        if i1 == "run" and i2 == "_":
            t += "_"
        elif i1 == "run" and i2 == "|":
            t += "/"
        elif i1 == "jump" and i2 == "_":
            t += "x"
        else:
            t += "|"
    return t