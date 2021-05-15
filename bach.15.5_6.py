
def str100():
    a=[]
    for i in range(0,101):
        a.append(str(i))
    return ''.join(a)
print(str100())