x='''Let me be your hero
Would you dance
If I asked you to dance?
Would you run
And never look back?
Would you cry
If you saw me crying?
And would you save my soul, tonight?
Would you tremble
If I touched your lips?
Would you laugh?
Oh please tell me this.
Now would you die
For the one you loved?
Hold me in your arms, tonight.
I can be your hero, baby.
I can kiss away the pain.
I will stand by you forever.
You can take my breath away.
Would you swear
That you'll always be mine?
Or would you lie?
Would you run and hide?
Am I in too deep?
Have I lost my mind?
I don't care...
You're here tonight.
I can be your hero, baby.
I can kiss away the pain.
I will stand by you forever.
You can take my breath away.
Oh, I just want to hold you.
I just want to hold you, oh, yeah.
Am I in too…'''
print(x)
print('========================================================================')
# Programs list
print('Programs List:')
print('''1. Uppercase Letter
2. Lowercase Letter
3. First letter Capital and Other Small
4. Find Word with Index
5. Replace word
6. Remove word
7. Count word Repeatation
8. Count Total Words
9. Count Unique Words
10. Count total Characters
11. Count Unique Characters
12. Count Unique Capital Alphabetic Characters
13. Count Unique Small Alphabetic Characters
14. Calculate Length of String
15. Count Character Frequency
16. Finding Longest Word
17. Finding Smallest Word
18. Finding length of words
19. Sorted words in ascending order
20. Sorted words in descending order
21. Remove n th index word
22. Insert word at n th index
23. Remove Character
24. Add a Prefix Character to all of the lines in a string
25. Reverse String
26. Reverse Words
27. Check if a string contains all letters of the alphabet
28. Count and display the vowels of a given string
29. Count Most Repeated Word
30. Remove spaces from a given string
31. Find the maximum occurring character in a given string.
32. Remove Special Character from a given string.
''')
print('========================================================================')
# Enter Number for corresponding Program.
p=int(input("Enter Program Number:"))
print('========================================================================')
#Program for Uppercase letter.
if p==1:
    y=x.split(' ')
    z=''
    for i in y:
        for j in range(len(i)):
            if (ord(i[j])>=97 and 122>=ord(i[j])):
                z=z+chr(ord(i[j])-32)
                if j==(len(i)-1):
                    z=z+' '
            else:
                z=z+i[j]
                if j==(len(i)-1):
                    z=z+' '        
    print(z)
# Program for lowercase Letter.
if p==2:
    y=x.split(' ')
    z=''
    for i in y:
        for j in range(len(i)):
            if (ord(i[j])>=65 and 90>=ord(i[j])):
                z=z+chr(ord(i[j])+32)
                if j==(len(i)-1):
                    z=z+' '
            else:
                z=z+i[j]
                if j==(len(i)-1):
                    z=z+' '

    print(z)
# Program for First letter Capital and Other Small.
if p==3:
    y=x.split(' ')
    z=''
    for i in y:
        if (ord(i[0])>=97 and 122>=ord(i[0])):
            z=z+chr(ord(i[0])-32)
            for j in range(1,len(i)):
                z=z+i[j]
            if j==(len(i)-1):
                z=z+' '
        else:
            for j in range(0,len(i)):
                z=z+i[j]
            if j==(len(i)-1):
                z=z+' '
        
    print(z)
# Program for Find Word with Index.
if p==4:
    z=input("Enter Word For Find:")
    print("Here, Indexing is according to words, Whitespace is not include in indexing")
    y=x.split()
    flag=0
    for i in range(0,len(y)):
        if (y[i]==z):
            flag=1
            print('Word is Found at Index:',i)
    if flag==0:
        print("Word is not found")
            
# Program for Replace word.
if p==5:
    y=input("Enter Word, Which you want to Replace:")
    w=input("Enter Replaced Word:")
    a=x.split('\n')
    b=[]
    for j in a:
        b.append(j.split(' '))
    for i in b:
        z=''
        for j in i:
            if j==y:
                z=z+w+' '
            else:
                z=z+j+' '
            if (i.index(j)==len(i)-1):
                print('\n')
        print(z)
# Program for Remove word.
if p==6:
    y=input("Enter Word, Which you want to Remove:")
    a=x.split('\n')
    b=[]
    for j in a:
        b.append(j.split(' '))
    for i in b:
        z=''
        for j in i:
            if j==y:
                z=z
            else:
                z=z+j+' '
            if (i.index(j)==len(i)-1):
                print('\n')
        print(z)

# Program for count word Repeatation.
if p==7:
    y=input("Enter Word:")
    z=x.split()
    count=0
    for i in z:
        if i==y:
            count=count+1
    print('"',y,'"', 'Repeat', count, 'Time')
# Program for Count Total Words.
if p==8:
    y=x.split()
    print('Total Words:', len(y))
# Program for Count Unique Words.
if p==9:
    y=x.split()
    z=set(y)
    print('Unique Words:', sorted(z))
    print('Total Words:', len(z))
# Program for Count Total Alphabetic Characters.
if p==10:
    y=''
    for i in x:
        if ((ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90)):
            y=y+i
    print('Total Characters:',len(y))
# Program for Count Unique Alphabetic Characters.
if p==11:
    z=set()
    for i in x:
        if ((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122)):
            z.add(i)
    print(sorted(z))
    print('Unique Letters:',len(z))
# Program for Count Unique Capital Alphabetic Characters.
if p==12:
    z=set()
    for i in x:
        if ((ord(i)>=65 and ord(i)<=90)):
            z.add(i)
    print(sorted(z))
    print('Capital Characters:',len(z))
# Program for Count Unique Small Alphabetic Characters.
if p==13:
    z=set()
    for i in x:
        if ((ord(i)>=97 and ord(i)<=122)):
            z.add(i)
    print(sorted(z))
    print('Small Letters:',len(z))
#Program for Calculate Length of String.
if p==14:
    length=0
    for i in x:
        length=length+1
    print("Length of String:",length)
#Program for Count Character Frequency.
if p==15:
    F={}
    y=[]
    z=[]
    b={}
    for i in x:
        if i not in y:
            y.append(i)
    for j in x:
        z.append(j)
    if ('\n' in (y or z)):
        y.remove('\n')
        z.remove('\n')
    for i in y:
        count=0
        for j in x:
            if i==j:
                count=count+1
        F.update({i:count})
    a=sorted(F)
    for i in a:
        b.update({i:F.get(i)})
    print(b)
# Program for Finding Longest Word.
if p==16:
    y=x.split()
    max=0
    for i in y:
        if len(i)>max:
            max=len(i)
            z=i
    print('Lognest Word:','"',z,'"',', ' 'length:', max)
# Program for finding smallest word
if p==17:
    y=x.split()
    z=[]
    for i in y:
        z.append(len(i))
    print('"',y[z.index(min(z))],'"','length:', min(z))
# Program for finding length of words.
if p==18:
    y=x.split()
    w={}
    for i in y:
        len=0
        for j in i:
            len=len+1
        w.update({i:len})
    print('{Word:Length}', w)
# Program for sorted words in ascending order.
if p==19:
    y=x.split()
    z=sorted(y)
    s=''
    for i in z:
        s=s+i+' '
    print(s)
# Program for sorted words in descending order.
if p==20:
    y=x.split()
    z=sorted(y, reverse=True)
    s=''
    for i in z:
        s=s+i+' '
    print(s)
# Program for remove n th index word.
if p==21:
    print("Here, Indexing is according to words, Whitespace is not include in indexing.")
    y=x.split(' ')
    Index=int(input("Enter Index of Word which you want to remove:"))
    z=''
    for i in y:
        if y.index(i)==Index:
            a=i
            y.remove(i)
        z=z+i+' '
    print('Removed Word:', a)
    print(z)
# Program for insert word at n th index.
if p==22:
    print("Here, Indexing is according to words, Whitespace is not include in indexing.")
    y=x.split(' ')
    Index=int(input("Enter Index for insert word:"))
    word=input("Enter Word for insert:")
    z=''
    for i in y:
        if y.index(i)==Index:
            y.insert(Index,word)
    for j in y:
        z=z+j+' '
    print(z)
# Program for Remove character.
if p==23:
    z=input("Enter Character for Remove:")
    y=''
    for i in x:
        if i==z:
            y=y
        else:
            y=y+i
    print(y)
# Program to add a prefix text to all of the lines in a string.        
if p==24:
    y=input("Enter Special Character")
    z=x.split('\n')
    for i in z:
        print(y,' ', i)
# Program for Reverse String.
if p==25:
    y=''
    for i in range(len(x)-1,-1,-1):
        y=y+x[i]
    print(y)
# Program for Reverse Words in String.
if p==26:
    y=x.split('\n')
    z=[]
    w=''
    for i in y:
        z.append(i.split(' '))
    for i in z:
        for j in i:
            for k in range(len(j)-1,-1,-1):
                w=w+j[k]
            w=w+' '
        w=w+'\n'
    print(w)
# Program for check if a string contains all letters of the alphabet.
if p==27:
    y=[]
    z=[]
    for i in x:
        if (ord(i)>=65 and ord(i)<=90):
            y.append(i)
        if (ord(i)>=97 and ord(i)<=122):
            z.append(i)
    if (len(set(y)) or len(set(z)))==26:
        print('String Contains All Letters of the Alphabet')
    else:
        print('String Not Contains All Letters of the Alphabet')
    print('Available Capital Alphabets:',len(set(y)),';',sorted(set(y)))
    print('Available Small Alphabets:',len(set(z)),';',sorted(set(z)))
# Program for count and display the vowels of a given string.
if p==28:
    y=['a','A','e','E','i','I','o','O','u','U']
    z={}
    for i in y:
        count=0
        for j in x:
            if i==j:
                count=count+1
        z.update({i:count})
    print(z)
# Program for Count Most Repeated Word.
if p==29:
    w=x.split()
    y=set(w)
    z=[]
    for i in y:
        count=0
        for j in w:
            if i==j:
                count=count+1
        z.append(count)
    print('"',w[z.index(max(z))],'"', max(z),'time')
# Program for remove spaces from a given string.
if p==30:
    y=''
    for i in x:
        if i==' ':
            y=y
        else:
            y=y+i
    print(y)
# Program for find the maximum occurring character in a given string.
if p==31:
    y=[]
    z=[]
    for i in x:
        if i not in y:
            y.append(i)
    y.remove(' ')
    for i in y:
        count=0
        for j in x:
            if i==j:
                count=count+1
        z.append(count)
    print('"',y[z.index(max(z))],'"', max(z),'time')
# Program for remove special character from a given string.
if p==32:
    y=''
    for i in x:
        if (33<=ord(i)<=47 or 58<=ord(i)<=64 or 91<=ord(i)<=96 or 123<=ord(i)<=127):
            y=y
        else:
            y=y+i
    print(y)
