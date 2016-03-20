import sys

data = raw_input()

rot = 13
for s in list(data) :
    c = ord(s)
    if c >= ord('A') and c <= ord('Z') :
        sys.stdout.write(chr((c - ord('A') - rot + 26) % 26 + ord('A')))
    elif c >= ord('a') and c <= ord('z') :
        sys.stdout.write(chr((c - ord('a') - rot + 26) % 26 + ord('a')))
    else :
        sys.stdout.write(s)
