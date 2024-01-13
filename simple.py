# def cir(r):
#     pi = 3.14
#     return pi*(r*r)
# print("ar of circle is",cir(5))


# import math
# def cir(r):
#     area = math.pi*pow(r,2)
#     return print(area)

# cir(5)


# def prime(n):
#     prime = []
#     for i in range (2,n):
#         if n%i == 0:
#            return  False
#         else:
#             return True
# print(prime(7))



# def prime(n):
#     pm = []
#     s =0
#     for i in range(2,n):
#         if n%i == 0:
#             s = 0
#             break
#         else :
#             s = 1
            
#     if s == 1:
#         pm.append(i)
                
#     return print("no") if len(pm)==0 else print("yes")

# prime(7)


# n = 12
# if n>1:
#     for i in range(2,int(n/2)+1):
#         if n%i == 0:
#            print(n,"is not a prime number")
#            break   
#     else:
#         print(n,"is a prime number")
# else:
#     print(n,"is not a prime number")       
        
    
# n = 12
# if n > 0 :
#     for i in range(2,n):
#         if n%i == 0:
#             print("NO its not a Prime Number")
#             break
#     else:
#         print("YES its a Prime Number")
            
            
# else :
#     print("NO its not a Prime Number")
    


# n = 17
# flag = 0
# prime=[]
# if n > 0 :
#     for i in range(2,n):
#         if n%i == 0:
#             s = 0
           
#             break
#     else:
#         s = 1
        
# else :
#     print("NO its not a Prime Number")
    
# if s == 0:
#     print("NO its not a Prime Number")
# elif s==1:
#     print("YES its a Prime Number")
            


# def prime(n):
#     if n <= 1:
#         return print("NO its not a Prime Number")
#     else :
#         return prime(n,)
        


def fib(n):
    a = 0
    b = 1
    sum = 0 
    list = []      #  a,b,a+b,   0,1,1,2,3,5,8
    list.append(a)
    list.append(b)

    print(list)
    for i in range (1,n):

        next_digit = list[-1]+list[-2]
        list.append(next_digit)
        a = list[-2]
        b = list[-1]
        
    print(list)
fib(8)



























