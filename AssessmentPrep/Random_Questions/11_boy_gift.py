file = open("11_sample.txt", 'r')

formatted_list = []
for line in file:
    temp_s = line.replace(" - ", "-")
    temp_s = temp_s.replace('\n', "")
    formatted_list.append(temp_s.split("-"))

formatted_list.sort(key=lambda x: x[1], reverse=True)
print(formatted_list)

n = int(input())
i = 0
while n > 0:
    print(f"{formatted_list[n-1][0]}-{formatted_list[n-1][1]}")
    n -= 1


