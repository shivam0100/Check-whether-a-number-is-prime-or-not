def is_prime(n):
    if n>1:
        for i in range(2, n):
            if n%i==0:
                print("False")
                break
        else:
            print("True")
    else:
        print("False")
is_prime(11)


