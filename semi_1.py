#皆さんが教えてくれた補足事項をここにまとめておきます
#これ言ったはずなのに記録されてない・・・（泣）と思った方はこのソースコードを再編集してpushするか直接コメントしてください
#Pythonでは、コメントアウトは#で行ってください

#文字列
#言うのを忘れていましたが、Pythonでは文字列の表記は'hoge'でも"hoge"でも構いません。
print("Hello")
print('Hello')

#演算
#これも言うのを忘れてたんですが、bool型の1,0への型変換は演算の時にも使えます
print(2+True)
print(True*3)
#整数から浮動小数点数への型変換（下の式の出力は浮動小数点数であることに注意）
print(1+1.0)

#変数
#予約語（すでに何らかの意味を持っているワード。andとかifとかprintとか）は変数名に使えないので注意。
and = 'hoge'
print(add)

#print関数
#printのキーワード引数'end'は、出力値の末尾をどうするかを示します。
#デフォルトは'\n'
print('Hello',end = '!')
print('World')
#printのキーワード引数'sep'は、文字を何で区切るかを示しています。（デフォルトは' '）
print('Hello','world',sep = '')

#ブール型と比較演算子
#型変換
print(1 == True)
print(0 == False)
print(1.0 == True)

#'==' とisの違い
#'=='と似たような働きをするものにisがあります
x = [1,1,1]
y = [1,1,1]
if (x == y) and (x is y):
    print('Same')
elif (x == y) and not (x is y):
    print('Equal')
else:
    print('Different')    
#ざっくりとですが、
# 値が同じ（等価である）→　'=='
# オブジェクトそのものが同じ → is
#のようです

#ブール演算子
#orとnotに注意。
#if (bool値を返さないが、何らかの値を返す式):
    #〜処理〜
#といった場合、帰ってきた値が0でないなら処理が行われるようです
if 'hoge':
  print('OK')

#range(a,b,c)（a.b.cは整数）：aからb-1までc間隔で値を返す

#関数の定義
#関数に戻り値が定義されてないのに参照した場合は'None'が返ってきます
def hello(greet):
    # 引数greetの値を返す
    pass
    
echo = hello("Hello")
print(echo)
#ローカル変数とグローバル変数
#ローカル変数：プログラムの一部（ここでは関数内）でのみ利用可能な変数。関数の外からは参照することはできません。
#グローバル変数：関数外で定義されてる変数。
#グローバル変数を関数内で操作するにはglobal xを使う
x = 1
def hello2(greet):
    # 引数greetの値を出力
    global x
    x = 2
    print(greet)
    
hello2("Hello")
print(x)




