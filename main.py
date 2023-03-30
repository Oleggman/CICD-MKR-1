file = "file.txt"

with open(file, 'r') as file:
    data = file.readline()

data = [line.strip() for line in data]
data = [line.split(", ") for line in data]

