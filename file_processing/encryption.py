
import os
import re

def enco(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            oldPath = os.path.join(root, f)
            filename, fileType = os.path.splitext(f)
            d = re.search('{0}$'.format(formatName), fileType)
            if d is None:
                file = open(oldPath,'a')
                file.write(fileType)
                file.close()
                newFileType = fileType + formatName
                filename = filename + newFileType
                newPath = os.path.join(root, filename)
                print(newPath)
                try:
                    os.rename(oldPath, newPath)

                except:
                    pass
        for dir in dirs:
            enco(os.path.join(root,dir))
def dec(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            oldPath = os.path.join(root, f)
            filename, fileType = os.path.splitext(f)
            d = re.search('{0}$'.format(formatName), fileType)
            if d is not None:
                file = open(oldPath, 'a')
                file.write('')
                file.close()
                newFileType = fileType[:-len(formatName)]
                filename = filename + newFileType
                newPath = os.path.join(root, filename)
                print(newPath)
                try:
                    os.rename(oldPath, newPath)
                except:
                    pass
        for dir in dirs:
            dec(os.path.join(root, dir))
if __name__ == '__main__':
    path = 'D:/b'
    formatName = 'rar'
    # 加密
    enco(path)
    # 解密
    # dec(path)
