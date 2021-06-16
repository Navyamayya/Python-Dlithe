''''Python program to remove Nth occurrence of the given word. Given a list of words in Python, the task is to remove the Nth occurrence of the given word in that list.

'''
lis=list(input().split())
word,N=input().split()
num=0
for i in range(0,len(lis)):
    if lis[i] == word:
        num=num+1
        if num==int(N):
            lis.pop(i)
            break
print(lis)

