#Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    num = int(number/2)
    
    for i in range(2,num):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")    
    else:
        print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
