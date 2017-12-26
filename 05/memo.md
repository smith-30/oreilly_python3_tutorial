## シーケンスデータ型

list, tuple, range

__tuple__

immutable

カンマ区切りの値からなる

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # タプルは入れ子にできる
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
```

空のtupleと1アイテムのタプル
singleton変数の代入はダサいけどこういうものらしい

```python
>>> empty = ()
>>> singleton = 'hello',  
```

アンパッキングも可
```python
>>> t = 12345, 54321, 'hello!'
>>> x, y, z = t 
```

### 集合

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # 重複が除去されている
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # 高速な存在判定
True
>>> 'crabgrass' in basket
False
```

### ディクショナリ(dict)

連想配列的(map)なやつ

ディクショナリは、 キーの唯一性（ひとつのディクショナリの中で重複しないこと）を条件とするので
「キー  : 値」ペアによるソートされない集合

dict() コンストラクタは、 「キー : 値」ペアのタプルからなるシーケンスからディクショナリを構築する。
```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}
# キーワード引数でもいける
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127} 
```

__ループ(key - val)__

```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave 
```

インデックスも込みでループをしたいときはenumtateを使って回す

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe 
```

シーケンスの同時ループもできる

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?It is {1}.'.format(q, a))
...
What is your name?It is lancelot.
What is your quest?It is the holy grail.
What is your favorite color?It is blue. 
```

ソート順にループ

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear 
```

