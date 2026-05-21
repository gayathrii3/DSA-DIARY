# Secret Pair Destroyer

s = input().strip()

def destroy_pair(s):

    final_str = ""
    count = 0

    i = 0
    while i < len(s):  #checks till the last index

        if i < len(s)-1 and s[i] == s[i+1]:  #checks if the next num present and is same as its previous num
            final_str += "##"
            count += 1
            i += 2           #skips the 2 nums and replaces them with ##

        else:
            final_str += s[i]
            i += 1

    print("Final string:", final_str)
    print("Count:", count)

    if "##" in final_str:
        print("Danger pattern")

destroy_pair(s)