## クラス

- ビルトイン名の入った名前空間はpythonインタープリタの起動とともに作られ
終了まで削除されない

- モジュールのグローバル名前空間はモジュール定義の読み込み時に作られる

### スコープ

pythonは、global文の影響下にない限り、代入を常に最内のスコープに行う
代入はデータをコピーしない

global 文を使うと、その変数がグローバルスコープにあること
再結合もそちらに行うべきであることを示すことができる。

nonlocal 文は、その変数が自分を取り
囲むスコープにあり、再結合もそちらに行うべきであることを示す。

```python
def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

__Output__

```python
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam  # nonlocal使わないと再結合されない。外を見に行かない
In global scope: global spam
```

### クラスオブジェクト

```python
class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

    def __init__(self):
        self.data = []
```

constructは\__init__で宣言する

### インスタンスオブジェクト

属性参照のみ
データ属性とメソッドの2種類

```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

### 共有データとインスタンス変数の使い分けに注意

```python
class Dog:
    tricks = []  # クラス変数の使い方を間違えてる

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('ころがる')
>>> e.add_trick('死んだふり')
>>> d.tricks              # すべての犬が共有してるなんて...
['ころがる', '死んだふり']
```

↑ は意図した挙動をしないのでインスタンス変数使う

```python
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []      # それぞれの犬に新たに空リストを生成
    def add_trick(self, trick):
        self.tricks.append(trick)
```

### 継承

```python
class DerivedClassName(BaseClassName):
    <文1>
    .
    .
    .
    <文N>
```

継承周りのtips

• インスタンスの型をチェックするには isinstance() を使う。
たとえば isinstance(obj, int) では、obj.__class__ が int またはその派生クラス
である場合にのみ True が返る。

• クラス継承のチェックに issubclass() を使おう。issubclass(bool, int) は True が返るが 、
これはbool が int のサブクラスであるからだ 。
issubclass(float, int) は、float が int のサブクラスでないため False となる。

### 多重継承

```python
class DerivedClassName(Base1, Base2, Base3):
    < 文 1>
    .
    .
    .
    < 文 N>
```

pythonには __プライベートインスタンス変数__ がない

マングリングとよばれるサポート機能
継承による名前衝突、不意なオーバーライドを防ぐ
保護したいメンバメソッドを\__hogeで宣言する


### iterator

for 文などは渡されたオブジェクトに対して`iter()`を呼ぶようになっている

__ex__

```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<iterator object at 0x00A1DB50>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
    File "<stdin>", line 1, in ?
    next(it)
StopIteration
```

なのでクラスをforで回せるようにするには
\__iter__() と
\__next__() を実装してやればいい


### yield

yieldメソッドが何故forで受けられるかというと
自動的に\__iter__() と \__next__() が生成されるから

ローカル変数と実行状態が保存される
