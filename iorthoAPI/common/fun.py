import os


def get_fileBasePath():
    func_path = os.path.dirname(__file__)
    base_dir = os.path.dirname(func_path)
    base_dir = str(base_dir)
    # 对路径的字符串进行替换
    base_dir = base_dir.replace('\\', '/')

    return base_dir

# print(get_fileBasePath())

#链接测试数据库
