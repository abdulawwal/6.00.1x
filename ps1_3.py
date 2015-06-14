s = 'azcbobobegghakl'
longString = ''
for i in range(len(s)):
    tmpString = s[i]
    for j in range(len(s[i:])-1):
        if s[i+j] <= s[i+j+1]:
            tmpString += (s[i+j+1])
        else:
            break
    if len(tmpString) > len(longString):
        longString = tmpString
print longString
