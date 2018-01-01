## 例外処理

```python
>>> while True:
...     try:
...         x = int(input(" 数字を入れてください : "))
...         break
...     except ValueError:
...         print(" あらら ! これは有効な数字ではありません。どうぞもう一度 ...")
...
```

• 最初に try 節（キーワード try と except に挟まれた文）が実行される。

• 例外が送出されなければexcept節はスキップされ、 try文の実行が終了する。

• try 節の実行中に例外が発生すると、try 節中の残りはスキップされる。
発生した例外の型が except キーワードの後ろで指定してある例外と一致すれば、
except 節が実行される。そして try 文のあとのプログラムの実行がそのまま続けられる。

• 例外の型が except 節にある名前と一致しない場合、
送出された例外はさらに外側にある try 文に渡される（try 文が入れ子になっている場合） 。
ハンドラが見つからないと、これは未処理例外（unhandled exception）となり、
上の方の例で示したようなメッセージを表示して実行が終了する。


__else節で捕捉もできる__

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

### 例外はraiseで起こすことが可能

```python
>>> raise NameError('HiThere')
    Traceback (most recent call last):
    File "<stdin>", line 1, in ?
    NameError: HiThere
```

### ユーザー定義例外

```python
>>> class MyError(Exception):
...     def __init__(self, value):
...         self.value = value
...     def __str__(self):
...         return repr(self.value)
...
>>> try:
...     raise MyError(2*2)
... except MyError as e:

...     print('My exception occurred, value:', e.value)
...
My exception occurred, value: 4
>>> raise MyError('oops!')
Traceback (most recent call last):
File "<stdin>", line 1, in ?
__main__.MyError: 'oops!'
```

`Exception` を受けるクラスを作成する。


### finallyで必ず実行する節を作る

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
Traceback (most recent call last):
File "<stdin>", line 2, in ?
KeyboardInterrupt
```

オブジェクトによってはクリーンナップ動作が保証されている
下記の例では、with文を使うことで必ずファイルがクローズされることが保証される

```python
for line in open("myfile.txt"):
    print(line, end="")
```

↓

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```
