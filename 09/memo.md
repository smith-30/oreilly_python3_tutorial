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

### クラス
