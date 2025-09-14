def pallindrom_test(a):
    n=0
    for _ in a:
        n+=1

    for i in range(n//2):
        if a[i]!=a[n-i-1]:
            return False
    return True

var = "racecar"
if(pallindrom_test(var)):
    print("Pallindrome")
else:
    print("Not a Pallindrome")