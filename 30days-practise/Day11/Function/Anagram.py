# check anagram

def is_anagram(w1, w2):

    if len(w1) != len(w2):
        return False
    
    freq = {}

    for ch in w1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in w2:
        if ch not in freq:
            return False
        
        freq[ch] -= 1

    for value in freq.values():
        if value != 0:
            return False
        
    return True

print(is_anagram('listen', 'slent'))


