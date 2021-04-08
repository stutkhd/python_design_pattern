## 概要
クラスを複数の方向に拡張させるパターン

## 例題
①：配列のソートをクイックソートまたはバブルソートで行います（方向①）

②：後に、①の機能に、ソートの時間を計測する機能を足します（方向②）

クイックソート・バブルソートについてはqiitaの記事よりお借りしたコードを用います。

```python
# バブルソート
def bsort(a):
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]

    return a


# クイックソート
def qsort(a):
    if len(a) in (0, 1):
        return a

    p = a[-1]
    left = [x for x in a[:-1] if x <= p]
    right = [x for x in a[:-1] if x > p]

    return qsort(left) + [p] + qsort(right)


# 簡易テスト
if __name__ == "__main__":
    print(bsort([2, 7, 3, 4, 9, 1]))
    print(qsort([2, 7, 3, 4, 9, 1]))
```

### 参考
[バブルソート](https://medium-company.com/%E3%83%90%E3%83%96%E3%83%AB%E3%82%BD%E3%83%BC%E3%83%88/)  
[クイックソート](https://medium-company.com/%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%82%BD%E3%83%BC%E3%83%88/)

### NotImplementedErrorについて
NotImplementedErrorは定義はされているが、中身は実装されていない関数などをよび出した時に発生する例外  

使用する状況  
1. 子クラスで実装することが前提の親クラスの関数が呼び出された時  
-> 今回はこれかも? SoftImple.sort()という実装にさせたくないってことかも  

2. 将来的に実装する予定はあるが、現状は実装されていない関数が呼び出された時  

SortImpleは基底クラスで、継承した子クラスでsort()を実装することが前提  
そのため、SortImple をオブジェクト化して sort() が呼び出されたり、継承した子クラスで sort() を実装していないなど、本来呼び出されないはずの SortImple クラスの sort() が呼び出されてしまったときに、それを知らせるために NotImplementedError を発生させるようになっている￥。

## 特徴
QuickSorter(), BubbleSorter()のコードの重複が解消される。  
一番大事なところはSorterクラスの以下の部分

```python
class Sorter:
    def __init__(self, sorter):
        self.sorter = sorter

    def sort(self, a):
        return self.sorter.sort(a)
```

アンチパターンではSorterクラスのsort()メソッドは実装されておらず、子クラスに実装が任される。  
これを委譲(オブジェクトのメソッドに振る舞いを委譲すること)することで、柔軟な振る舞いをできるようにしている。