## 引用
今回はこちらからサンプルコードを引っ張っています
https://medium.com/since-i-want-to-start-blog-that-looks-like-men-do/python%E3%81%AB%E3%82%88%E3%82%8B%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3-bridge-2612ee0da3a9

## なぜBridgeを使うのか
抽出されたクラス -> 機能  
サポート環境やバージョン -> 実装

サポート環境やバージョンなどとは，
　　Windows向け，Linux向け，MacOS向け
　　プリンタ用，ディスプレイ用，通信用
　　巨人向け，阪神向け，楽天向け
などいろいろ考えられる  

これら向けに機能も色々追加したい場合は、機能ごとに全ての環境向けやバージョン向けに実装するのは面倒臭い
そのためにBridgeを用いて機能側と環境側を独立に変更，拡張，再利用することができるように機能側と環境側の橋渡し（Bridgeという）を工夫する

## 機能のクラス階層
単なる継承のこと  
機能をつけるために継承できる階層を昨日の階層クラスと呼ぶ
  
## 実装のクラス階層
抽象クラスによる継承のこと  
抽象クラスでは抽象メソッドで**インターフェース**を定義する  
具体的な中身を実装するために抽象クラスを継承し、サブクラスで関数を実装する  
この抽象クラスによる継承でできる階層を「実装のクラス階層」と呼ぶ

## いつ問題になるのか
実装のクラス階層に機能のクラスを混ぜたい時  
->  **抽象クラスに実装クラスとは別に、機能を付け加えるクラスを継承したい時**  

この時抽象クラスを継承して、機能(新たな関数)だけを付け加えるだけだとエラー出るらしい(抽象クラスに新しいの追加したら、具象の方はその新しい関数が追加されてないため)  
抽象クラスを継承するなら、抽象メソッドを全て実装していないといけないので、実装クラスと全く同じような関数を記述しなくてはいけません。  
-> 使わない関数を実装しなくちゃいけないから無駄  

## 実践
文字列を与えると囲って表示するアルゴリズムを考える
```
+-------------+
|Hello, Japan.|
+-------------+
```
- 上の模様(+ — — — — — — +)を表示する関数 — def open
- 真ん中の文字( |(string)|)を表示する関数 — def pprint
- 下の模様(+ — — — — — — +)を表示する関数 — def close  

に分けて定義し、抽象クラス(class DisplayImpl),サブクラス(class StringDisplayImpl)に分けて実装する  
そして表示方法に文字を5回表示させるmulti_display関数を持つクラス CountClassを別に作成する  
```
+----------------+
|Hello, Universe.|
|Hello, Universe.|
|Hello, Universe.|
|Hello, Universe.|
|Hello, Universe.|
+----------------+
```

## 説明
新しいclass Displayを作成し、抽象クラスDisplayImplと機能を加えるCountDisplayに挟み込む  
クラス図
```
<class Display> ------> <class DisalayImpl>
      ^                        ^
      |                        |
      |                        |
      |                        |
<class CountDisplay>   <class StringDisplayImpl>
```

(def main()の話)
環境側の具体的な動作を実装しているのはStringDisplayImplのみ.  
機能側の昨日はメソッドdisplayとメソッドmultiDisplayの２つ

環境側にクラスが追加された時は、読んでいるクラスStringDisplayImplだけを変えればいい  
機能側にメソッドが追加されたら、CountDisplayだけ変えればいい



重要なのはDisplay  
implというFieldを定義する。これはclass DiplayImplである。つまり自分自身の変数に**抽象クラス**のインスタンスを入れ込む  
そして、各関数の実装はimplのつまり、class DisplayImplの関数を実行していることになる  
これによって、Displayが抽象クラスDisplayImplと機能をつけるCountDisplayの橋渡し(Bridge)になり、class CountDisplayは継承によって機能multi_displayを加えることができる  

## 結論
クラス間を結びつける時に継承を使うと、結びつきが硬すぎてクラスの関係を変更する時に面倒臭い  
Bridgeを使い、クラスにField(impl)を置いて、そのFieldに別のインスタンスを代入して、クラス間を結びつけることを委譲(delegation)と呼ぶ

## 補足
Bridgeパターンと関連するパターン  
- Abstract Factory: このパターンでBridgeパターンに基づくインスタンスの生成と構築ができる  
- Adapter: このパターンは関係のないクラス同士を繋ぐ. このパターンは通常設計が終わったあとで適用される。  それに対し、Bridgeは抽出されたクラスと実装を独立に変更可能にするために設計の前段階で使われる。  
