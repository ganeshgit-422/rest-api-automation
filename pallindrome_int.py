def pallindrom_test(n):
    org = n
    sum = 0
    while n > 0:
        a = n%10
        sum = sum*10 + a
        n = n//10
    if sum == org:
        return True
    else:
        return False

num = 12321
if(pallindrom_test(num)):
    print("Pallindrome")
else:
    print("Not a Pallindrome")