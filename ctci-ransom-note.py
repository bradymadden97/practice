# Hash Tables: Ransom Note
# Cracking the Coding Interview Challenge
# https://www.hackerrank.com/challenges/ctci-ransom-note

class Word:
    def __init__(self, word, used):
        self.word = word
        self.used = used
    
    
def ransom_note(magazine, ransom):
    # Initialize hashMap
    hashMap = []
    for i in range(len(magazine)):
        hashMap.append([])
        
    # Add magazine words to hashMap
    for word in magazine:
        hashIdx = hash_func(word, len(hashMap))
        hashMap[hashIdx].append(Word(word, False))
    
    # Compare note words to magazine hashMap
    for word in ransom:
        hashIdx = hash_func(word, len(hashMap))
        foundMatch = False
        for entries in hashMap[hashIdx]:
            if entries.word == word and not entries.used:
                foundMatch = True
                entries.used = True
                break
        if not foundMatch:
            return False
    return True
            

def hash_func(word, length):
    hashVal, count = 0, 0
    for letter in list(word):
        count += 1
        hashVal += (ord(letter) * 31 + count * 7)
    return hashVal % length

#------------------------------- Provided -------------------------------

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    
