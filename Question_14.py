#find the missing no in an array
my_list=list(map(int,input().split()))
n=int(input())
t=n*(n+1/2)
sum=0
miss=0
for i in range(len[my_list]):
    sum+=my_list[i]
miss=t-sum
print(miss)
