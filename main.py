file = "file.txt"

with open(file, 'r') as file:
    data = file.readline()

data = [line.strip() for line in data]
data = [line.split(", ") for line in data]

def get_sort(id):
    return sorted(data, key=lambda x: int(x[id]))
