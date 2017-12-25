## 制御文

### if

```python
if <条件> : 
    <処理>
elif # else if ではない
```

### for

```python
>>> # 文字列の長さを測る：
... words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12 
````

反復中のシーケンスを改変する必要があるときは（たとえば選択したアイテムを複製するなど、
コピーを取って反復をかけることが推奨される。
シーケンスに反復をかけることで暗黙にコピーが取られたりはしない。
これにはスライス表記を使うのがよい：

```python
>>> for w in words[:]:  # リスト全体のスライスコピーにループをかける
...     if len(w) > 6:
...         words.insert(0, w)
...
>>> words
['defenestrate', 'cat', 'window', 'defenestrate'] 
```

### range

```python
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
```

range(5, 10)
→ 5 から 9 まで

こんな使い方も

```python
>>> list(range(3, 6))            # 個別の引数を使った普通のコール
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))           # リストからアンパックした引数でコール
[3, 4, 5] 
```

### break, continue, else

```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # ループで約数を見つけられなかった場合
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3 
```

上記の `else` は `break` 節を受けるためにあって
ifの分岐ではない

continueの使い方は他プログラミング言語と同じ

### pass

何もさせない時に使われる

pass 文は何もしない。構文的に文が必要なのに、プログラム的には何もする必要がないときに使う。
例：

```python
>>> while True:
...     pass # ビジーウェイトでキーボード割込(Ctrl+C)を待つ
... 
```

これは最小のクラスを生成するのにもよく使われる：

```python
>>> class MyEmptyClass:
...     pass
... 
```

### 関数

`def <関数名>(引数):`

関数は値として渡すことが可能

```python
>>> def fib(n):     # フィボナッチ級数をnまで書き出す
...     """nまでのフィボナッチ級数を表示する"""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> fib
<function fib at 10042ed0>
>>> f = fib
>>> f(100)
0 1 1 2 3 5 8 13 21 34 55 89 
```

"""nまでのフィボナッチ級数を表示する""" は関数についてのdoc
関数宣言の次の行に書くことができる


```python
>>> def fib2(n): # n までのフィボナッチ級数を書き出す
...     """n までのフィボナッチ級数からなるリストを返す """
...     result = []
...     a, b = 0, 1 
...     while a < n:
...         result.append(a)    # 下記参照
...         a, b = b, a+b
...     return result
...
>>> f100 = fib2(100)    # コールする
>>> f100                # 結果を書き出す
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
```

関数はキーワード引数も取れる。 「キーワード  = 値」の形である。次のような関数があるとする：

仮引数の最後が **名前の形になっていると、 この引数はディクショナを受け取る。
このディクショナリには、仮引数に対応するキーワードを除いたすべてのキーワード引数が入っている
（つまりこの形にすれば、仮引数にないキーワードが使える）。
またこれは、*名前の形式（次項で詳説）と組み合せて使うことができる（*名前は **名前の前にあること）。
こちらの形式では仮引数にない位置指定型引数をすべて含んだタプルが関数に渡る。
だからたとえば次のような関数を定義すると

```python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
    "It's really very, VERY runny, sir.",
    shopkeeper="Michael Palin",
    client="John Cleese",
    sketch="Cheese Shop Sketch") 
```

*argumentsには、`key=value`形式でない値が入ってくる
**keywordsには、`key=value`形式の値が入る

*argumentsは必ず**keywordsの前にないといけない。

### lambda

lambdaは単一の式しか持てない

```python
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43 
```

### 関数アノテーション

php7っぽく書ける

```python
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 
'str'>}
Arguments: spam eggs
'spam and eggs' 
```