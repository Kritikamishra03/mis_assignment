#Q.1

#to take inout from user

string1= input("Enter First string: ")
print(string1)
string2= input("Enter second string: ")
print(string2)
string3 = input("Enter the third string: ")

#concatinate string2 and string1
c = string2 + string1

#to check if the reverse string is identical to string 3
if string3 == c:
    print("The two strings are equal in the reverse order")
else:
    print("They are not equal")

############################################################################

#Q.2
"""
max : maximum number
min : Minimum number
avg : average number
mdn : median number
lst : empty list

"""

n = int(input("Do you want to use 4 or 5 integers:"))

lst =[]
#to take input as a 4 from user
if n==4:
    for i in range(0,4):
        if i==0:
            a = int(input("Enter First No. "))
            lst.append(a)
        elif i==1:
            b = int(input("Enter Second No. "))
            lst.append(b)
        elif i==2:
            c = int(input("Enter Third No. "))
            lst.append(c)
        elif i==3:
            d = int(input("Enter fourth No. "))
            lst.append(d)
            
#to take input as a 5 from user           
elif n==5:
    for i in range(0,5):
        if i==0:
            a = int(input("Enter First No. "))
            lst.append(a)
        elif i==1:
            b = int(input("Enter Second No. "))
            lst.append(b)
        elif i==2:
            c = int(input("Enter Third No. "))
            lst.append(c)
        elif i==3:
            d = int(input("Enter fourth No. "))
            lst.append(d)
        elif i==4:
            e = int(input("Enter fifth No. "))
            lst.append(e)    
else:
    print("Invalid input")
    
print(lst)
l= len(lst)
#defined variables
s =0
avg =0
maxm=0
minm =lst[0]


#check which number is maximum and minimum
for i in lst:
    s =s+i #for increment
    if i >= maxm:
        maxm=i
    else:
        pass
        
    if i <= minm :
        minm=i
    else:
        pass

  
#Average
avg = float(s / l) 
lst.sort()

x = l//2

if l%2 ==0:
    m1 = lst[x]
    m2 = lst[x - 1]
    mdn = (m1+m2)/2
else:
    mdn = lst[x]
    
if n==4:   
    print("The average of four numbers is",avg)
   
    print("The minimum of the four numbers is:",minm)
    print("The maximum of the four numbers is:",maxm)
    
        
    print("The median of the four number ",mdn)
else:
    print("The average of five numbers is",avg)
    
    print("The minimum of the five numbers is:",minm)
    print("The maximum of the five numbers is:", maxm)
    
        
    print("The median of the five number ",mdn)
    
#######################################################################

#Q.3

def prime():
    num = input("Enter positive integer")

    if num.isnumeric():
        num = int(num)
        c=0
        if num <0:
            print("Error: You did not enter a positive integer")
        elif num ==0 or num ==1:
            print("It is neither prime nor composite")
        elif num>1 :
            for i in range(2,num+1):
                if num%i ==0:
                    c=c+1
            if c ==1:
                print("It's a Prime")
            else:
                print("It's a Composite")
        else:
            print("Error: You did not enter a positive integer")
    else:
        print("Error: You did not enter a positive integer")

ans = 'y'
while ans =='y':
    prime()
    ans= input("do you want to continue: y/n :")
	
########################################################################

#Q.4

def rect_coordinate():
    x1 = int(input("Enter x1 coordinate :"))
    y1 = int(input("Enter y1 coordinate :"))
    x2 = int(input("Enter x2 coordinate :"))
    y2 = int(input("Enter y2 coordinate :"))
    x = int(input("Enter x coordinate :"))
    y = int(input("Enter y coordinate :"))
    flag=0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if i ==x and j == y:
                flag =1
    
    if flag >0:
        print("Yes, it lies within the rectangle")
    else:
        print("Not, it doesn’t lie in the rectangle")
        
ans = 'y'
while ans =='y':
    rect_coordinate()
    ans= input("do you want to continue: y/n :")
print("Goodbye!!")

##########################################################################

#Q.5
def Interest():
    time = int(input("Enter time period :"))
    rate = float(input("Enter rate of interest :"))
    principle = float(input("Enter principle :"))
    
    # if rate.isdecimal():
        # rate = float(rate)
    # else:
        # rate = int(rate)
        
    # if principle.isdecimal():
        # principle = float(principle)
    # else:
        # principle = int(principle)
    
    simple_interest = (time*rate*principle)/100
    print("Simple Interest need to be paid:",simple_interest)
    # print(type(principle))
    # print(type(rate))
    return principle+simple_interest
        
ans = 'y'
while ans =='y':
    amounts = Interest()
    print("Final Amount need to be paid:", amounts)
    ans= input("do you want to continue: y/n :")
print("Goodbye!!")

##############################################################################