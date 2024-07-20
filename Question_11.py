'''find the maximum element in a given list'''
my_list=list(map(int,input().split()))
res=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>res):
        res=my_list[i]
print(res)