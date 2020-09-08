# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
num = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # line = line.find("0")
    line = float(line[20:])
    count += line
    num += 1
    # print(line)
    # print(count)
    # print(num)
avg = count/num
print("Average spam confidence:", avg)
