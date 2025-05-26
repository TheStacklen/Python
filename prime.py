prime_list=[]

def check(a,b):
    s=0
    for i in range(a,b):
        for a in range(2,i):
            if i%a==0:
                break
        else:
            s+=1
    return s

print(check(10,30))
