n='abcd'
def strToASCII(a):
    b=list(a)
    c=[]
    sum=0
    for i in b:
        c.append(str(ord(i)))
    return (''.join(c))
print(strToASCII(n))
