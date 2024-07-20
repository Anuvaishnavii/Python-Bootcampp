'''find the duplicates in an array
8 7 7 7 5 4 4 8 9
membership operator-in '''
my_list=list(map(int,input().split()))
''''for i in range(0,len(my_list)):
    for j in range(i+1,len(my_list)):
        if(my_list[i]==my_list[j]):
            print(my_list[j])'''
n=[]
for i in my_list:
    if(i not in n):
        n.append(i)
print(n)