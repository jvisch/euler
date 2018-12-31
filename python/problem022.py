from urllib.request import urlopen

# with open(r'C:\Users\owwwt\Dropbox\projectEuler\python\p022_names.txt') as f:
#    names = f.read().replace('"', '').split(',')

with urlopen('https://projecteuler.net/project/resources/p022_names.txt') as story:
    names = []
    for line in story:
        names.extend(line.decode('utf-8').replace('"', '').split(','))

# names = names[1:10]

names.sort()

nameValues = [sum([ord(c) - ord('A') + 1 for c in n]) for n in names]
total = sum([(idx + 1) * value for idx, value in enumerate(nameValues)])

print(total)
