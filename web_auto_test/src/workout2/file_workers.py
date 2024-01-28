# file = open('web_auto_test\src\workout2\prodfile.txt', 'r')
# line = file.readline
# file.close

# print(line)

def read_from_file(filepath):
		with open('web_auto_test\src\workout2\prodfile.txt', 'r') as f_o:
			return f_o.readLines()

print(read_from_file('web_auto_test\src\workout2\prodfile.txt'))