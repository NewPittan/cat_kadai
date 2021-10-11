import os
import sys
args = sys.argv
os.chdir('..')  # 相対パス
os.chdir(args[1])  # 絶対パス
f = open(args[2], 'r', encoding='UTF-8')

data = f.read()
print(data)

f.close()
print('処理終了')
