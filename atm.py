n=input('please enter the new reading:')
new=float(n)
o=input('please enter the old reading')
old=float(o)
u=new-old
if u>500:
    rate=12

elif u>300:
    rate=10

elif u>100:
    rate=8

else :
    rate=5

bill=rate*u
print('your consumed units:',u)
print('rate:',rate)
print('your power bill is:',bill)
