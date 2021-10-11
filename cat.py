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
'''
使用言語：Python
コマンドプロンプトで動作することを確認しました。
Cドライブ直下のファイルに入れてもらってパス　目的のファイルの順に
入力してください。パス間は/で入力してください。
文字コードがUTF-8だったら表示出来ます。

'''
