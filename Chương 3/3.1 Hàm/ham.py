#vi du de nham:
def square(x):
    y = x*x
print(square(5))

def square(x):
    print(x*x) 
print(square(5))

def square(x):
    return x*x
print(square(5))

# viet ham tinh giai thua cua n:
#cach 1: De quy
def gt(n):
    if n == 0:
        return 1
    else:
        return n * gt(n-1)
print(gt(5))

#cach 2: dung vong lap
def gt(n):
    kq = 1
    for i in range(1,n+1):
        kq *= i
    return kq
n = int(input("nhap n: "))
print("%d! = %d" %(n, gt(n)))

#3.1.4. tham so truyen vao:
def sum (a, b =10):
    return a + b
print(sum(5))
print(sum(5, 20))
#tham so thay Doi:
def sum (*args):
    kq = 0
    for i in args:
        kq += i
    return kq
print(sum(1,2,3))
print(sum(1,2,3,4,5))

def sum (a,b,*p):
    s=a+b
    for i in p:
        s+=i
    return s
print(sum(1,2))
print(sum(1,2,3))
print(sum(1,2,3,4,5,6))
#3.1.6 Ham vo danh:
nhan_doi = lambda x: x*x
print(nhan_doi(10))

def nhan_doi(x):
    return x*x
print(nhan_doi(10))
#dung lamda voi filter:
lst1 = [1,2,3,4,5,6,7,8,9,10]
lst2 = list(filter(lambda x: x%2==0, lst1))
print(lst2)
#dung lamda voi map:
lst3 = list(map(lambda x: x*x, lst1))
print(lst3)
