name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
# init empty {}
counts = {}
# iterate through file
for line in handle:
    # uf file does not start with "From", skip
    if not line.startswith('From '):
        continue
    # split line into array and take data from index 1 and save in word variable
    word = line.split()[1]
    # if word is not in count dict set value of word to 0, otherwise + 1 current value
    counts[word] = counts.get(word, 0) + 1
print(counts)
# set variables to None value
bigcount = None
bigword = None
# iterate through items in counts dict with key AND value iterator variables
for word, count in counts.items():
    # if the bigcount is still none OR current count iterator is greater than None
    if bigcount is None or count > bigcount:
        # update variables to be current iterator variables
        bigword = word
        bigcount = count
print(bigword, bigcount)

# #############################################

# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)
# # init empty {}
# counts = {}
# # iterate through file
# for line in handle:
#     # uf file does not start with "From", skip
#     if not line.startswith('From '):
#         continue
#     print(line)
#     # split line into array and take data from index 1 and save in word variable
#     # words = line.split()
#     # words = words[1]
#     # print(words)
#     # counts[words] = counts.get(words, 0) + 1
# print(counts)

# bigcount = None
# bigword = None
# for word, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
# print(bigword, bigcount/2)
