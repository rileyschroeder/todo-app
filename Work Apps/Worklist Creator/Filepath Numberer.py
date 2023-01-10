length = int(input("Enter number of samples in set: "))
path = input("Enter the filepath of the data files: ")

x = 1
paths = []

while x <= length:
    sample_path = path + f'{x:03d}' + '.d\n'
    paths.append(sample_path)
    x = x + 1

with open("Names2.txt", "w") as file:
    file.writelines(paths)
