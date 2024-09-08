def count(s):
    counts = {}
    if len(s) == 0:
        return {}
    else:
        i = 0
        while i < len(s):
            if s[i] not in counts.keys():
                counts[s[i]] = s.count(s[i])                
            i += 1
        return counts