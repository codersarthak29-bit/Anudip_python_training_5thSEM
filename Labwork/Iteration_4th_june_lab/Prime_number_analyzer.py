#Program to check if a number is prime or not
#Taking input from the user
num=int(input("Enter a number: "))
if num>1:
    i=2
    while i<num:
        if (num%i)==0:
            #factors of num are found, so it is not a prime number
            print("Factors of",num,"are:")
            while i<num:
                if (num%i)==0:
                     print(i)
                i+=1
            print(num,"is not a prime number")
            break
        i+=1
    else:
        print(num,"is a prime number")
else:
    print("numbers less than or equal to 1 are not prime numbers")