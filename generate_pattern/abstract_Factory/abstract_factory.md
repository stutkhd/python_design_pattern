# Abstract Factory
## 概要
インスタンスの生成を専門に行うクラスを用意することで、間違いないように(複雑)なオブジェクトを作る、パターン

## 例題
ピザを作ることを考えます。

ピザは生地、ソース、トッピングからできます。  
工場Aでは、生地に小麦、ソースにトマト、トッピングにコーンを使用します。  
工場Bでは、生地に米粉、ソースにバジル、トッピングにチーズを使用します。  
すべての素材に確認のためのメソッド（check）をもたせます。

生地 -> dough  
小麦 -> wheat  
米粉 -> rice flour  

## 特徴
ピザ作成には、生地、ソース、トッピングが必要  
それぞれを配列に入れることでピザが完成する  

AbstractFactoryは素材と作り方があまり変わらない時、これらを抽象化するパターン

**抽象化** -> 具体的な値を取り除いて、引数で使い分ける感じ
```
CoanTopping(amount)
```
トッピング(作り方)とコーン(素材)を抽象化

これにより、別のピザを作りたくなってきた時は別の工場を作ることで、作るものの入れ替えを簡素化する。  

ソースコードにおけるピザの生地の流れ  
1. AbstractPizzaFactoryの中でself.add_doughが実行
2. self.factoryがPizzaFactoryAのインスタンスのため、PizzaFactoryAクラスのadd_dough()が呼ばれる
という流れ。

## new_pizza.pyはpythonらしく書いたver  
-> クラス内クラスを使用する  

Abstract Factoryを無くして、Factoryごとにクラスを追加して、Factory特有の処理をかく

材料は工場によって違って、工場ごとの専用クラスになっている  
ex)小麦生地クラス、トマトソースクラス、コーントッピングクラスは工場Aクラス専用のクラス  
Pythonでは、クラスの中にクラスを含めることができます。  

そこで、今回は  
工場のクラスに材料のクラスを含める

@classmethod -> クラスメソッド: クラスに紐づくメソッド  
インスタンスなしで実行できる

```
# インスタンスメソッドの場合
ins_method = Class_A()
ins_method.method(1,2,3)

# クラスメソッドの場合
Class_B().method(1,2,3)

```
