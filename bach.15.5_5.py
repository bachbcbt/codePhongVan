a=['abc','','def']
def delEmpty(a):
    b=[]
    for i in range(0,len(a)):
        if len(a[i])!=0:
            b.append(a[i])
    return b
print(delEmpty(a))
