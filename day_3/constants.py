alphabet = 'abcdefghijklmnopqrstuvwxyz'
VALUES = {}
# Code to generate values. After generation, it should never be changed
for i in range(26):
    VALUES[alphabet[i]] = i + 1
for i in range(26):
    VALUES[alphabet[i].upper()] = i + 27
