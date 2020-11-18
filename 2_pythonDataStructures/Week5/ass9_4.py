name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

word_counter = dict()
for line in handle:
    word_list = line.rstrip().split(" ")

    if word_list[0] == "From":
        word_counter[word_list[1]] = word_counter.get(word_list[1], 0) + 1

big_count = None
big_email = None

for k, v in word_counter.items():
    if big_count is None or v > big_count:
        big_count = v
        big_email = k

print(big_email, big_count)
