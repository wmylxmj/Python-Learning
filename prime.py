#求一个数的所有质因子
import math 
number=int(input("please input a int number which little than 100000: "))
prime_number=[2]
prime_factor=[]
#预处理
if (number%10)%2==0:
    number=int(number/2)
    prime_factor.append(2)
if (number%10)%5==0:
    number=int(number/5)
    prime_factor.append(5)
if number%3==0:
    number=int(number/3)
    prime_factor.append(3)
#求范围内质数
for i in range(3,number+1):
    judge=1
    if(i%2==0):
        judge=0
    else:    
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                judge=0   
        if judge==1:
            prime_number.append(i)
'''print(prime_number)'''
#求质因子
while number!=1:
    for k in range(0,len(prime_number)):
        if number%prime_number[k]==0:
            prime_factor.append(prime_number[k])
            number=number/prime_number[k]
prime_factor.sort()
print(prime_factor)

