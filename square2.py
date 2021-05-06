size = int(input("How big is the square? "))

for i in range(size):
    row = ""
    for i in range(size):
        row = row + "*"
    print(row)