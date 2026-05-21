s = input().strip()
vowel = "aeiou"

def vowel_substrings(s):
    
    for i in range(len(s)):
        
        for j in range(i + 1, len(s) + 1):
            
            sub_str= s[i:j]
            
            if sub_str[-1] in vowel:   #takes the last index num
                print(sub_str)
                
vowel_substrings(s)