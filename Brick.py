'''You are given a rectangular board of M×N squares. Also you are given an unlimited number of standard domino pieces of 2×1 squares. You are allowed to rotate the pieces. You are asked to place as many dominoes as possible on the board so as to meet the following conditions:

1.Each domino completely covers two squares.

2.No two dominoes overlap.

3.Each domino lies entirely inside the board. It is allowed to touch the edges of the board.

Find the maximum number of dominoes, which can be placed under these restrictions.
'''
m,n=map(int, input().split())
a=max(m,n)
b=min(m,n)
counth=0
countv=0
for i in range(0,int(a/2)):
   counth=counth+1
counth=counth*b
if a % 2 != 0:
   for i in range(0, int(b / 2)):
       countv=countv+1
count=countv+counth
print(count)
