hd = []
hd_s = []

while True:
	name = input('請輸入雙通道數字，或輸入q結束: ')
	if name == 'q':
		break
	hd.append(name)
while True:
	name_h = input('請輸入單通道數字，或輸入q結束: ')
	if name_h == 'q':
		break
	hd_s.append(name_h)
print(hd)
print(hd_s)


char = []
char1 = []

with open('human design.txt', 'r', encoding='utf-8') as file:
	for line in file:
		for num in hd:
			if num == line:
				char.append(line)
with open('human design.txt', 'r', encoding='utf-8') as file:
	for line in file:
		for num in hd_s:
			if num == line:
				char1.append(line)
print('-------------------')
print(char)
print('-------------------')
print(char1)
print('-------------------')