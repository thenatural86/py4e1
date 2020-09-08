name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

tmp = {}

for line in handle:
    if not line.startswith('From '):
        continue
    line = line.rstrip().split()
    day = line[4]
    time = line[5]
    hr = time.split(":")[0]
    # print("LINE", line)
    # # print("DAY", day)
    # print("TIME", time)
    # print("HR", hr)
    tmp[hr] = tmp.get(hr, 0) + 1
# print(tmp)

lst = []
for k, v in tmp.items():
    # print(k, v)
    tup = (k, v)
    lst.append(tup)
lst = sorted(lst)
# print(lst)
for k, v in lst:
    print(k, v)
