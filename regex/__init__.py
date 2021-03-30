import re

s = r'ABC\-001'

if re.match(r'^\d{3}\-\d{3,8}$','010-12345') :
    print('ok')
else:
    print('failed')

print(re.split(r'\s+','a b  c'))
print(re.split(r'[\s\,]+','a, b,  c'))
print(re.split(r'[\s\,\;]+','a,b;;c  d'))

m = re.match(r'(\d{3})-(\d{3,8})$','010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

m=re.match(r'^(\d+?)(0*)$', '102300')
print(m.group(0))
print(m.group(1))
print(m.group(2))

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
m=re_telephone.match('010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))
