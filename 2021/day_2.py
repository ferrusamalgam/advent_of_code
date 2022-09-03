
with open("input_day_2.txt", "r") as file: 
	inp = [line.split() for line in file]

height = 0
forward = 0

for i in inp:
	if i[0] == 'forward':
		forward += int(i[1])
	if i[0] == 'up':
		height -= int(i[1])
	if i[0] == 'down':
		height += int(i[1])

print(height * forward)
