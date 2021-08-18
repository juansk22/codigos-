str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' *4)

ch1 = '@'
ch2 = ' ' # espacio
ch3 = "["

print(ord(ch1))
print(ord(ch2))
print(ord(ch3))

print(chr(64))
print(chr(222))

alpha = 'abcdefg'
print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[::2])

alpfabeto = 'abcdefghijklmnñopqrstuvwxy'

print('f' in alpfabeto)
print('F' in alpfabeto)
print('l' in alpfabeto)
print('ghi' in alpfabeto)
print('Xyz' in alpfabeto)

alfabeto = alpfabeto + 'z'
print(alpfabeto)

print(min('aAbByYzZ'))

t = [0,1,2]
print(min(t))

print(max('aAbByYzZ'))

print("www.netacad.com".replace("netacad.com","pytohninstitute.org"))
print("this is it!".replace("is","are"))
print("apple juice".replace("juice",""))

print("yo se que nada se".swapcase())

print()
print("yo se que nada se. parte 2".upper())

secondGreek = ['omega','alfa','pi','gama']
print(secondGreek)

secondGreek.sort()
print(secondGreek)

print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

print("Moooo".isalpha())
print("Mu40".isalpha())

print('2018'.isdigit())
prin("Año2019".isdigit())