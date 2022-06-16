a = '12345контактов'

number = []
for i in a:
    if i.isdigit():
        number.append((int(i)))

b = " ".join(map(str,number))
for i in b:
    b = b.replace(' ', '')

print(b)

# sentence = 'Extract 100 , 100.45 and 10000 from this string'
# s = [int(s) for s in str.split(sentence) if s.isdigit()]
# print(s)

