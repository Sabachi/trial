import re
handle = open("regex_sum_1386934.txt")

num = list()



for line in handle:
    z = list()
    y = list()
    if re.search('[0-9]+',line):
        y = re.findall( '[0-9]+',line)
        print(y)
        for i in y:
            x = int(i)
            print("x",x)
            z.append(x)
            print("z",z)
        num.append(sum(z))
        print("num",num)
    else:continue

total = sum(num)

print(total)
