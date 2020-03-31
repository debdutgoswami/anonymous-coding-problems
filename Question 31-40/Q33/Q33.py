def alternatingCharacters(s):
    final = s[0]
    for i in range(1,len(s)):
        if final[len(final)-1]==s[i]:
            continue
        else:
            final+=s[i]
    return len(s)-len(final)

if __name__ == '__main__':
    s = input()
    result = alternatingCharacters(s)
    print(s)