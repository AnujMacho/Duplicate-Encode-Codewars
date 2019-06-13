def duplicate_encode(word):
    d = {c: word.lower().count(c) for c in word.lower()}
    print(d)
    res = []
    for a in word.lower():
        if d[a] == 1:
            res.append("(")
        else:
            res.append(")")
    return "".join(res)
print(duplicate_encode("dind"))