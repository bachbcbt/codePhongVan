a=(1,2,3,4)
b=(1,2,3,3)
def comTup(a,b):
    a1=list(set(a))
    b1=list(set(b))
    sum=0
    for i in b1:
        if a1.count(i)==1:
            sum=sum+1
    if sum==len(b1):
        print('A has all B values')
    else:
        print('''A doesn't have all B values''')
    if len(set(a))<len(a) or len(set(b))<len(b):
        print('Both not unique')
    else:
        print('Both unique')
comTup(a,b)