import sys

def pigLatin(txt):
    words = txt.split(' ')
    i = 0
    while i < len(words):
        if words[i][0] in 'aeiou':
            words[i] = words[i] + 'yay'
        else:
            index = 0
            while words[i][index] not in 'aeiou':
                index += 1
            words[i] = words[i][index:] + words[i][:index] + 'ay'
        i = i + 1
    return ' '.join(words)

#output
MESSAGE=sys.stdin.readlines()
for i in MESSAGE:
    if i[-1]=='\n':
        print(pigLatin(i[:-1]))
    else:
        print(pigLatin(i))