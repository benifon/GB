#1
with open('nginx_logs.txt', 'r') as f:
    result = []
    for line in f:
        final = line.split()
        result.append((final[0], final[5], final[6]))
print(result)



#3

from itertools import zip_longest
import json

new_dict = {}
with open('имена.csv', encoding='utf-8') as namefile:
    with open('хобби.csv', encoding='utf-8') as hobbyfile:

        num_namefile = sum(1 for line in namefile)
        num_hobbyfile = sum(1 for line in hobbyfile)

        if num_namefile < num_hobbyfile:
            exit(1)

        namefile.seek(0)
        hobbyfile.seek(0)
        for line_namefile, line_hobbyfile in zip_longest(namefile, hobbyfile):
            print((line_namefile, line_hobbyfile))
            new_dict[line_namefile.strip()] = line_hobbyfile.strip() if line_hobbyfile is not None else line_hobbyfile

with open('task3.json', 'w', encoding='utf-8') as f:
    json.dump(new_dict, f, ensure_ascii=False)
print(new_dict)

#6

import sys

price = sys.argv[1]

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(price + '\n')

import sys

nums = sys.argv[1:]
print(nums)
with open('bakery.csv', encoding='utf-8') as f:
    if len(nums) > 1:
        start_idx = int(nums[0])
        end_idx = int(nums[1])
    elif len(nums) == 0:
        start_idx = 0
        end_idx = sum(1 for line in f)
        f.seek(0)
    else:
        start_idx = int(nums[0])
        end_idx = sum(1 for line in f)
        f.seek(0)

    for idx, line in enumerate(f):
        if start_idx <= idx + 1 <= end_idx:
            print(line.strip())



