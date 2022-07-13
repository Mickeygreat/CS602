''' format strings (f-strings)'''
''' this is from chapter 2 '''
dozen = 12
items = "cookies"
result = f'I ate {dozen} donuts'
print (result)
print (f'I ate {dozen} donuts.')

result2 = f'I ate {dozen} {items}'
print (result2)
print(f'I ate {dozen} {items}')


print(f'I ate {dozen * 2}  chocolate chip {items:10s}.')
print(f'{dozen} donuts cost ${dozen:<8.2f}!!')
print(f'{dozen} donuts cost ${dozen:>8.2f}!!')
print(f'{dozen} donuts cost ${dozen:>4.2f}!!')
print(f'{dozen} donuts cost ${dozen:>.2f}!!')
''' using str.format()'''
print("I ate {} donuts".format(dozen))
