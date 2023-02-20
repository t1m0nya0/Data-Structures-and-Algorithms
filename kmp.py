def pattern(t):
    p = [0] * len(t)
    j = 0
    i = 1
    while i < len(t):
        if t[j] == t[i]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j - 1]
    return p


def kmp(a, t):
    p = pattern(t)
    m = len(t)
    n = len(a)

    i = 0
    j = 0
    while i < n:
        if a[i] == t[j]:
            i += 1
            j += 1
            if j == m:
                return True
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1

    if i == n and j != m:
        return False


strs = ["flower","flow","flight"]
for i in strs:
    print(pattern(i))