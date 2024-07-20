#find the element that is  present in  k+n index k is given by user k=3 n=2 i/p parameters are 3 6 8 4 61 2 o/p=2
  #k=3 n=4 80 70 54 36 72 o/p=error
'''my_list=list(map(int,input().split()))
k=int(input())
n=int(input())
len=len(my_list)
if len<k+n:
    print("ERROR")
else:
    for i in range(len):
        if(i==k+n):
            print(my_list[i])
            break'''
my_list=list(map(int,input().split()))
k=int(input())
n=int(input())
for i in range(0,len(my_list)):
    print(my_list(k+n),end=" ")
     break