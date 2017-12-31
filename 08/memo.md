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
