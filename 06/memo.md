## モジュール

import 文には別の構文もある。これはモジュール内で定義されている名前を 
import する側のシンボル表に直接取り込む

```python
>>> from fibo import fib, fib2
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377 

# 全て取り込むにはこう
>>> from fibo import *
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377 
```

## モジュールの読み込み順

1. ビルトインモジュール
1. 入力スクリプトのあるディレクトリ
1. PYTHONPATH
1. インストールごとのデフォルト


シンボリックリンクを置いてあるディレクトリはモジュール検索パスに入らない

## コンパイルについて

pythonはコンパイル済みのモジュールを\__pycache__ディレクトリに
module.バージョン名.pycの名前でキャッシュする

ソースファイルの最終変更日時をコンパイル済みのバージョンと比較し
再コンパイルが必要か判断する
__コンパイル済みのモジュールはプラットフォーム非依存__

以下の2つの状況ではキャッシュをチェックしない
- 常に再コンパイルが行われ結果を保存しない状況(モジュールがコマンドラインから直接ロードされるとき)
- キャッシュのチェックが行われない状況(モジュールのソースファイルがないとき)

コンパイルの補足

- mpileallモジュールを使うと、ディレクトリのモジュールすべての.pycファイルが生成できる。 
- の処理の詳細についてはPEP 3147を参照のこと。判断のフローチャートも掲載されている。 

## パッケージ

__モジュールの集まり__

`ex`

```
sound/                          トップレベルパッケージ
    __init__.py              soundパッケージの初期化
    formats/                  ファイル形式間変換用のサブパッケージ
        __init__.py
        wavread.py
        wavwrite.py
        aiffread.py
        aiffwrite.py
        auread.py
        auwrite.py
        ...
    effects/                  エフェクタ用のサブパッケージ
        __init__.py
        echo.py
        surround.py
        reverse.py
        ...
    filters/                  フィルタ用のサブパッケージ
        __init__.py
        equalizer.py
        vocoder.py
        karaoke.py
```

あるディレクトリをパッケージを含むものとして扱わせるには
\_\__init\_\__.pyファイルが必要。

`import sound.effects.echo ` でモジュールを引っ張れる
ただ、これによる参照はフルネームで行わねばならない


```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

__サブモジュールの別ロード方法__

```python
from sound.effects import echo 
```

この場合は次のように使える

```python
echo.echofilter(input, output, delay=0.7, atten=4) 
```

直接インポートも可能

```python
from sound.effects.echo import echofilter 
```

↓

```python
echofilter(input, output, delay=0.7, atten=4) 
```


