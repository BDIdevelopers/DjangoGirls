print('Hello, Django girls!')

if 5 > 2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')

volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")


def hi():
		print('Hi there!')
		print('How are you?')

hi()

def hi(name):
	if name == 'Ola':
		print('Hi Ola')
	elif name == 'Sonja':
		print('Hi Sonja')
	else:
		print('Hi in general')

hi('Ola')

def hi(name):
	print('Hi '+ name)
hi('Rachel')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
print(girls)
for name in girls:
	print(name)

s = ', '
print(s.join(girls))


output = ""
for item in girls:
	output = output + item
print(output)

for name in girls:
	hi(name)

for i in range(1, 6):
	print(i)



