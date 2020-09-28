

# import os
#
# def list_dir(file_path):
#
#     file_list = []
#     if os.path.isfile(file_path):
#         file_list.append(file_path)
#         return file_list
#     dir_list = os.listdir(file_path)
#     for cur_file in dir_list:
#         # 获取文件的绝对路径
#         path = os.path.join(file_path, cur_file)
#         if os.path.isfile(path):  # 判断是否是文件还是目录需要用绝对路径
#             file_list.append(path)
#         if os.path.isdir(path):
#             list_dir(path, file_list)  # 递归子目录
#     return file_list

import re
print(re.match('www', 'www.runoob.com').span())

print(re.match('com', 'www.runoob.com'))