# Given a string S, print all possible substrings that are palindrome.

s = input().strip()  #removes extra spaces

def palindrome_strings(s):

    for i in range(len(s)):

        for j in range(i + 1, len(s) + 1):
            sub_str = s[i:j]
                                            
            if sub_str == sub_str[::-1]:
                print(sub_str)
                
palindrome_strings(s)


#i=0, j=1
#s[0:1]---->m
#s[0:2]---->ma
#s[0:3]---->mad
#s[0:4]---->mada
#s[0:5]---->madam