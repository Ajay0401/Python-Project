print('========================================================================')
print('''Q1. Find the MAX of three numbers
Q2. Reverse a String
Q3. Calculate the factorial of a number
Q4. Check whether a number is in a given range
Q5. Calculate the number of upper case letters and lower case letters
Q6. New list with unique elements of the first list
Q7. Function to check whether a string is a pangram or not.
Q8. Program to access a function inside a function.
Q9. Program to detect the number of local variables declared in a function.
Q10. Function that prints out the first n rows of Pascal’s triangle
Q11. Prints the word in a hyphen-separated sequence after sorting them alphabetically
Q12. Print a list where the values are square of numbers
Q13. Addition and Subtraction of two variables
Q14. Print employee name and salary
Q15. Calculate the sum of numbers from 0 to n
Q16. Different name to function and call it through the new name
Q17. Function to multiply all the numbers in the list.
Q18. Check if the number is prime or not.
Q19. Checks whether a string is palindrome or not.
Q20. Function that takes x as argument and returns y. (Formula: y = 6x^2 + 3x + 2)
Q21. Function x(n) for computing an element in the sequence, x(n) = n^2 + 1''')
print('========================================================================')
p=int(input("Enter Question No."))
print('========================================================================')
if p==1:
# Find the MAX of three numbers
    def Max(a, b, c):
        if a>=b and a>=c:
            max=a
        elif b>=a and b>=c:
            max=b
        else:
            max=c
        return max
    print('Maximum Number:', Max(int(input("Enter First No.")),int(input("Enter Second No.")),int(input("Enter Thrid No."))))
if p==2:
    # Reverse a String
    def reverse(string):
        s=''
        for i in range(len(string)-1,-1,-1):
            s=s+string[i]
        return s
    X=reverse(input("Enter String:"))
    print("Reverse String:",X)
if p==3:
    # Calculate the factorial of a number
    def factorial(n):
        global y
        y=n
        if n<0:
            print('factorial is not defined for negative number')
        
        else:
            f=1
            for i in range(1,n+1):
                f=f*i
            return f
    x=factorial(int(input('Enter a Number:')))
    if y>=0:
        print('Factorial of',y,'=',x)
if p==4:
    # Check whether a number is in a given range
    x=int(input("Enter First Number of Range:"))
    y=int(input("Enter Last Number of Range:"))
    def check(n):
        if x<=n<=y:
            print("Number is in Range")
        else:
            print("Number is not in Range")
        return
    check(int(input("Enter number for check:")))
if p==5:
    # Calculate the number of upper case letters and lower case letters
    def count(string):
        global upper
        upper=0
        global lower
        lower=0
        for i in string:
            if 65<=ord(i)<=90:
                upper+=1
            if 97<=ord(i)<=122:
                lower+=1
        return
    count(input("Enter String:"))
    print("No. of uppercase characters:",upper)
    print("No. of lowercase characters:",lower)
if p==6:
    print('# Enter element in list like: AABC1112223345')
    # function that takes a list and returns a new list with unique elements of the first list.
    def List(list1):
        list2=[ ]
        for i in list1:
            if i not in list2:
                list2.append(i)
        print('List:',list1)
        print('List with Unique Elements:',list2)
        return
    List(list(input("Enter elements in list:")))
if p==7:
    # Function to check whether a string is a pangram or not.
    def pangram(string):
    # Convert into Upper Case
        x=''
        for i in string:
            if 65<=ord(i)<=90:
                x=x+i
            elif 97<=ord(i)<=122:
                x=x+chr(ord(i)-32)
        print(len(set(list(x)))==26)
    pangram(input('Enter String:'))
if p==8:
    # Program to access a function inside a function.
    def add(x,y):
        print('Addition:', x+y)
        def multiply(x,y):
            print("Multiplication:",x*y)
        multiply(4,5)
    add(4,5)
if p==9:
    # Program to detect the number of local variables declared in a function.
    def function():
        a=4
        b=8
        string='Hi'
    print('Local Variables:',function.__code__.co_nlocals)
if p==10:
    # Function that prints out the first n rows of Pascal’s triangle
    def Pascal(n):
        for i in range(1,n + 1):
            a = 1
            for j in range(1, i+1):
                print(a, end=' ')
                a = int(a * (i-j)/j)
            print("")
    Pascal(int(input("Enter Pascal Triangle Height:")))
if p==11:
    # Prints the word in a hyphen-separated sequence after sorting them alphabetically
    def word(x):
        y=x.split('-')
        y.sort()
        z=''
        for i in range(len(y)):
            z+=y[i]
            if i<len(y)-1:
                z+='-'
        print('Sorted:', z)
    word(input("Enter word with '-':"))
if p==12:
    # Print a list where the values are square of numbers
    def square():
        x=[ ]
        for i in range(1,31):
            x.append(i**2)
        print('Squares:',x)
    square()
if p==13:
    # Addition and Subtraction of two variables
    def function(a, b):
        print("Addition:",a+b)
        print("Subtraction:",a-b)
    function(int(input('Enter First Variable Value:')),int(input('Enter Second Variable Value:')))
if p==14:
    # Print employee name and salary
    def Employee(Name, Salary):
        if Salary=='':
            print('Employee',Name,'Salary is 9000')
        else:
            print('Employee',Name,'Salary is',Salary)

    Employee(input('Enter Employee Name:'),input("Enter Employee Salary / Left Empty:"))
if p==15:
    # Calculate the sum of numbers from 0 to n.
    def sum(n):
        if n<=1:
            return n
        else:
            return n+sum(n-1)
    n=int(input("Enter a Number:"))
    if n<0:
        print("Enter a positive number")
    else:
        print("The sum from 0 to", n,"is",sum(n))
if p==16:
    # different name to function and call it through the new name.
    def student(Name, Age):
        print('Name:',Name)
        print("Age:", Age)

    showstudent=student
    showstudent(input("Enter Name:"),input('Enter Age:'))
if p==17:
    print('Enter Number like 1,2,15,45,60')
    # function to multiply all the numbers in the list.
    x=list(map(int, input('Enter Numbers with comma:').split(',')))
    def Multiplication():
        a=1
        for i in x:
            a=a*i
        print('Multiplication of list Elements:',a)
    print(x)
    Multiplication()
if p==18:
    # Check if the number is prime or not.
    def num(n):
        if n<2:
            print(n,'is not prime')
        else:
            flag=0
            for i in range(2,n//2+1):
                if n%i==0:
                    flag=1
            if flag==1:
                print(n,'is not prime')
            else:
                print(n, 'is prime')
    num(int(input('Enter A Number:')))
if p==19:
    # Checks whether a string is palindrome or not.
    def palindrome(string):
        a=''
        for i in range(len(string)-1,-1,-1):
            a=a+string[i]
        if a==string:
            print('String is Palindrome')
        else:
            print('String is not Palindrome')
    palindrome(input("Enter A String:"))
if p==20:
    # Function that takes x as argument and returns y. (Formula: y = 6x^2 + 3x + 2)
    def equation(x):
        y=6*x**2+3*x+2
        return y
    print('y=',equation(int(input("Enter a Number:"))))
if p==21:
    # Function x(n) for computing an element in the sequence, x(n) = n^2 + 1
    def function(n):
        x=n**2+1
        return x
    result=function(int(input("Enter A Number:")))
    print('x=',result)
    
    
