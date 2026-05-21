# longest palindrome substring

s = input().strip()

def longest_substring(s):
    longest = ""
    
    for i in range(len(s)):
        
        for j in range(i+1, len(s)+1):

            sub_str = s[i:j]
            
            if sub_str == sub_str[::-1]:
                
                if len(sub_str) > len(longest):
                    longest = sub_str

    print(longest)                              


longest_substring(s)