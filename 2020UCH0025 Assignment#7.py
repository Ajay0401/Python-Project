print('=======================================================================')
print("""Q1. Check whether two string are a permutation of each other or not.
Q2. Count trailing zeroes in factorial of a number.
Q3. Check Armstrong Number
Q4. Sum of all the elements of a list
Q5. Program to reverse a date in the format "yyyyMMdd"
Q6. Sum of G.P.
Q7. Take upper limit and prints all numbers within the given range in increasing order.
Q8. Take upper limit and prints all numbers within the given range in decreasing order.
Q9. Factorial of A Integer
Q10. Recursive python program to print the fibonacci series upto n terms.
Q11. Recursive python program to return gcd of a and b
Q12. Recursive python program to return lcm of a and b
Q13. Binomial Coefficient C(n, k)
Q14. Program to find Minimum element of array
Q15. Program to find Maximum element of array
Q16. Find out and return the number of digits present in a number
Q17. (a) Calculating the factorial of a number
          (b) Python code along with one line explaination
          (c) Python code along with one line explaination
          (d) Python code along with one line explaination
          (e) Observe the adjacent Python Code
Q18. Program Raise a TypeError if x is not an integer
Q19. Try-except for division of x by y""")
print('=======================================================================')
p=int(input("Enter Q. No.:"))
print('=======================================================================')
if p==1:
    # check whether two string are a permutation of each other or not.
    # Q1.
    def str(a,b):
        x=[]
        for i in b:
            if i in a:
                x.append(i)
        print(len(x)==len(a))
    str(input('Str1:'), input('Str2:'))
if p==2:
    # count trailing zeroes in factorial of a number.
    # Q2.
    def Num(n):
        global x
        x=n
        y=1
        global count
        count=0
        i=1
        while(n>=y):
            y=y*5
            count=count+n//5**i
            i=i+1
        return count
    Num(int(input("Enter A Number:")))
    print('Count of trailing 0s in',x,'! is', count)
if p==3:
    # check Armstrong Number
    # Q3.
    n=input('Enter Numbers')
    def power(n):
        if n=='':
            return 0
        else:
            return 1+power(n[1:])
    p=power(n)
    def order(n):
        x=[]
        y=int(n)
        for i in range(p):
            z=y%10
            x.append(z)
            y=y//10
        return x
    a=order(n)
    def Armstrong(n):
        b=0
        for i in a:
            b+=i**p
        print(b==int(n))
    Armstrong(n)
if p==4:
    # sum of all the elements of a list
    # Q4.
    # Enter Elements like 12,45,78,16
    list1=list(map(int,input("Enter Elements with ','(comma):").split(',')))
    def sum(list,size):
        if size==0:
            return 0
        else:
            return list1[size-1]+sum(list,size-1)
    sum=sum(list1,len(list1))
    print("Sum of all elements in given list: ", sum)
if p==5:
    #program to reverse a date in the format "yyyyMMdd"
    # Q5
    def reverse(n):
        if len(n)==1:
            return n
        else:
            return reverse(n[1:])+n[0]
    print(reverse(input("Enter A Date (YYYYMMDD):")))
if p==6:
    # Sum of G.P.
    # Q6.
    n=int(input("Enter Number of terms, n:"))
    a=int(input("Enter First term, a:"))
    r=int(input("Enter Common ratio, r:"))
    def sum(n,s=0):
        if n==1:
            return a
        elif n==0:
            return 0
        elif n<0:
            print('Term cannot be negative')
        else:
            return sum(n-1,a*r**(n-1))+a*r**(n-1)
    print('The sum of the first ',n,' terms in the sequence is',sum(n))
if p==7:
    '''program that takes in the upper limit and prints all numbers within the
       given range in increasing order.'''
    # Q7.
    def Num(n):
        if n>0:
            Num(n-1)
            print(n)
    Num(int(input("Enter A Upper Limit:")))
if p==8:
    '''program that takes in the upper limit and prints all numbers within the
       given range in decreasing order.'''
    # Q8.
    def Num(n):
        if n<=0:
            return
        else:
            print(n)
            return Num(n-1)
    Num(int(input("Enter A Upper Limit:")))
if p==9:
    # Factorial of A Integer
    # Q9.
    n=int(input("Enter A Number:"))
    def Factorial(n):
        if n==0:
            return 1
        elif n<0:
            return print('Factorial is not defined for negative Numbers')
        elif n==1:
            return 1
        else:
            return n*Factorial(n-1)
    output=Factorial(n)
    print('The factorial of',n,'=',output)
if p==10:
    # recursive python program to print the fibonacci series upto n terms.
    # Q10.
    n=int(input("Enter A Number:"))
    def fibonacci(n):
        if n<=1:
            return n
        else:
            return fibonacci(n-1)+fibonacci(n-2)
    for i in range(n):
        print(fibonacci(i),end='')
        if i<n-1:
            print(', ',end='')
    
if p==11:
    # recursive python program to return gcd of a and b
    # Q11.
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    def GCD(a,b):
        if a==0:
            return b
        elif b==0:
            return a
        return GCD(b,a%b)
    output=GCD(a,b)
    print('GCD of',a,'and',b,'is',output)

if p==12:
    # recursive python program to return lcm of a and b
    # Q12.
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    def GCD(a,b):
        if a==0:
            return b
        elif b==0:
            return a
        return GCD(b,a%b)
    output=GCD(a,b)
    def LCM(a,b):
        return int(a*b/output)
    print('LCM of',a,'and',b,'is',LCM(a,b))
if p==13:
    print('There is two method please select one:')
    m=int(input('Enter Method No. 1 or 2 :'))
    if m==1:
    # Binomial Coefficient C(n, k)
    # Q13.
        n=int(input("Enter 'n' :" ))
        k=int(input("Enter 'k' :" ))
        def Binomial(n,k):
            if k>n:
                return 0
            elif (k==0 or k==n):
                return 1
            else:
                return Binomial(n-1,k-1)+Binomial(n-1,k)
        output=Binomial(n,k)
        print('Value of C(',n,',',k,') is', output)
    if m==2:
        def factorial(n):
            if n==0:
                return 1
            else:
                return n*factorial(n-1)
        def Binomial(n,k):
            if k>n:
                return 0
            else:
                return int(factorial(n)/(factorial(n-k)*factorial(k)))

        n=int(input('Enter n:'))
        k=int(input("Enter k:"))
        output=Binomial(n,k)
        print('Value of C(',n,',',k,') is',output)
if p==14:
    # program to find Minimum element of array
    # Q14.
    a=list(map(int,input('Enter Elements with "," :').split(',')))
    print(set(a))
    n=len(a)
    def Min(a,n):
        if n==1:
            return a[0]
        return min(a[n-1],Min(a,n-1))
    print('Min=',Min(a,n))
if p==15:
    # program to find Maximum element of array
    # Q15.
    a=list(map(int,input('Enter Elements with "," :').split(',')))
    print(set(a))
    n=len(a)
    def Max(a,n):
        if n==1:
            return a[0]
        return max(a[n-1],Max(a,n-1))
    print('Max=',Max(a,n))

if p==16:
    # find out and return the number of digits present in a number
    # Q16.
    n=input("Enter Number")
    def Digit(n):
        if len(n)==1:
            return 1
        else:
            return 1+Digit(n[1:])
    output=Digit(n)
    print('Digits present in',n,'=',output)
if p==17:
    s=input("Enter Section a,b,c,d,e:")
    if s=='a':
        # calculating the factorial of a number
        def fact(num):
            if num==0:
                return 1
            else:
                return num*fact(num-1)
        num=int(input("Enter a Number:"))
        print('Factorial of',num,'=',fact(num))
        print("""It is recursive type function. In it if number equal to 0 then it return 1 else number
multiple with (number-1), (number-2)...and so on it repeat till number is not equal to 0""")
    if s=='b':
        def test(i,j):
            if i==0:
                return j
            else:
                return test(i-1,i+j)
        print('Output:',test(4,7))
        print("""It is recursive type function. In it if 'i' equal to 0 then it return value of 'j' else
i' equal to 'i-1' and 'j' equal to 'i+j' and it repeat till 'i' is not equal to 0 and final output is 'j'""")
    if s=='c':
        l=[]
        def convert(b):
            if (b==0):
                return 1
            dig=b%2
            l.append(dig)
            convert(b//2)
        convert(6)
        l.reverse()
        for i in l:
            print(i, end="")
        print("""\nIn it 'b'= 6, dig = 0 then '0' append in list 'l', now 'b'=6//2=3 and function repeat
now dig=1 and b=3//2=1 and it repeat till b=0, using reverse function reverse the elements of
list 'l' and using for loop, element of list 'l'print in one line and output is 110""")
    if s=='d':
        def fun(n):
            if (n>100):
                return n-5
            return fun(fun(n+11));

        print(fun(45))
        print("""In it n=45 if condition is false and it go to fun(fun(45+11)) and function repeat
for fun(56) then fun(56+11) and it's repeat till n is not greater 100 and output is 100 """)
    if s=='e':
        def a(n):
            if n==0:
                return 0
            else:
                return n*a(n-1)
        def b(n,tot):
            if n==0:
                return tot
            else:
                return b(n-2,tot-2)
        print("""In it both function are tail recursive because in return statement it call function
again and again""")
if p==18:
    # program Raise a TypeError if x is not an integer
    x = input('Enter String for TypeError:')
    if not type(x) is int:
        raise TypeError("Only integers are allowed")
if p==19:
    # try-except for division of x by y
    def divide(x, y):
        try:
            result = x // y
            print("Yeah ! Your answer is :", result)
        except ZeroDivisionError:
            print("Sorry ! You are dividing by zero")
            
    divide(int(input("Enter First Number:")), int(input("Enter Second Number:")))
