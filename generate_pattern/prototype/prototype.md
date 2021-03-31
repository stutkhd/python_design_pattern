## 概要
**オブジェクトをコピーすることでオブジェクトを作る**
pythonのビルトイン機能で実現できる

## 例題
x、yのプロパティを持つ Point クラスをコピーします。

## 説明
copy.deepcopy(オブジェクト)でオブジェクトをコピーすることができる  
point1 = point2のように代入ではエイリアスが作られるだけでコピーには慣れない  

```python
point1 = Point(2, 3)
point2 = point1
point1.x = 5
print(point1.x)  # => 5
print(point2.x)  # => 5
```