def plusOne(li):
    s = "".join([str(i) for i in li])
    i = int(s)
    i += 1
    s1 = []
    while(i > 0):
        r = i % 10
        i = i // 10
        s1.append(r)
    return s1[::-1]
li = [9,9,9]
print(plusOne(li))