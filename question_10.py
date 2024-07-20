#print the element at a particular index and do cyclic manner 
#large number values can be descresed by using mod %
'''my_list=list(map(int,input().split()))
k=int(input())
len=len(my_list)
a=k%len
if(a==0):
    print("Error")
else:
    print(my_list[a])'''
my_list=list(map(int,input().split()))
k=int(input())
idx=k%len(my_list)
print(my_list[idx])