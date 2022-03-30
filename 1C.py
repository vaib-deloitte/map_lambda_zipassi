num=[]
n=int (input("enter range"))
for i in range(1,n+1):
    e=int(input("enter element"))
    num.append(e)
print ("numbers in the list:",num)
new_num= list(filter(lambda x: x<0,num))
print ("negative no",new_num)