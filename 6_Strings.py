import re
s1 = 'Hello'
s2 = 'World'

print(s1 + s2)

print(len(s1), len(s2))

print(s1[1:4])
print(s1.index('l'))

para = 'This is a paragraph to check match() method'

print(re.match('This', para))

s = 'Hello'
s_clone = 'Hello'
print(s == s_clone)

print(para.startswith('This'))
print(para.endswith('od'))

s3 = '    This is an untrimmed string    '

print(s3.strip())
print(s3.replace('is', 'was'))

print(s3.split())

print(type(str(5)))

print(s3.upper())
