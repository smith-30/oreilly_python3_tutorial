__数字周り__

```python
>>> 17 / 3  # 標準の除算はfloatを返す
5.666666666666667
>>>
>>> 17 // 3  # 切り下げ除算は小数点以下を捨てる
5
>>> 17 % 3  # %演算子は剰余（除算の余り）を返す
2
>>> 5 ** 2  # 5の自乗
25
```

__文字列周り__

引用符にはシングルクォートも （'...'） ダブルクォートも （"..."） 使えて、 
どちらも同じ結果になる 。
バックスラッシュ（\）でクォート文字のエスケープができる

「\」を前置した文字が特殊文字に解釈されるのが嫌なときは、raw 文字列を使えばよい。
これは最初の引用符の前に r を置く：

```python
>>> print('C:\some\name')  # \n は改行なので
C:\some
ame
>>> print(r'C:\some\name')  # 引用符の前の r に注目
C:\some\name 
```

文字列リテラルを複数行にわたり書くこともできる。ひとつの方法はトリプル 
クォート（"""...""" または '''...'''）を使うというものだ。行末文字は自動的に 
文字列に含有される。これを避けたいときは行末に \ を置く。以下のようにすると：

```python
print("""\
Usage: thingy [OPTIONS]
-h                        Display this usage message
-H hostname               Hostname to connect to
""") 
```

以下のような出力が得られる（最初の改行が含まれていないことに注目）:

```python
Usage: thingy [OPTIONS]
-h                        Display this usage message
-H hostname               Hostname to connect to 
```

文字列は + 演算子で連結できるし、* 演算子で繰り返すこともできる：

```python
>>> # un を 3 回繰り返して最後に ium を付ける
>>> 3 * 'un' + 'ium'
'unununium' 
```

列挙された文字列リテラル（引用符で囲まれたものたち）は自動的に連結される。

```python
>>> 'Py' 'thon'
'Python'
```


変数とリテラルの連結、そして変数同士の連結には + を使う：

```python
>>> prefix + 'thon'
'Python' 
```

文字列にはインデックスを使える

```python
>>> word = 'Python'
>>> word[0]  # 位置0のキャラクタ
'P'

>>> word[-1]     # 最後のキャラクタ
'n'
```

スライスもできる。goと同じように

```python
>>> word[:2]  # 最初の文字から位置 2（2 を含まない）までの文字
'Py'
```

Python の文字列は改変できない̶̶変更不能体（immutable）であるという。
このため、文字列のインデックス位置に代入を行うとエラーが出る：

len()は文字列の長さを返す

```python
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34 
```