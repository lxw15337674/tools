# 番号清洗
import os
import re

if __name__ == '__main__':
    path1 = 'G:/b'
    for root, dirs, files in os.walk(path1):
        for f in files:
            oldpath = os.path.join(root,f)
            filename, filetype = os.path.splitext(f)
            d = re.search('[a-zA-Z]{3,4}(-)?(\d)+', filename)
            if d is not None:
                filename = d.group(0) + filetype
                newpath = os.path.join(root, filename)
                print(newpath)
                try:
                    os.rename(oldpath,newpath)
                except:
                    pass
