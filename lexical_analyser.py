#List of Keywords
keywords = ["if", "else", "while", "do", "break",
			"continue", "int", "double", "float", 
			"return", "char", "sizeof", "typedef",
			"switch", "void", "static", "struct", "main"]
			

#List of Operators
operators = ['+', '-', '*', '/',
			 '>', '<', '=']

#List of Seprators
seprators = ['+', '-', '*',
			 '/', ',', ';', '>',
			 '<', '=', '(', ')',
			 '[', ']', '{', '}']

# Function to classify the tokens
def identify(st:str):
	if st.isdecimal():
		return "Integer"
	elif st in keywords:
		return "Keyword"
	elif st in operators:
		return "Operator"
	elif st in seprators and st not in operators:
		return "Seprator"
	else:
		return "User defined Identifier"

#------------------------------------------------------------

count = 0 #token count
line = input(">>>> ")
tokens = line.split(' ')
print("\n")

for t in tokens:
	
	if len(t) != 1:
		temp = ""
		for i in t:
			if i in seprators:
				if len(temp) != 0:
					result = identify(temp)
					print(temp, ": ",result)
					count+=1

				result = identify(i)
				print(i, ": ",result)
				count+=1
				temp=""
			else :
				temp += i
				#print(temp)

		if len(temp) != 0:
			result = identify(temp)
			print(temp, ": ",result)
			count+=1

	else:
		result = identify(t)
		print(t, ": ",result)
		count+=1

print("\nTotal token identified: ",count)



