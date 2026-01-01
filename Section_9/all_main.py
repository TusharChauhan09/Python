# # 1  G.C.D or H.C.F

# def calcHCF(x,y):
#     if x>y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1,smaller+1):
#         if ((x%i==0) and (y%i==0)):
#             HCF = i
#     return HCF

# print(calcHCF(12,30))

# n1 = int(input("enter1: "))
# n2 = int(input("enter2: "))
# if n1>n2:
#     great = n1
# else:
#     great = n2
#     for i in range(1,great+1):
#         if ((n1%i==0)and (n2%i==0)):
#             LCM = i

# print(LCM)

def rec(n):
    if n==1:
        return 0
    if n==0:
        return 1
    else:
        return (rec(n-1)+rec(n-2)) 

n=int(input("enter: "))
for i in range(1,n+1):
    print(rec(i))





# # 2 Fibonarcci series

# n = int(input("Enter the number: "))
# x = 0
# y = 1
# z = 0
# while(z<=n):
#     print(z)
#     x=y
#     y=z
#     z=x+y


# # 3 Armstrong Number 

# i = int(input("Enter Number: "))
# o = i
# sum = 0
# while(i>0):
#     sum = sum + (i%10)**3           # 0 + (3 * 3 * 3) = 27   // 27 + (5*5*5) =152 // 152 + 1 =153
#     i = i//10

# if o == sum:
#     print("Number is a armstrong: ")
# else:
#     print("Number is not armstrong")


# 4 Prime no.

# n = int(input("enter: "))
# if n==1:
#     print("not a prime no. as 1")
# if n>1:
#     for i in range(2,n):
#         if (n%i==0):
#             print("composite no .")
#             break
#     else:
#         print("prime no. ")

# # 5 Vowel and consonants

# a = input("Enter: ")
# vowel = 0
# cons = 0
# for i in range(0,len(a)):
#     if (a[i]!=" "):
#         if a[i]=="a" or a[i]=="i" or a[i]=="o" or a[i]=="u" or a[i]=="e" or a[i]=="A" or a[i]=="E" or a[i]=="I" or a[i]=="O" or a[i]=="U" :
#             vowel = vowel+1
#         else:
#             cons=cons+1
# print(vowel)
# print(cons)

# # 6 Sum of digits of number

# n = int(input("enter: "))
# sum = 0
# while(n>0):
#     sum = sum + n%10
#     n = n//10
# print("sum of digits: ",sum)


# # 6 Strong numbers

# n = int(input("enter the number: "))
# s = 0
# num = n
# while(n>0):
#     digit = n%10
#     fact = 1
#     for i in range(1,digit+1):
#         fact = fact*i
#     s = s + fact
#     n = n//10
# if (s==num):
#     print("strong number")
# else:
#     print("not a strong number")

# # 7 Palindrome number

# i = int(input("Enter: "))
# rev = 0
# x = i
# while(i>0):
#     rev = (rev*10) + i%10
#     i = i//10

# if x == rev:
#     print("Palindrone number")
# else:
#     print("not a palindrome number")

# i = int(input("Enter: "))
# i = str(i)
# rev = i[::-1]
# if i == rev:
#     print("Palandrome no.")
# else:
#     print("not a palandrome")


# # 8  Biggest number

# num1 = int(input("num1: "))
# num2 = int(input("num2: "))
# num3 = int(input("num3: "))
# if num1>num2 and num1>num3:
#     max_num = num1
# elif num2>num1 and num2>num3:
#     max_num = num2
# else:
#     max_num = num3
# print(max_num)


# # 9 Floyd's Triangle


# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print(" ")

# n = int(input("Enter the number: "))       # increasing triangle
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print(" ")

# n = int(input("Enter the number: "))       # decreasing triangle
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print(" ")


# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(i,n):                   # dec space inc *
#         print(" ",end =" ")
#     for j in range(i+1):
#         print("*",end = " ")
#     print(" ")


# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(i+1):                   # inc * inc space
#         print(" ",end =" ")
#     for j in range(i,n):
#         print("*",end = " ")
#     print(" ")

# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     print()

# n = int(input("Enter the number: "))
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     print()



# n = int(input("Enter the number: "))     
# for i in range(n):
#     for j in range(i+1):
#         print("1",end=" ")
#     print()


# n = int(input("Enter the number: "))       
# p = 1
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#     p = p+1
#     print()

# n = int(input("Enterv the number: "))
# p = n
# for i in range(n):
#     for j in range(i,n):
#         print(p,end=" ")
#     p = p-1
#     print()

# n = int(input("Enter the number: "))      
# for i in range(n):
#     p = 1 
#     for j in range(i+1):
#         print(p,end=" ")
#         p = p+1
#     print()

# n = int(input("Enter the number: "))
# for i in range(n):
#     p = 1
#     for j in range(i+1):                   
#         print(" ",end =" ")
#     for j in range(i,n):
#         print(p,end = " ")
#         p = p+1
#     print(" ")


# n = int(input("Enter the number: "))
# k = 5
# for i in range(n):
#     p = k
#     for j in range(i):                  
#         print(" ",end =" ")
#     for j in range(i,n):
#         print(p,end=" ")
#         p = p-1
#     k = k-1
#     print(" ")

# # Floyd triangle

# n = int(input("Enter the number: "))
# p = 1  
# for i in range(n): 
#     for j in range(i+1):
#         print(p,end=" ")
#         p = p+1
#     print()

# # Extra question 
# a = input("Enter: ")
# x=len(a)
# for i in range(x):
#     for j in range(i+1):
#         print(a[j],end="")
#     print()

# # 10. perfect number
# n = int(input("Enter: "))
# sum = 0
# i = 1
# while i<n:
#     if n%i==0:
#         sum = sum + i
#     i = i+1
# if sum == n:
#     print("perfect number")
# else:
#     print("not a perfect number")

# # 11. Pascal Triangle

# def pascaltriangle(m):

#     a = [[] for i in range(m)]
#     for i in range(m):
#         for j in range(i+1):
#             if(j<i):3
#                 if(j==0):
#                     a[i].append(1)
#                 else:
#                     a[i].append(a[i-1][j]+a[i-1][j-1])
#             elif(j==i):
#                 a[i].append(1)
#     return a

# print(pascaltriangle(5))


# # important example 
# a = input("Enter 1: ").lower()
# b = input("Enter 2: ").lower()
# a1 = a.split()
# b1 = b.split()
# for i in a1:
#     for j in b1:
#         if i==j:
#             print(j)

# n = input("enter: ")
# if n is n.lower():
#     m = ord(n)
#     print("here: ",chr(m+1))



# n = input("enter: ").split()
# x = int(input("enter2: "))
# for i in n:
#     for j in n:
#         if i==j:
#             print(j)
#             print(n.count(j,x))


# def pascaltriangle(n):

#     a = [[] for i in range(n)]
#     for i in range(n):
#         for j in range(i+1):
#             if(j<i):
#                 if(j==0):
#                     a[i].append(1)
#                 else:
#                     a[i].append(a[i-1][j]+a[i-1][j-1])
#             elif(j==i):
#                 a[i].append(1)
#     return a

# print(pascaltriangle(5))


# n = input("Enter: ")
# vowel = 0
# con = 0
# for i in n:
#     if  i=="a" or i=="i" or i=="o" or i=="u" or i=="e" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U" : 
#         vowel = vowel+1
#     else:
#         con = con + 1
# print(vowel)
# print(con)



# n = int(input("enter: "))
# sum = 0
# while(n>0):
#     sum = sum + n%10
#     n = n//10
# print("sum of digits: ",sum)


# l = []
# n=int(input("enter: "))
# for i in range(n):
#     x=int(input("enter: "))
#     l.append(x)
# print(l)
# print(min(l))