file = "file.txt"

with open(file, 'r') as file:
    data = file.readline()

data = [line.strip() for line in data]
data = [line.split(", ") for line in data]


def sort_by_area():
    print("Sort by area: ")
    sorted_by_area = get_sort(1)
    for country in sorted_by_area:
        print(", ".join(country))


def get_sort(el):
    return sorted(data, key=lambda x: int(x[el]))
