x = []
y = 0
with open("input_day_1.txt", "r") as file:
	for line in file:
		x.append(int(line))

for i in range(len(x)-1): 
	if x[i] < x[i  + 1]:
		y += 1
print(y)
#		if int(line) < int(line+1):
#			x += 1
#print(x)
