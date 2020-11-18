import re
line = "this is a line of text. 1337"

result = re.search('[0-9]+', line)

result2 = re.findall('[a-z0-9]+', line)
print(result[0])

