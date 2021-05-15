def pr():
    a=[]
    for i in range(1,21):
        if i%3==0 and i%5!=0:
            a.append('Fizz')
        elif i%5==0 and i%3!=0:
            a.append('Buzz')
        elif i%15==0:
            a.append('FizzBuzz')
        else:
            a.append(str(i))
    return ''.join(a)
print(pr())