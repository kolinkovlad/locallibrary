# class FileOwners:
#
#     @staticmethod
#     def group_by_owners(files):
#         owners = [item[1] for item in files]
#         owners = set(owners)
#         rez ={}
#         for ovner in owners:
#             file_list=[item[0] for item in files  if item[1] == ovner]
#             print(file_list)
#             # rez[]
#         return None
#
# files = {
#     'Input.txt': 'Randy',
#     'Code.py': 'Stan',
#     'Output.txt': 'Randy'
# }
# print(FileOwners.group_by_owners(files))
#
#
# shift = 2
# {'a':'c', 'b':'d'}
#
# for i in list_sdf:
#     pass
#
# sdfsdf= 12

import string

# print(string.ascii_lowercase)

# print(string.punctuation)
# letter_list = string.ascii_lowercase
# print(len(letter_list))
# for index in range(len(letter_list)):
#     print(letter_list[index], " : ",  letter_list[(index + 5) % 26])

shift_dict={}

shift_dict['a'] = 'c'