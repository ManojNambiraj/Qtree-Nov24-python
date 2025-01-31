file = open("text/dummy.txt", 'a')

file.writelines(["\nIt's a Sample word", "\nSecond String"])

# # print(file.read())
# # print(file.readline())
# print(file.readlines())

file.close()