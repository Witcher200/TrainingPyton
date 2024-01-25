def reed_from_file(filepath):
		with open(filepath, "r") as f_o:
					return f_o.readlines()

print(reed_from_file("web_auto_test\workout1\prodfile.txt"))