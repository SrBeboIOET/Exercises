import os 


name_file = input("Enter the name of file: \n")
print("The name of file is: ", name_file+"\n")

file_path = os.path.abspath(name_file)
print("The path of file is: ", file_path+"\n")

file = open(name_file, "r")
content = file.read()
words = content.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

for word in sorted(frequency):
    print(word, "---", frequency[word])