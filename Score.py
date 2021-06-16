'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given N scores. Store them in a list and find the score of the runner-up.
'''
n = int(input())
lis=list(map(int,input().split()))
lis.sort()
for i in lis:
    while i==max(lis):
        lis.remove(i)
print(lis[-1])

