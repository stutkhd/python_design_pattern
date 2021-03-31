## 概要
オブジェクト作成時に、作成するオブジェクトのクラスをサブクラスに選ばせる

## 例題
牛（Cow）を作る工場と鶏（Chicken）を作る工場があるとします。

出荷された動物のチェックとして餌を与え、鳴き声のチェックを行います。  
（各animalに対し eat() と speak() をさせる）

## 特徴
大事なのは以下の部分

```python
class Factory:
    def __init__(self):
        self.animal = self.factory_method()

    # check_animal関数

    @abc.abstractmethod
    def factory_method(self):
        pass
```

self.animalに対してself.factory_method()関数で作成したオブジェクトを代入しているが、self.factory_method()自体は抽象メソッドであり、**子クラスにオブジェクトの生成を選択させている。** (子クラスはFactoryメソッドを継承しているCowFactoryなど)  
子クラスは内部のfactory_methodで特定の関数を選択して実行している。

例えば、以下のようなコードでも対応できる

```python
class Factory:
    def __init__(self, animal_name):
        if animal_name == "cow":
            self.animal = Cow()
        elif animal_name == "chicken":
            self.animal = Chicken()

    # あと同じ
```

このようにかくと、牛、鶏以外に新しいクラスを追加する時に、if文も書き換える必要が出てくる。

## pythonらしく書く
1. pythonは動的型付け言語なため、Animalクラスは省略することの方が多い  
2. pythonはクラスが第１級オブジェクトである、が使える  

第一級オブジェクトとは簡単にいうと、「変数に入れたりすることができる」  
例
```python
class Hoge:
    def test(self):
        print("hoge")

hoge_class_copied = Hoge
hoge_instance = hoge_class_copied()
hoge_instance.test()  # => hoge
```
このようにHogeを一度変数に入れても使用できる。
この特性を使うとfactory_methodが不要になる。

一番大事なところは self.animal = animal_class() の1行で、ここでクラスを指定することで
**「オブジェクト作成時に、作成するオブジェクトのクラスをサブクラスに選ばせる」**ことを実現しています。