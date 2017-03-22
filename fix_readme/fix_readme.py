import os
import re

path1 = "C:/Users/40417/Desktop/Language _learning"
path2 = "C:/Users/40417/Desktop/python"
path_list = [path1, path2]
readme_list = []


# 遍历出所有readme文件,并输入为list
def traversal(path):
    # root为目录名, dirs为目录中的文件夹名, files为目录中的文件名.保存为list
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.lower().endswith('.md'):
                path = os.path.join(root, f)
                readme_list.append(path)


def statistics():
    for path in readme_list:
        d = ''

        def lol():
            d = ''
            for line in f.read().split('\n'):
                num = ''  # 记录#个数
                for a in line[0:6]:
                    if a == '#':
                        num += "#"
                if len(num) != 0:
                    line = line.replace(num, num + ' ')
                    line = line.replace(num + '  ', num + ' ')
                line += "\n"
                d += line
            return d

        # 暂时只能通过try语句处理两种不同的编码文件
        try:
            try:
                with open(path, 'r', encoding="utf-8") as f:
                    d = lol()
            except:
                with open(path, 'r', encoding="gb2312") as f:
                    d = lol()
            with open(path, 'w') as f:
                f.write(d)
            print(path + "已经修复!")
        except:
            print(path+"无法修复!")


if __name__ == '__main__':
    for path in path_list:
        traversal(path)
    statistics()
