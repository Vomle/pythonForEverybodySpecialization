import re
fh = open("regex_sum_1050110.txt")

counter = 0
for line in fh:
    numbers = re.findall('[0-9]+', line)
    numbers_int = [int(i) for i in numbers]
    line_sum = sum(numbers_int)
    counter = counter + line_sum

print(counter)

