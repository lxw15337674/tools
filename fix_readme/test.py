import chardet
path = "C:/Users/40417\Desktop\Language _learning/test.md"

with open(path, 'r',encoding='gb2312') as f:
    fencoding=chardet.detect(f.read())
    print (fencoding)