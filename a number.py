n=int(input())
if n<100:
        a=n//10
        b=n%10
        e=(b*10)+a
else:
        a=n//10
        b=n%10
        c=a%10
        d=a//10
        e=(b*100)+(c*10)+d
print(e)        
