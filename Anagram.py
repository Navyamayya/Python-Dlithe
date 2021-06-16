'''Problem Description
Rotate a given String in the specified direction by specified magnitude.
After each rotation make a note of the first character of the rotated String, After all rotation are performed the accumulated first character as noted previously will form another string, say FIRSTCHARSTRING.
Check If FIRSTCHARSTRING is an Anagram of any substring of the Original string.
If yes print "YES" otherwise "NO". Input
The first line contains the original string s. The second line contains a single integer q. The ith of the next q lines contains character d[i] denoting direction and integer r[i] denoting the magnitude.
'''
string=input()
time=int(input())
n=len(string)
lis=[]
for index in range(time):
    side,r= input().split()
    x=int(r)
    for i in string:
        if(side=="L"):
            new_string=string[x:]+string[0:x]
        elif(side=="R"):
            new_string = string[(n-x):] + string[0:(n-x)]
        lis.append(new_string[0])
"".join(lis)
sub_list =[(string[index1-1:index2])
for index1 in range(1,len(string)+1)for index2 in range(index1,len(string)+1)if len(string[index1-1:index2]) == 3]
for substring in sub_list:
    if sorted(lis) == sorted(substring):
        print("Yes")
        break
    else:
        print("No")
        break
