list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
a = int(input("Enter the length of pattern required: "))
n = 0
for i in range(a + 1):
    for j in range(i):
        print(list[n%len(list)], end="")
        n += 1
    print()