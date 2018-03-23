
#Q1_A

x = "junyiacademy"

def restr(str):
	return str[::-1]
	
print(restr(x))


#Q1_B

x = "flipped class room is important"

def restr2(str):
	str_arr = x.split(' ')
	str_out = ""
	
	for i in str_arr :
		i = i[::-1]
		
		str_out += i + ' '
	
	return str_out
	
print(restr2(x))



#Q2

input = int(input("intput : "))
output = 0

for i in range(input):
	if (i+1)%3 == 0 and (i+1)%5 == 0 :
		output += 1
	elif (i+1)%3 == 0 or (i+1)%5 == 0 :
		continue
	else :
		output += 1
	
print("output : " + str(output))


#Q3

#Q4
