num=[]
n=int (input("enter range"))
for i in range(1,n+1):
    e=int(input("enter element"))
    num.append(e)
print("original list",num)
result= map(lambda x: x+x+x,num)
print("\nTriple of list")
print(list(result))