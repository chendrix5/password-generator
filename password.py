import random

print('your password: ')

chars = 'abcdefghijklmnopqrstuvwxyx1234567890'

password = ''
for x in range(16):
    password += random.choice(chars)

print(password)