name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

time_distribution = dict()
for line in handle:
    word_list = line.rstrip().split(" ")

    if word_list[0] == "From":
        time = word_list[6].split(":")
        hour = time[0]

        time_distribution[hour] = time_distribution.get(hour, 0) + 1

for k, v in sorted(time_distribution.items()):
    print(k, v)
