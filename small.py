small='none'
print('before',small)
for value in [9,41,12,3,74,38]:
    if small is 'none':
        small=value
    elif value<small:
        small=value
    print(small,value)
print('after',small)
