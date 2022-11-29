count=0
sum=0
print('initially',count,sum)
for value in [8,14,27,35,48,98]:
    count=count+1
    sum=sum+value
    print(count,sum,value)
average=sum/count
print('finally',count,sum,average)
