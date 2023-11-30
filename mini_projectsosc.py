import random as rd
letters="ABCDEFGHIJKLMOPQRSTUVWXYZ"
digits="123456789"
sym="!@#$%^&*"
print("how many alphabets do you want:")
l=int(input())
print("how many digits do you want:")
d=int(input())
print("how many symbols do you want:")
s=int(input())
pwd=""
for i in range(l):
    pwd+=rd.choice(letters)
for i in range(d):
    pwd+=rd.choice(digits)
for i in range(s):
    pwd+=rd.choice(sym)
pwd="".join(rd.sample(pwd,len(pwd)))
print("your password is\n"+pwd)

      