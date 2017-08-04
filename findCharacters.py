# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
# # output
# new_list = ['hello','world']

word_list = ['hello','world','my','name','is','Anna']
new_list = []
for item in word_list:
    if "o" in item:
        print item
        new_list.append(item)
print new_list
