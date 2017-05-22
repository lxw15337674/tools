#保存文件夹结构
import os
import re

if __name__ == '__main__':
    path = open("C:/Users/40417/Desktop/text.txt",'w')
    result = ""
    path1 = 'G:/b'
    for root, dirs, files in os.walk(path1):
        for f in files:
            a = root+'/'+f+'\n'
            result +=a
    path.write(result)
    path.close()

